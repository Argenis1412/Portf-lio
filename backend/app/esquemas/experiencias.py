"""
Schemas para endpoint /api/experiencias.

Define contratos para listagem de experiências profissionais.
"""

from pydantic import BaseModel, Field
from datetime import date


class Experiencia(BaseModel):
    """
    Uma experiência profissional.

    Attributes:
        id: Identificador único.
        cargo: Título do cargo.
        empresa: Nome da empresa.
        localizacao: Localização do trabalho.
        data_inicio: Data de início.
        data_fim: Data de término (None se atual).
        descricao: Descrição das atividades.
        tecnologias: Tecnologias utilizadas.
        atual: Se é o emprego atual.
    """

    id: str = Field(
        ...,
        examples=["exp-001"],
        description="Identificador único",
    )
    cargo: str = Field(
        ...,
        max_length=100,
        examples=["Backend Developer"],
        description="Título do cargo",
    )
    empresa: str = Field(
        ...,
        max_length=100,
        examples=["Tech Company"],
        description="Nome da empresa",
    )
    localizacao: str = Field(
        ...,
        max_length=100,
        examples=["Remoto"],
        description="Localização do trabalho",
    )
    data_inicio: date = Field(
        ...,
        examples=["2023-01-01"],
        description="Data de início (YYYY-MM-DD)",
    )
    data_fim: date | None = Field(
        default=None,
        examples=["2024-06-01"],
        description="Data de término (None se atual)",
    )
    descricao: str = Field(
        ...,
        max_length=1000,
        examples=["Desenvolvimento de APIs REST com FastAPI..."],
        description="Descrição das atividades",
    )
    tecnologias: list[str] = Field(
        ...,
        examples=[["Python", "FastAPI", "PostgreSQL"]],
        description="Tecnologias utilizadas",
    )
    atual: bool = Field(
        default=False,
        description="Se é o emprego atual",
    )


class RespostaExperiencias(BaseModel):
    """
    Resposta da listagem de experiências.

    Attributes:
        experiencias: Lista de experiências ordenadas por data.
        total: Quantidade total de experiências.
    """

    experiencias: list[Experiencia] = Field(
        ...,
        description="Lista de experiências profissionais",
    )
    total: int = Field(
        ...,
        ge=0,
        examples=[2],
        description="Total de experiências",
    )