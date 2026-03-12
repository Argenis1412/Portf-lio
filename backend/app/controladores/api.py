"""
Controlador de rotas da API.

Endpoints:
- GET /api/sobre
- GET /api/projetos
- GET /api/projetos/{projeto_id}
- GET /api/stack
- GET /api/experiencias
"""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.esquemas.sobre import RespostaSobre
from app.esquemas.projetos import ProjetoResumo, ProjetoDetalhado, RespostaProjetos
from app.esquemas.stack import ItemStack, RespostaStack
from app.esquemas.experiencias import Experiencia, RespostaExperiencias
from app.casos_uso import (
    ObterExperienciasUseCase,
    ObterProjetoPorIdUseCase,
    ObterProjetosUseCase,
    ObterSobreUseCase,
    ObterStackUseCase,
)
from app.controladores.dependencias import (
    obter_obter_experiencias_use_case,
    obter_obter_projeto_por_id_use_case,
    obter_obter_projetos_use_case,
    obter_obter_sobre_use_case,
    obter_obter_stack_use_case,
)
from app.core.excecoes import ErroRecursoNaoEncontrado

roteador = APIRouter(tags=["API"])


@roteador.get(
    "/sobre",
    response_model=RespostaSobre,
    summary="Informações pessoais",
    description="Retorna informações da seção 'Sobre Mim'.",
)
async def obter_sobre(
    obter_sobre_uc: Annotated[
        ObterSobreUseCase,
        Depends(obter_obter_sobre_use_case),
    ],
) -> RespostaSobre:
    """
    Obtém informações pessoais do desenvolvedor.

    Returns:
        RespostaSobre: Dados pessoais validados.

    Example:
        GET /api/sobre
        → {
            "nome": "Argenis Lopez",
            "titulo": "Backend Developer | Python | FastAPI",
            ...
        }
    """
    dados = await obter_sobre_uc.executar()
    return RespostaSobre(**dados)


@roteador.get(
    "/projetos",
    response_model=RespostaProjetos,
    summary="Listar projetos",
    description="Retorna lista de projetos ordenada (destacados primeiro).",
)
async def listar_projetos(
    obter_projetos_uc: Annotated[
        ObterProjetosUseCase,
        Depends(obter_obter_projetos_use_case),
    ],
) -> RespostaProjetos:
    """
    Lista todos os projetos do portfólio.

    Returns:
        RespostaProjetos: Lista de projetos resumidos.

    Ordenação:
        Projetos em destaque aparecem primeiro, depois ordem alfabética.

    Example:
        GET /api/projetos
        → {
            "projetos": [...],
            "total": 3
        }
    """
    projetos = await obter_projetos_uc.executar()
    
    projetos_resumo = [
        ProjetoResumo(
            id=p.id,
            nome=p.nome,
            descricao_curta=p.descricao_curta,
            tecnologias=p.tecnologias,
            destaque=p.destaque,
        )
        for p in projetos
    ]
    
    return RespostaProjetos(
        projetos=projetos_resumo,
        total=len(projetos_resumo),
    )


