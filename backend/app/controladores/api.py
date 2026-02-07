"""
Controlador de rotas da API.

Endpoints:
- GET /api/sobre
- GET /api/projetos
- GET /api/projetos/{projeto_id}
- GET /api/stack
- GET /api/experiencias
"""

from fastapi import APIRouter, HTTPException

from app.esquemas.sobre import RespostaSobre
from app.esquemas.projetos import ProjetoResumo, ProjetoDetalhado, RespostaProjetos
from app.esquemas.stack import ItemStack, RespostaStack
from app.esquemas.experiencias import Experiencia, RespostaExperiencias
from app.casos_uso import (
    ObterSobreUseCase,
    ObterProjetosUseCase,
    ObterProjetoPorIdUseCase,
    ObterStackUseCase,
    ObterExperienciasUseCase,
)
from app.adaptadores import RepositorioJSON

# Dependency injection manual
_repositorio = RepositorioJSON()
_obter_sobre_uc = ObterSobreUseCase(_repositorio)
_obter_projetos_uc = ObterProjetosUseCase(_repositorio)
_obter_projeto_por_id_uc = ObterProjetoPorIdUseCase(_repositorio)
_obter_stack_uc = ObterStackUseCase(_repositorio)
_obter_experiencias_uc = ObterExperienciasUseCase(_repositorio)

roteador = APIRouter(tags=["API"])


@roteador.get(
    "/sobre",
    response_model=RespostaSobre,
    summary="Informações pessoais",
    description="Retorna informações da seção 'Sobre Mim'.",
)
def obter_sobre() -> RespostaSobre:
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
    dados = _obter_sobre_uc.executar()
    return RespostaSobre(**dados)


@roteador.get(
    "/projetos",
    response_model=RespostaProjetos,
    summary="Listar projetos",
    description="Retorna lista de projetos ordenada (destacados primeiro).",
)
def listar_projetos() -> RespostaProjetos:
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
    projetos = _obter_projetos_uc.executar()
    
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
        404: {"description": "Projeto não encontrado"},
    },
)
def obter_projeto(projeto_id: str) -> ProjetoDetalhado:
    """
    Obtém detalhes completos de um projeto.

    Args:
        projeto_id: ID do projeto a buscar.

    Returns:
        ProjetoDetalhado: Informações completas do projeto.

    Raises:
        HTTPException 404: Se projeto não existe.

    Example:
        GET /api/projetos/portfolio-api
        → {
            "id": "portfolio-api",
            "nome": "Portfolio API",
            ...
        }
    """
    projeto = _obter_projeto_por_id_uc.executar(projeto_id)
    
    if not projeto:
        raise HTTPException(
            status_code=404,
            detail=f"Projeto '{projeto_id}' não encontrado",
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
def obter_stack() -> RespostaStack:
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
    por_categoria = _obter_stack_uc.executar()
    
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
def listar_experiencias() -> RespostaExperiencias:
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
    experiencias = _obter_experiencias_uc.executar()
    
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
