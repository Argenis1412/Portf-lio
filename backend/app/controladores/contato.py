"""
Controlador de contato.

Endpoint:
- POST /api/contato
"""

from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Request

from app.esquemas.contato import RequisicaoContato, RespostaContato
from app.casos_uso import EnviarContatoUseCase
from app.controladores.dependencias import obter_enviar_contato_use_case
from app.core.excecoes import ErroInfraestrutura
from app.core.limite import limiter
from app.core.idempotencia import verificar_idempotencia, store, content_store
from app.core.honeypot import is_honeypot_triggered
from app.core.spam_check import calculate_spam_score
import hashlib
import logging

logger = logging.getLogger(__name__)

roteador = APIRouter(tags=["Contato"])


@roteador.post(
    "/contato",
    response_model=RespostaContato,
    summary="Send contact message",
    description="Submits a contact form message via Formspree. Rate limited to 5 requests/minute.",
    responses={
        200: {"description": "Message sent successfully"},
        429: {"description": "Too many requests - rate limit exceeded"},
        500: {"description": "Failed to deliver message via external service"},
    },
)
@limiter.limit("5/minute; 5/hour")
async def enviar_contato(
    request: Request,
    requisicao: RequisicaoContato,
    enviar_contato_uc: Annotated[
        EnviarContatoUseCase,
        Depends(obter_enviar_contato_use_case),
    ],
    idempotency_key: Annotated[Optional[str], Depends(verificar_idempotencia)] = None,
) -> RespostaContato:
    # 1. Honeypot Check (Direct Bot Trap)
    # Precisamos ler o corpo bruto para ver campos que não estão no esquema Pydantic
    try:
        raw_body = await request.json()
        if is_honeypot_triggered(raw_body):
            logger.info(
                "contact_blocked",
                extra={
                    "classification": "HONEYPOT",
                    "action": "silent_drop",
                    "honeypot_fields": [
                        field for field in ("website", "fax", "company", "middle_name")
                        if raw_body.get(field)
                    ],
                },
            )
            return RespostaContato(
                sucesso=True,
                mensagem="Mensagem enviada com sucesso! Retornarei em breve.",
            )
    except Exception:
        # Se não for JSON ou falhar, continuamos com os dados validados
        pass

    # 2. Spam Scoring (Heuristic Filter)
    spam_score = calculate_spam_score(requisicao.mensagem, requisicao.email)
    
    # SILENT_SPAM (> 70)
    if spam_score > 70:
        logger.info(
            "contact_classified",
            extra={
                "classification": "SILENT_SPAM",
                "action": "silent_drop",
                "spam_score": spam_score,
                "email_domain": requisicao.email.split("@")[-1].lower(),
            },
        )
        return RespostaContato(
            sucesso=True,
            mensagem="Mensagem enviada com sucesso! Retornarei em breve.",
        )

    # 3. Verificação de conteúdo duplicado (Deduplicação de 5 minutos)
    content_str = f"{requisicao.email.lower()}:{requisicao.mensagem.strip()}"
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()
    
    if content_store.check_duplicate(content_hash):
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="DUPLICATE_CONTENT"
        )

    # SUSPECT (> 30)
    is_suspicious = spam_score > 30
    if is_suspicious:
        logger.info(
            "contact_classified",
            extra={
                "classification": "SUSPECT",
                "action": "deliver_with_flag",
                "spam_score": spam_score,
                "email_domain": requisicao.email.split("@")[-1].lower(),
            },
        )
    else:
        logger.info(
            "contact_classified",
            extra={
                "classification": "NORMAL",
                "action": "deliver",
                "spam_score": spam_score,
                "email_domain": requisicao.email.split("@")[-1].lower(),
            },
        )

    sucesso = await enviar_contato_uc.executar(
        nome=requisicao.nome,
        email=requisicao.email,
        assunto=requisicao.assunto,
        mensagem=requisicao.mensagem,
        is_suspicious=is_suspicious,
    )
    
    if sucesso:
        # Registrar conteúdo para evitar duplicatas nos próximos 5 minutos
        content_store.add(content_hash)
    else:
        raise ErroInfraestrutura(
            mensagem="Falha ao enviar mensagem de contato",
            codigo="ERRO_ENVIO_CONTATO",
            origem="formspree",
        )
    
    resposta = RespostaContato(
        sucesso=True,
        mensagem="Mensagem enviada com sucesso! Retornarei em breve.",
    )

    if idempotency_key:
        # Cache da resposta de sucesso
        store.set(idempotency_key, 200, resposta.model_dump())
    
    return resposta
