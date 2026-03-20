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
from app.core.idempotencia import verificar_idempotencia, store

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
@limiter.limit("5/minute")
async def enviar_contato(
    request: Request,
    requisicao: RequisicaoContato,
    enviar_contato_uc: Annotated[
        EnviarContatoUseCase,
        Depends(obter_enviar_contato_use_case),
    ],
    idempotency_key: Annotated[Optional[str], Depends(verificar_idempotencia)] = None,
) -> RespostaContato:
    """
    Envia mensagem de contato.

    Args:
        requisicao: Dados validados do formulário.

    Returns:
        RespostaContato: Resultado do envio.

    Raises:
        ErroInfraestrutura: Se falha ao enviar.

    Example:
        POST /api/contato
        {
            "nome": "Maria Silva",
            "email": "maria@example.com",
            "assunto": "Contato",
            "mensagem": "Olá!"
        }
        → {
            "sucesso": true,
            "mensagem": "Mensagem enviada com sucesso!"
        }
    """
    sucesso = await enviar_contato_uc.executar(
        nome=requisicao.nome,
        email=requisicao.email,
        assunto=requisicao.assunto,
        mensagem=requisicao.mensagem,
    )
    
    if not sucesso:
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
