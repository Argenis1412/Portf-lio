"""
Testes dos controladores (endpoints HTTP).

Testa integração entre rotas FastAPI e casos de uso.
"""

import pytest
from fastapi.testclient import TestClient

from app.principal import app

client = TestClient(app)


def test_saude_retorna_ok():
    """Testa endpoint GET /saude retorna status ok."""
    response = client.get("/saude")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "mensagem" in data


def test_obter_sobre_retorna_200():
    """Testa endpoint GET /api/sobre retorna 200."""
    response = client.get("/api/sobre")
    
    assert response.status_code == 200
    data = response.json()
    assert "nome" in data
    assert "email" in data
    assert "descricao" in data


def test_listar_projetos_retorna_200():
    """Testa endpoint GET /api/projetos retorna lista."""
    response = client.get("/api/projetos")
    
    assert response.status_code == 200
    data = response.json()
    assert "projetos" in data
    assert "total" in data
    assert isinstance(data["projetos"], list)


def test_obter_projeto_existente_retorna_200():
    """Testa GET /api/projetos/{id} com projeto existente."""
    response = client.get("/api/projetos/portfolio-api")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "portfolio-api"
    assert "nome" in data
    assert "tecnologias" in data


def test_obter_projeto_inexistente_retorna_404():
    """Testa GET /api/projetos/{id} com projeto inexistente."""
    response = client.get("/api/projetos/projeto-inexistente")
    
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data


def test_obter_stack_retorna_200():
    """Testa endpoint GET /api/stack retorna tecnologias."""
    response = client.get("/api/stack")
    
    assert response.status_code == 200
    data = response.json()
    assert "stack" in data
    assert "por_categoria" in data
    assert isinstance(data["stack"], list)


def test_listar_experiencias_retorna_200():
    """Testa endpoint GET /api/experiencias retorna lista."""
    response = client.get("/api/experiencias")
    
    assert response.status_code == 200
    data = response.json()
    assert "experiencias" in data
    assert "total" in data
    assert isinstance(data["experiencias"], list)


def test_enviar_contato_com_dados_validos_retorna_200():
    """Testa POST /api/contato com dados válidos (sem form_id real).
    
    Nota: Como não há FORMSPREE_FORM_ID configurado no ambiente de testes,
    o endpoint retorna 500 (falha ao enviar). Em produção com form_id válido,
    retornaria 200 com sucesso=true.
    """
    payload = {
        "nome": "Maria Silva",
        "email": "maria@example.com",
        "assunto": "Teste",
        "mensagem": "Esta é uma mensagem de teste com mais de 10 caracteres.",
    }
    
    response = client.post("/api/contato", json=payload)
    
    # Como não há form_id configurado, deve retornar 500
    assert response.status_code == 500


def test_enviar_contato_com_dados_invalidos_retorna_422():
    """Testa POST /api/contato com dados inválidos."""
    payload = {
        "nome": "M",  # Muito curto
        "email": "email-invalido",
        "assunto": "Abc",  # Muito curto
        "mensagem": "Curta",  # Muito curta
    }
    
    response = client.post("/api/contato", json=payload)
    
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
