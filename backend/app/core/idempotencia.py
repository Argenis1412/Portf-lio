import time
from typing import Any, Dict, Optional
from fastapi import Request, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class IdempotencyRecord(BaseModel):
    """Registro de uma resposta cacheada."""
    status_code: int
    content: Any
    timestamp: float

class IdempotencyStore:
    """
    Armazenamento em memória para chaves de idempotência.
    Simplificado para este portfólio. Em produzir, usar Redis.
    """
    def __init__(self, max_size: int = 100, ttl_seconds: int = 3600):
        self._cache: Dict[str, IdempotencyRecord] = {}
        self.max_size = max_size
        self.ttl_seconds = ttl_seconds

    def get(self, key: str) -> Optional[IdempotencyRecord]:
        """Recupera registro se não expirado."""
        record = self._cache.get(key)
        if not record:
            return None
        
        # Verificar expiração
        if time.time() - record.timestamp > self.ttl_seconds:
            self._cache.pop(key, None)
            return None
            
        return record

    def set(self, key: str, status_code: int, content: Any):
        """Armazena novo registro, limpando se necessário."""
        # Limpeza básica se cache estiver cheio (FIFO simplificado)
        if len(self._cache) >= self.max_size:
            # Remover a entrada mais antiga (primeira chave no dict)
            try:
                oldest_key = next(iter(self._cache))
                self._cache.pop(oldest_key, None)
            except StopIteration:
                pass
            
        self._cache[key] = IdempotencyRecord(
            status_code=status_code,
            content=content,
            timestamp=time.time()
        )

# Instância global simplificada
store = IdempotencyStore()

class IdempotencyException(Exception):
    """Exceção interna para sinalizar que resposta cacheada deve ser retornada."""
    def __init__(self, record: IdempotencyRecord):
        self.record = record
        super().__init__("Idempotency HIT")

async def verificar_idempotencia(
    request: Request,
    idempotency_key: Optional[str] = Header(None, alias="Idempotency-Key")
):
    """
    Dependency para verificar chave de idempotência.
    """
    if request.method != "POST":
        return None

    if not idempotency_key:
        return None

    record = store.get(idempotency_key)
    if record:
        raise IdempotencyException(record)

    return idempotency_key