@roteador.get(
    "/projetos/{projeto_id}",
    response_model=ProjetoDetalhado,
    summary="Detalhes de um projeto",
    description="Retorna informações completas de um projeto específico.",
    responses={
        200: {
            "description": "Projeto encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "id": "portfolio-api",
                        "nome": "Portfolio API",
                        "descricao_curta": "API REST profissional",
                        "descricao_completa": "Descrição detalhada...",
                        "tecnologias": ["Python", "FastAPI"],
                        "funcionalidades": ["CRUD", "Validação"],
                        "aprendizados": ["Clean Architecture"],
                        "repositorio": "https://github.com/...",
                        "demo": None,
                        "destaque": True,
                    }
                }
            },
        },
        404: {
            "description": "Projeto não encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "erro": {
                            "codigo": "PROJETO_NAO_ENCONTRADO",
                            "mensagem": "Projeto 'xyz' não encontrado",
                        }
                    }
                }
            },
        },
    },
)
async def obter_projeto(
    projeto_id: str,
    obter_projeto_por_id_uc: Annotated[
        ObterProjetoPorIdUseCase,
        Depends(obter_obter_projeto_por_id_use_case),
    ],
) -> ProjetoDetalhado:
    """
    Obtém detalhes completos de um projeto.

    Args:
        projeto_id: ID do projeto a buscar.

    Returns:
        ProjetoDetalhado: Informações completas do projeto.

    Raises:
        ErroRecursoNaoEncontrado: Se projeto não existe.

    Example:
        GET /api/projetos/portfolio-api
        → {
            "id": "portfolio-api",
            "nome": "Portfolio API",
            ...
        }
    """
    projeto = await obter_projeto_por_id_uc.executar(projeto_id)
    
    if not projeto:
        raise ErroRecursoNaoEncontrado(
            mensagem=f"Projeto '{projeto_id}' não encontrado",
            codigo="PROJETO_NAO_ENCONTRADO",
        )
    
    return ProjetoDetalhado(
        id=projeto.id,
        nome=projeto.nome,
        descricao_curta=projeto.descricao_curta,
        descricao_completa=projeto.descricao_completa,
        tecnologias=projeto.tecnologias,
        funcionalidades=projeto.funcionalidades,
        aprendizados=projeto.aprendizados,
        repositorio=projeto.repositorio,
        demo=projeto.demo,
        destaque=projeto.destaque,
    )


@roteador.get(
    "/stack",
    response_model=RespostaStack,
    summary="Stack tecnológico",
    description="Retorna tecnologias organizadas por categoria.",
)
async def obter_stack(
    obter_stack_uc: Annotated[
        ObterStackUseCase,
        Depends(obter_obter_stack_use_case),
    ],
) -> RespostaStack:
    """
    Obtém stack tecnológico organizado.

    Returns:
        RespostaStack: Tecnologias agrupadas por categoria.

    Example:
        GET /api/stack
        → {
            "stack": [...],
            "por_categoria": {
                "backend": [...],
                "frontend": [...]
            }
        }
    """
    por_categoria = await obter_stack_uc.executar()
    
    # Converter para ItemStack
    stack_completo = []
    por_categoria_validado: dict[str, list[ItemStack]] = {}
    
    for categoria, itens in por_categoria.items():
        itens_validados = [ItemStack(**item) for item in itens]
        por_categoria_validado[categoria] = itens_validados
        stack_completo.extend(itens_validados)
    
    return RespostaStack(
        stack=stack_completo,
        por_categoria=por_categoria_validado,
    )


@roteador.get(
    "/experiencias",
    response_model=RespostaExperiencias,
    summary="Experiências profissionais",
    description="Retorna lista de experiências ordenadas cronologicamente.",
)
async def listar_experiencias(
    obter_experiencias_uc: Annotated[
        ObterExperienciasUseCase,
        Depends(obter_obter_experiencias_use_case),
    ],
) -> RespostaExperiencias:
    """
    Lista experiências profissionais.

    Returns:
        RespostaExperiencias: Lista ordenada de experiências.

    Ordenação:
        Experiência atual primeiro, depois por data (mais recente primeiro).

    Example:
        GET /api/experiencias
        → {
            "experiencias": [...],
            "total": 2
        }
    """
    experiencias = await obter_experiencias_uc.executar()
    
    experiencias_schema = [
        Experiencia(
            id=e.id,
            cargo=e.cargo,
            empresa=e.empresa,
            localizacao=e.localizacao,
            data_inicio=e.data_inicio,
            data_fim=e.data_fim,
            descricao=e.descricao,
            tecnologias=e.tecnologias,
            atual=e.atual,
        )
        for e in experiencias
    ]
    
    return RespostaExperiencias(
        experiencias=experiencias_schema,
        total=len(experiencias_schema),
    )
