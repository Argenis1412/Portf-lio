"""
Módulo principal da aplicação FastAPI.

Este módulo configura a aplicação FastAPI com:
- CORS para desenvolvimento local (localhost:5173)
- Endpoint de health check (/saude)
- Rotas da API (/api/*)
- Documentação automática (/docs)

Arquitetura: Clean Architecture simplificada
- Controllers (HTTP) → Use Cases (lógica) → Entities (domínio) → Adapters (externos)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configuracao import configuracoes
from app.controladores import roteador_saude, roteador_api, roteador_contato


def criar_aplicacao() -> FastAPI:
    """
    Cria e configura a aplicação FastAPI.

    Returns:
        FastAPI: Instância configurada da aplicação.

    Configurações aplicadas:
        - Título e descrição para documentação OpenAPI
        - CORS para origens permitidas
        - Rotas de health check e API
    """
    aplicacao = FastAPI(
        title=configuracoes.nome_app,
        description="API REST para portfólio de desenvolvedor backend. "
                    "Demonstra Clean Architecture, validação Pydantic e testes.",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    _configurar_cors(aplicacao)
    _registrar_rotas(aplicacao)

    return aplicacao


def _configurar_cors(aplicacao: FastAPI) -> None:
    """
    Configura CORS (Cross-Origin Resource Sharing).

    Args:
        aplicacao: Instância FastAPI para configurar.

    Permite requisições do frontend em localhost:5173 (Vite dev server).
    """
    aplicacao.add_middleware(
        CORSMiddleware,
        allow_origins=configuracoes.lista_origens_permitidas(),
        allow_credentials=False,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )


def _registrar_rotas(aplicacao: FastAPI) -> None:
    """
    Registra todos os roteadores na aplicação.

    Args:
        aplicacao: Instância FastAPI para registrar rotas.

    Rotas registradas:
        - /saude: Health check (sem prefixo)
        - /api/*: Endpoints da API
    """
    aplicacao.include_router(roteador_saude)
    aplicacao.include_router(roteador_api, prefix="/api")
    aplicacao.include_router(roteador_contato, prefix="/api")


# Instância global da aplicação (usada pelo uvicorn)
app = criar_aplicacao()