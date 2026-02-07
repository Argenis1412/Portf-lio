"""
Controlador de health check.

Endpoint simples para verificar se a API está respondendo.
Usado por load balancers, kubernetes probes e monitoramento.
"""

from fastapi import APIRouter

from app.esquemas.saude import RespostaSaude

roteador = APIRouter(tags=["Saúde"])


@roteador.get(
    "/saude",
    response_model=RespostaSaude,
    summary="Health check da API",
    description="Retorna status OK se a API está funcionando.",
)
def verificar_saude() -> RespostaSaude:
    """
    Verifica se a API está saudável.

    Returns:
        RespostaSaude: Status "ok" e mensagem de confirmação.

    Example:
        GET /saude
        → {"status": "ok", "mensagem": "API funcionando normalmente"}
    """
    return RespostaSaude(
        status="ok",
        mensagem="API funcionando normalmente",
    )