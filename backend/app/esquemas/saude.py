"""
Schemas Pydantic para endpoint de saúde.

Define contratos de entrada/saída para validação automática.
"""

from pydantic import BaseModel, Field


class RespostaSaude(BaseModel):
    """
    Schema de resposta do health check.

    Attributes:
        status: Status da API ("ok" ou "erro").
        mensagem: Descrição legível do status.
    """

    status: str = Field(
        ...,
        examples=["ok"],
        description="Status da API",
    )
    mensagem: str = Field(
        ...,
        examples=["API funcionando normalmente"],
        description="Mensagem descritiva do status",
    )