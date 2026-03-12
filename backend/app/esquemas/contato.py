"""
Schemas para endpoint POST /api/contato.

Define contratos de requisição e resposta para envio de mensagens.
"""

from pydantic import BaseModel, Field, EmailStr


class RequisicaoContato(BaseModel):
    """
    Dados do formulário de contato.

    Validações:
        - nome: 2-80 caracteres
        - email: formato válido
        - mensagem: 10-2000 caracteres
    """

    nome: str = Field(
        ...,
        min_length=2,
        max_length=80,
        examples=["Maria Silva"],
        description="Nome de quem está enviando",
    )
    email: EmailStr = Field(
        ...,
        examples=["maria@empresa.com"],
        description="Email para resposta",
    )
    assunto: str = Field(
        ...,
        min_length=5,
        max_length=100,
        examples=["Oportunidade de trabalho"],
        description="Assunto da mensagem",
    )
    mensagem: str = Field(
        ...,
        min_length=10,
        max_length=2000,
        examples=["Olá, vi seu portfólio e gostaria de conversar..."],
        description="Conteúdo da mensagem",
    )


class RespostaContato(BaseModel):
    """
    Resposta após envio de mensagem.

    Attributes:
        sucesso: Se a mensagem foi enviada com sucesso.
        mensagem: Descrição do resultado.
    """

    sucesso: bool = Field(
        ...,
        examples=[True],
        description="Se o envio foi bem-sucedido",
    )
    mensagem: str = Field(
        ...,
        examples=["Mensagem enviada com sucesso!"],
        description="Descrição do resultado",
    )