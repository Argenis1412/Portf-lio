"""
Configuração do Rate Limiter para a aplicação.
"""

from slowapi import Limiter
from slowapi.util import get_remote_address

# Inicializar limiter baseado no IP do cliente
limiter = Limiter(key_func=get_remote_address)
