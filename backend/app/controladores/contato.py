"""
Controlador de contato.

Endpoint:
- POST /api/contato
"""

from fastapi import APIRouter, Request

from app.esquemas.contato import RequisicaoContato, RespostaContato
from app.casos_uso import EnviarContatoUseCase
from app.adaptadores import FormspreeEmailAdaptador, LoggerEstruturado
from app.configuracao import configuracoes
from app.core.excecoes import ErroInfraestrutura
from app.core.limite import limiter

# Dependency injection manual
_email_adaptador = FormspreeEmailAdaptador(
    configuracoes.formspree_url,
    configuracoes.formspree_form_id,
)
_logger = LoggerEstruturado()
_enviar_contato_uc = EnviarContatoUseCase(_email_adaptador, _logger)

roteador = APIRouter(tags=["Contato"])


@roteador.post(
    "/contato",
    response_model=RespostaContato,
    summary="Enviar mensagem de contato",
    description="Envia mensagem do formulário de contato via Formspree.",
    responses={
        500: {"description": "Erro ao enviar mensagem"},
        429: {"description": "Muitas requisições"},
    },
)
@limiter.limit("5/minute")
async def enviar_contato(
    request: Request,
    requisicao: RequisicaoContato,
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
    sucesso = await _enviar_contato_uc.executar(
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
    
    return RespostaContato(
        sucesso=True,
        mensagem="Mensagem enviada com sucesso! Retornarei em breve.",
    )
