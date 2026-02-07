"""
Controladores HTTP (rotas FastAPI).

Responsabilidade:
- Receber requisições HTTP
- Validar entrada via Pydantic
- Delegar para casos de uso
- Retornar respostas HTTP

NÃO deve conter lógica de negócio.
"""

from app.controladores.saude import roteador as roteador_saude
from app.controladores.api import roteador as roteador_api

__all__ = ["roteador_saude", "roteador_api"]