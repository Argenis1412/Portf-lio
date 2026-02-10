"""
Middleware de requisições HTTP.

Adiciona:
- Request ID único para rastreamento
- Logging estruturado de cada requisição
- Medição de tempo de resposta
- Headers customizados de resposta
"""

import time
import uuid
import logging
from typing import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

logger = logging.getLogger(__name__)


class MiddlewareRequisicao(BaseHTTPMiddleware):
    """
    Middleware para processar todas as requisições HTTP.

    Funcionalidades:
        - Gera request_id único (UUID4)
        - Adiciona request_id nos logs
        - Mede tempo de resposta
        - Loga método, path, status e duração
        - Adiciona headers: X-Request-ID, X-Response-Time
    """

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: Callable,
    ) -> Response:
        """
        Processa requisição e adiciona metadados.

        Args:
            request: Requisição HTTP recebida.
            call_next: Próximo handler na cadeia.

        Returns:
            Response: Resposta com headers adicionais.
        """
        # Gerar ID único para rastreamento
        request_id = str(uuid.uuid4())
        
        # Adicionar request_id no state do request
        request.state.request_id = request_id
        
        # Timestamp de início
        inicio = time.time()
        
        # Log da requisição recebida
        logger.info(
            f"Requisição recebida",
            extra={
                "request_id": request_id,
                "metodo": request.method,
                "path": request.url.path,
                "query": str(request.url.query) if request.url.query else None,
                "client_ip": request.client.host if request.client else None,
            },
        )
        
        # Processar requisição
        try:
            response = await call_next(request)
        except Exception as exc:
            # Log de erro e re-raise para handlers tratarem
            logger.error(
                f"Erro durante processamento da requisição",
                extra={
                    "request_id": request_id,
                    "erro": str(exc),
                },
                exc_info=True,
            )
            raise
        
        # Calcular tempo de resposta
        duracao_ms = (time.time() - inicio) * 1000
        
        # Adicionar headers customizados
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Response-Time"] = f"{duracao_ms:.2f}ms"
        
        # Log da resposta enviada
        logger.info(
            f"Resposta enviada",
            extra={
                "request_id": request_id,
                "metodo": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duracao_ms": round(duracao_ms, 2),
            },
        )
        
        return response


def configurar_logging() -> None:
    """
    Configura logging estruturado para a aplicação.

    Formato:
        JSON-like para facilitar parsing em ferramentas de observabilidade.
    
    Configuração:
        - Nível: INFO
        - Handler: Console (stdout)
        - Formato: timestamp, level, logger, mensagem, extras
    """
    formato = (
        "%(asctime)s | %(levelname)-8s | %(name)s | "
        "%(message)s | %(request_id)s"
    )
    
    logging.basicConfig(
        level=logging.INFO,
        format=formato,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    
    # Definir valor padrão para request_id nos logs
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    
    # Configurar filtro para adicionar request_id quando disponível
    class RequestIDFilter(logging.Filter):
        def filter(self, record):
            if not hasattr(record, 'request_id'):
                record.request_id = '-'
            return True
    
    # Adicionar filtro a todos os loggers
    for handler in logging.root.handlers:
        handler.addFilter(RequestIDFilter())
    
    logger.info("Logging configurado com sucesso")
