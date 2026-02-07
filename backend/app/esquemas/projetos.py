"""
Schemas para endpoints /api/projetos e /api/projetos/{id}.

Define contratos para listagem e detalhes de projetos.
"""

from pydantic import BaseModel, Field, HttpUrl


class ProjetoResumo(BaseModel):
    """
    Resumo de projeto para listagem.

    Usado no endpoint GET /api/projetos.
    """

    id: str = Field(
        ...,
        examples=["portfolio-api"],
        description="Identificador único do projeto",
    )
    nome: str = Field(
        ...,
        max_length=100,
        examples=["Portfolio API"],
        description="Nome do projeto",
    )
    descricao_curta: str = Field(
        ...,
        max_length=200,
        examples=["API REST com FastAPI e Clean Architecture"],
        description="Descrição breve do projeto",
    )
    tecnologias: list[str] = Field(
        ...,
        examples=[["Python", "FastAPI", "Pydantic"]],
        description="Lista de tecnologias utilizadas",
    )
    destaque: bool = Field(
        default=False,
        description="Se o projeto deve ser destacado",
    )


class ProjetoDetalhado(BaseModel):
    """
    Detalhes completos de um projeto.

    Usado no endpoint GET /api/projetos/{id}.
    """

    id: str = Field(
        ...,
        examples=["portfolio-api"],
        description="Identificador único do projeto",
    )
    nome: str = Field(
        ...,
        max_length=100,
        examples=["Portfolio API"],
        description="Nome do projeto",
    )
    descricao_curta: str = Field(
        ...,
        max_length=200,
        examples=["API REST com FastAPI e Clean Architecture"],
        description="Descrição breve",
    )
    descricao_completa: str = Field(
        ...,
        max_length=2000,
        examples=["API REST desenvolvida com FastAPI demonstrando..."],
        description="Descrição detalhada do projeto",
    )
    tecnologias: list[str] = Field(
        ...,
        examples=[["Python", "FastAPI", "Pydantic", "Pytest"]],
        description="Lista de tecnologias utilizadas",
    )
    funcionalidades: list[str] = Field(
        ...,
        examples=[["Health check", "CRUD de projetos", "Validação"]],
        description="Lista de funcionalidades principais",
    )
    aprendizados: list[str] = Field(
        ...,
        examples=[["Clean Architecture", "Testes unitários"]],
        description="O que foi aprendido no projeto",
    )
    repositorio: HttpUrl | None = Field(
        default=None,
        examples=["https://github.com/argenis972/Portf-lio"],
        description="URL do repositório",
    )
    demo: HttpUrl | None = Field(
        default=None,
        examples=["https://portfolio-api.railway.app"],
        description="URL da demo ao vivo",
    )
    destaque: bool = Field(
        default=False,
        description="Se o projeto deve ser destacado",
    )


class RespostaProjetos(BaseModel):
    """
    Resposta da listagem de projetos.

    Attributes:
        projetos: Lista de projetos resumidos.
        total: Quantidade total de projetos.
    """

    projetos: list[ProjetoResumo] = Field(
        ...,
        description="Lista de projetos",
    )
    total: int = Field(
        ...,
        ge=0,
        examples=[3],
        description="Total de projetos",
    )