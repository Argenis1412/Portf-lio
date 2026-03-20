"""
Testes de robustez: Idempotência e Rate Limiting.
"""

import pytest
import time
from unittest.mock import AsyncMock
from fastapi.testclient import TestClient

from app.principal import app
from app.controladores.dependencias import obter_enviar_contato_use_case
from app.core.idempotencia import store

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_idempotency_store():
    """Limpa o store antes de cada teste."""
    store._cache.clear()

def test_idempotencia_contato():
    """Testa se o envio duplicado com mesma chave retorna cache."""
    payload = {
        "nome": "Test User",
        "email": "test@example.com",
        "assunto": "Re: Test",
        "mensagem": "Hello world, this is a long enough message."
    }
    headers = {"Idempotency-Key": "unique-key-123"}
    
    # Mock do Use Case
    mock_uc = AsyncMock()
    mock_uc.executar.return_value = True
    
    app.dependency_overrides[obter_enviar_contato_use_case] = lambda: mock_uc
    
    try:
        # Primeira tentativa
        resp1 = client.post("/api/v1/contato", json=payload, headers=headers)
        assert resp1.status_code == 200
        assert resp1.headers.get("X-Cache-Idempotency") is None
        
        # Segunda tentativa (deve ser cache)
        resp2 = client.post("/api/v1/contato", json=payload, headers=headers)
        assert resp2.status_code == 200
        assert resp2.headers.get("X-Cache-Idempotency") == "HIT"
        assert resp2.json() == resp1.json()
        
        # Verificar que o Use Case só foi chamado UMA vez
        assert mock_uc.executar.call_count == 1
        
    finally:
        app.dependency_overrides.pop(obter_enviar_contato_use_case, None)

def test_rate_limiting_projetos():
    """Testa se o limite de 20/minuto funciona para projetos."""
    # Fazer 20 requisições rápidas (limite é 20/min)
    for _ in range(20):
        resp = client.get("/api/v1/projetos")
        assert resp.status_code == 200
    
    # A 21ª deve falhar
    resp = client.get("/api/v1/projetos")
    assert resp.status_code == 429, f"Expected 429, got {resp.status_code}. Body: {resp.text}"
    data = resp.json()
    assert "erro" in data, f"Key 'erro' not in response: {data}"
    assert "rate limit exceeded" in data["erro"]["mensagem"].lower()

def test_idempotencia_sem_chave_funciona_normalmente():
    """Testa se funciona sem a chave (sem cache)."""
    payload = {
        "nome": "Test User",
        "email": "test@example.com",
        "assunto": "Re: Test",
        "mensagem": "Hello world, this is a long enough message."
    }
    
    mock_uc = AsyncMock()
    mock_uc.executar.return_value = True
    app.dependency_overrides[obter_enviar_contato_use_case] = lambda: mock_uc
    
    try:
        resp1 = client.post("/api/v1/contato", json=payload)
        assert resp1.status_code == 200
        
        resp2 = client.post("/api/v1/contato", json=payload)
        assert resp2.status_code == 200
        
        # Sem chave, deve ter chamado duas vezes
        assert mock_uc.executar.call_count == 2
        
    finally:
        app.dependency_overrides.pop(obter_enviar_contato_use_case, None)
