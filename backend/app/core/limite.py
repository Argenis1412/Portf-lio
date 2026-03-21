"""
Configuração do Rate Limiter para a aplicação.
"""

from fastapi import Request
from slowapi import Limiter
from slowapi.util import get_remote_address


def get_email_or_ip_key(request: Request) -> str:
    """
    Recupera a identidade (e-mail) já extraída pelo middleware no request.state.
    Caso não exista, retorna o IP remoto.
    Esta função é síncrona para compatibilidade total com o Limiter.
    """
    # A identidade é populada pelo MiddlewareRequisicao para POST /api/v1/contato
    identidade = getattr(request.state, "identidade", None)
    if identidade:
        return identidade
    
    return get_remote_address(request)


# Inicializar limiter baseado no IP do cliente por padrão
limiter = Limiter(key_func=get_remote_address)
