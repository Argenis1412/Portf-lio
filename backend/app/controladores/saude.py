"""
Controlador de health check.

Endpoint simples para verificar se a API está respondendo.
Usado por load balancers, kubernetes probes e monitoramento.
"""

import time
from fastapi import APIRouter

from app.esquemas.saude import RespostaSaude
from app.configuracao import configuracoes

roteador = APIRouter(tags=["Health"])

# Timestamp de inicialização da aplicação
_INICIO_APLICACAO = time.time()


@roteador.get(
    "/saude",
    response_model=RespostaSaude,
    summary="API health check",
    description="Returns OK if the API is running. Includes version, environment, and uptime.",
    responses={
        200: {"description": "API is healthy and running"},
    },
)
def verificar_saude() -> RespostaSaude:
    """
    Verifica se a API está saudável.

    Returns:
        RespostaSaude: Status, versão, ambiente e uptime.

    Example:
        GET /saude
        → {
            "status": "ok",
            "mensagem": "API funcionando normalmente",
            "versao_api": "1.0.0",
            "ambiente": "local",
            "uptime_segundos": 3600
        }
    """
    uptime = int(time.time() - _INICIO_APLICACAO)
    
    return RespostaSaude(
        status="ok",
        mensagem="API funcionando normalmente",
        versao_api="1.0.0",
        ambiente=configuracoes.ambiente,
        uptime_segundos=uptime,
    )