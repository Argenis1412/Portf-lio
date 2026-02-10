"""
Módulo principal da aplicação FastAPI.

Este módulo configura a aplicação FastAPI com:
- CORS para desenvolvimento local (localhost:5173)
- Middleware de requisições (request_id, logging, tempo de resposta)
- Handlers globais de exceções
- Endpoint de health check (/saude)
- Rotas da API versionadas (/api/v1/*)
- Rotas legadas para retrocompatibilidade (/api/*)
- Documentação automática (/docs)

Arquitetura: Clean Architecture simplificada
- Controllers (HTTP) → Use Cases (lógica) → Entities (domínio) → Adapters (externos)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configuracao import configuracoes
from app.controladores import roteador_saude, roteador_api, roteador_contato
from app.controladores.v1 import roteador_v1
from app.core.middleware import MiddlewareRequisicao
from app.core.handlers import registrar_handlers_excecao


def criar_aplicacao() -> FastAPI:
    """
    Cria e configura a aplicação FastAPI.

    Returns:
        FastAPI: Instância configurada da aplicação.

    Configurações aplicadas:
        - Título e descrição para documentação OpenAPI
        - CORS para origens permitidas
        - Middleware de requisições
        - Handlers de exceções
        - Rotas versionadas e legadas
        - Logging estruturado
    """
    # Configurar logging antes de criar app
    # Logging estruturado configurado automaticamente via middleware
    
    aplicacao = FastAPI(
        title=configuracoes.nome_app,
        description=_obter_descricao_api(),
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_tags=_obter_tags_openapi(),
    )

    _configurar_cors(aplicacao)
    _configurar_middleware(aplicacao)
    _registrar_handlers(aplicacao)
    _registrar_rotas(aplicacao)

    return aplicacao


def _obter_descricao_api() -> str:
    """
    Retorna descrição markdown para documentação OpenAPI.

    Returns:
        str: Descrição formatada em markdown.
    """
    return """
    API REST para portfólio de desenvolvedor backend.

    ## Arquitetura
    - **Clean Architecture**: Controllers → Use Cases → Entities → Adapters
    - **Validação**: Pydantic V2
    - **Testes**: pytest com cobertura
    - **Logging**: Estruturado com request_id

    ## Versionamento
    - **v1**: `/api/v1/*` (recomendado para novos consumidores)
    - **Legacy**: `/api/*` (retrocompatibilidade, será descontinuado)

    ## Padrão de Resposta
    - **Sucesso**: Retorna dados validados diretamente
    - **Erro**: 
      ```json
      {
        "erro": {
          "codigo": "CODIGO_ERRO",
          "mensagem": "Descrição legível",
          "detalhes": {...}
        }
      }
      ```

    ## Códigos HTTP
    - `200`: Sucesso
    - `400`: Erro de regra de negócio
    - `404`: Recurso não encontrado
    - `422`: Validação de entrada falhou
    - `500`: Erro interno do servidor

    ## Headers Customizados
    - `X-Request-ID`: ID único para rastreamento
    - `X-Response-Time`: Tempo de resposta em ms
    """


def _obter_tags_openapi() -> list[dict]:
    """
    Define tags para agrupar endpoints na documentação.

    Returns:
        list[dict]: Lista de tags com descrições.
    """
    return [
        {
            "name": "Saúde",
            "description": "Health check e status da aplicação",
        },
        {
            "name": "API v1",
            "description": "Versão 1 da API (recomendado)",
        },
        {
            "name": "Portfólio",
            "description": "Dados do portfólio (sobre, projetos, stack, experiências)",
        },
        {
            "name": "Contato",
            "description": "Envio de mensagens de contato",
        },
    ]


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


def _configurar_middleware(aplicacao: FastAPI) -> None:
    """
    Configura middleware da aplicação.

    Args:
        aplicacao: Instância FastAPI.

    Middleware aplicado:
        - MiddlewareRequisicao: request_id, logging, tempo de resposta
    """
    aplicacao.add_middleware(MiddlewareRequisicao)


def _registrar_handlers(aplicacao: FastAPI) -> None:
    """
    Registra handlers globais de exceções.

    Args:
        aplicacao: Instância FastAPI.
    """
    registrar_handlers_excecao(aplicacao)


def _registrar_rotas(aplicacao: FastAPI) -> None:
    """
    Registra todos os roteadores na aplicação.

    Args:
        aplicacao: Instância FastAPI para registrar rotas.

    Rotas registradas:
        - /saude: Health check (sem prefixo)
        - /api/v1/*: API versionada (recomendado)
        - /api/*: Rotas legadas (retrocompatibilidade)
    """
    # Health check (sem prefixo, usado por probes)
    aplicacao.include_router(roteador_saude)
    
    # API v1 (recomendado)
    aplicacao.include_router(roteador_v1, prefix="/api")
    
    # Rotas legadas (retrocompatibilidade - serão descontinuadas)
    aplicacao.include_router(roteador_api, prefix="/api", tags=["Legacy"])
    aplicacao.include_router(roteador_contato, prefix="/api", tags=["Legacy"])


# Instância global da aplicação (usada pelo uvicorn)
app = criar_aplicacao()