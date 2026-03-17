"""
Testes dos controladores (endpoints HTTP).

Testa integração entre rotas FastAPI e casos de uso.
"""

import pytest
from unittest.mock import AsyncMock
from fastapi.testclient import TestClient

from app.principal import app
from app.controladores.dependencias import obter_enviar_contato_use_case

client = TestClient(app)


def test_saude_retorna_ok():
    """Testa endpoint GET /saude retorna status ok."""
    response = client.get("/saude")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "mensagem" in data


def test_obter_sobre_retorna_200():
    """Testa endpoint GET /api/v1/sobre retorna 200."""
    response = client.get("/api/v1/sobre")
    
    assert response.status_code == 200
    data = response.json()
    assert "nome" in data
    assert "email" in data
    assert "descricao" in data


def test_listar_projetos_retorna_200():
    """Testa endpoint GET /api/v1/projetos retorna lista."""
    response = client.get("/api/v1/projetos")
    
    assert response.status_code == 200
    data = response.json()
    assert "projetos" in data
    assert "total" in data
    assert isinstance(data["projetos"], list)


def test_obter_projeto_existente_retorna_200():
    """Testa GET /api/v1/projetos/{id} com projeto existente."""
    response = client.get("/api/v1/projetos/portfolio-api")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "portfolio-api"
    assert "nome" in data
    assert "tecnologias" in data


def test_obter_projeto_inexistente_retorna_404():
    """Testa GET /api/v1/projetos/{id} com projeto inexistente."""
    response = client.get("/api/v1/projetos/projeto-inexistente")
    
    assert response.status_code == 404
    data = response.json()
    assert "erro" in data
    assert data["erro"]["codigo"] == "PROJETO_NAO_ENCONTRADO"
    assert "mensagem" in data["erro"]


def test_obter_stack_retorna_200():
    """Testa endpoint GET /api/v1/stack retorna tecnologias."""
    response = client.get("/api/v1/stack")
    
    assert response.status_code == 200
    data = response.json()
    assert "stack" in data
    assert "por_categoria" in data
    assert isinstance(data["stack"], list)


def test_listar_experiencias_retorna_200():
    """Testa endpoint GET /api/v1/experiencias retorna lista."""
    response = client.get("/api/v1/experiencias")
    
    assert response.status_code == 200
    data = response.json()
    assert "experiencias" in data
    assert "total" in data
    assert isinstance(data["experiencias"], list)


def test_listar_formacao_retorna_200():
    """Testa endpoint GET /api/v1/formacao retorna lista."""
    response = client.get("/api/v1/formacao")

    assert response.status_code == 200
    data = response.json()
    assert "formacoes" in data
    assert "total" in data
    assert isinstance(data["formacoes"], list)


def test_enviar_contato_com_dados_validos_retorna_200():
    """Testa POST /api/contato com dados válidos usando Mock.
    """
    payload = {
        "nome": "Maria Silva",
        "email": "maria@example.com",
        "assunto": "Teste",
        "mensagem": "Esta é uma mensagem de teste com mais de 10 caracteres.",
    }
    
    mock_uc = AsyncMock()
    mock_uc.executar.return_value = True

    app.dependency_overrides[obter_enviar_contato_use_case] = lambda: mock_uc
    try:
        response = client.post("/api/v1/contato", json=payload)
    finally:
        app.dependency_overrides.pop(obter_enviar_contato_use_case, None)
    
    assert response.status_code == 200
    data = response.json()
    assert data["sucesso"] is True
    assert "mensagem" in data
    mock_uc.executar.assert_awaited_once()


def test_enviar_contato_com_dados_invalidos_retorna_422():
    """Testa POST /api/contato com dados inválidos."""
    payload = {
        "nome": "M",  # Muito curto
        "email": "email-invalido",
        "assunto": "Abc",  # Muito curto
        "mensagem": "123",  # Muito curta (agora o limite é 5)
    }
    
    response = client.post("/api/v1/contato", json=payload)
    
    assert response.status_code == 422
    data = response.json()
    assert "erro" in data
    assert data["erro"]["codigo"] == "ERRO_VALIDACAO_ENTRADA"
    assert "detalhes" in data["erro"]  # Lista de erros de validação
