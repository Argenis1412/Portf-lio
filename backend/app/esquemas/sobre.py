"""
Schemas para endpoint /api/sobre.

Define o contrato de resposta com informações pessoais do desenvolvedor.
"""

from pydantic import BaseModel, Field, EmailStr, HttpUrl


class RespostaSobre(BaseModel):
    """
    Informações pessoais para seção "Sobre Mim".

    Attributes:
        nome: Nome completo do desenvolvedor.
        titulo: Título profissional (ex: "Backend Developer | Python").
        localizacao: Cidade e estado.
        email: Email de contato.
        telefone: Telefone de contato.
        github: URL do perfil GitHub.
        linkedin: URL do perfil LinkedIn.
        descricao: Resumo profissional.
        disponibilidade: Disponibilidade para trabalho.
    """

    nome: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["Argenis Lopez"],
        description="Nome completo",
    )
    titulo: str = Field(
        ...,
        max_length=200,
        examples=["Backend Developer | Python | FastAPI"],
        description="Título profissional",
    )
    localizacao: str = Field(
        ...,
        max_length=100,
        examples=["Curitiba, PR"],
        description="Localização atual",
    )
    email: EmailStr = Field(
        ...,
        examples=["argenislopez28708256@gmail.com"],
        description="Email de contato",
    )
    telefone: str = Field(
        ...,
        max_length=20,
        examples=["(41) 9 9510-3364"],
        description="Telefone de contato",
    )
    github: HttpUrl = Field(
        ...,
        examples=["https://github.com/argenis972"],
        description="URL do perfil GitHub",
    )
    linkedin: HttpUrl = Field(
        ...,
        examples=["https://linkedin.com/in/argenis972"],
        description="URL do perfil LinkedIn",
    )
    descricao: str = Field(
        ...,
        max_length=1000,
        examples=["Backend Developer com foco em Python e FastAPI..."],
        description="Resumo profissional",
    )
    disponibilidade: str = Field(
        ...,
        max_length=100,
        examples=["Remoto, híbrido ou presencial"],
        description="Disponibilidade para trabalho",
    )