import pytest
import hashlib
import time
from app.core.idempotencia import ContentStore

def test_content_store_duplicate_detection():
    """Valida que o ContentStore detecta duplicados ignorando o tempo se menor que o TTL."""
    store = ContentStore(ttl_seconds=300)
    msg_hash = hashlib.sha256(b"user@example.com:hello").hexdigest()
    
    # 1. Não deve ser duplicado na primeira vez
    assert store.check_duplicate(msg_hash) is False
    
    # 2. Adicionar hash
    store.add(msg_hash)
    
    # 3. Agora deve ser duplicado
    assert store.check_duplicate(msg_hash) is True
    
    # 4. Outro hash não deve ser duplicado
    other_hash = hashlib.sha256(b"user@example.com:other").hexdigest()
    assert store.check_duplicate(other_hash) is False

def test_content_store_ttl_expiration():
    """Valida que o ContentStore limpa hashes expirados."""
    store = ContentStore(ttl_seconds=0.1) # TTL muito curto
    msg_hash = hashlib.sha256(b"test:expire").hexdigest()
    
    store.add(msg_hash)
    assert store.check_duplicate(msg_hash) is True
    
    time.sleep(0.2) # Dormir mais que o TTL
    assert store.check_duplicate(msg_hash) is False

def test_endpoint_duplicate_repro(client):
    """
    Simula o comportamento do endpoint para múltiplas chamadas com mesmo conteúdo.
    """
    from app.core.idempotencia import content_store
    # Limpar qualquer estado anterior para este teste
    content_store._cache.clear()
    
    email = "dupe@example.com"
    content = "This belongs to a duplicate test."
    payload = {
        "nome": "Dupe User",
        "email": email,
        "assunto": "Subject A",
        "mensagem": content
    }
    
    # 1. Primeira requisição (Sucesso)
    resp1 = client.post("/api/v1/contato", json=payload)
    assert resp1.status_code == 200
    
    # 2. Segunda requisição com MESMO conteúdo mas assunto diferente (Deve ser bloqueado)
    payload_diff_subject = payload.copy()
    payload_diff_subject["assunto"] = "Subject B (Changed)"
    resp2 = client.post("/api/v1/contato", json=payload_diff_subject)
    
    assert resp2.status_code == 400
    assert resp2.json()["erro"]["codigo"] == "CONTEUDO_DUPLICADO"

def test_endpoint_rate_limit_manual_repro(client):
    """
    Verifica que o rate limit manual não bloqueia duplicatas de contar.
    """
    from app.core.idempotencia import content_store
    content_store._cache.clear()
    
    email = "limit@example.com"
    payload = {
        "nome": "Limit User",
        "email": email,
        "mensagem": "Fresh message 1"
    }
    
    # 1. Enviar normal (OK)
    resp1 = client.post("/api/v1/contato", json=payload)
    assert resp1.status_code == 200
    
    # 2. Enviar duplicado (Deve ser 400)
    resp2 = client.post("/api/v1/contato", json=payload)
    assert resp2.status_code == 400
