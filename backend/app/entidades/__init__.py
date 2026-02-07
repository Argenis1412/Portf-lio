"""
Entidades de domínio (modelos de negócio).

Responsabilidade:
- Representar conceitos do domínio
- Conter lógica de negócio pura
- Ser independente de frameworks externos

Entidades são imutáveis (frozen=True) para garantir consistência.
"""

from app.entidades.mensagem import Mensagem
from app.entidades.projeto import Projeto
from app.entidades.experiencia import ExperienciaProfissional

__all__ = [
    "Mensagem",
    "Projeto",
    "ExperienciaProfissional",
]
