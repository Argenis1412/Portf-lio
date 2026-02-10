"""
Controlador de contato.

Endpoint:
- POST /api/contato
"""

from fastapi import APIRouter, HTTPException

from app.esquemas.contato import RequisicaoContato, RespostaContato
from app.casos_uso import EnviarContatoUseCase
from app.adaptadores import FormspreeEmailAdaptador, LoggerEstruturado
from app.configuracao import configuracoes

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
    },
)
async def enviar_contato(requisicao: RequisicaoContato) -> RespostaContato:
    """
    Envia mensagem de contato.

    Args:
        requisicao: Dados validados do formulário.

    Returns:
        RespostaContato: Resultado do envio.

    Raises:
        HTTPException 500: Se falha ao enviar.

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
        raise HTTPException(
            status_code=500,
            detail="Erro ao enviar mensagem. Tente novamente mais tarde.",
        )
    
    return RespostaContato(
        sucesso=True,
        mensagem="Mensagem enviada com sucesso! Retornarei em breve.",
    )
