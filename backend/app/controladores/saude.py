"""
Controlador de health check.

Endpoint simples para verificar se a API está respondendo.
Usado por load balancers, kubernetes probes e monitoramento.
"""

import time
from fastapi import APIRouter

from app.esquemas.saude import RespostaSaude
from app.configuracao import configuracoes

roteador = APIRouter(tags=["Saúde"])

# Timestamp de inicialização da aplicação
_INICIO_APLICACAO = time.time()


@roteador.get(
    "/saude",
    response_model=RespostaSaude,
    summary="Health check da API",
    description="Retorna status OK se a API está funcionando. "
                "Inclui versão, ambiente e uptime.",
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