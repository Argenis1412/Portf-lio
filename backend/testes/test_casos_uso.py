"""
Testes dos casos de uso.

Testa lógica de negócio isoladamente, sem dependências de HTTP.
"""

import pytest
from unittest.mock import AsyncMock

from app.casos_uso import (
    ObterSobreUseCase,
    ObterProjetosUseCase,
    ObterProjetoPorIdUseCase,
    ObterStackUseCase,
    ObterExperienciasUseCase,
    EnviarContatoUseCase,
)


def test_obter_sobre_retorna_dados_corretos(repositorio_mock):
    """Testa que ObterSobreUseCase retorna dados do repositório."""
    uc = ObterSobreUseCase(repositorio_mock)
    
    resultado = uc.executar()
    
    assert resultado["nome"] == "Teste Silva"
    assert resultado["email"] == "teste@example.com"
    repositorio_mock.obter_sobre.assert_called_once()


def test_obter_projetos_ordena_por_destaque(repositorio_mock):
    """Testa que projetos destacados aparecem primeiro."""
    uc = ObterProjetosUseCase(repositorio_mock)
    
    projetos = uc.executar()
    
    assert len(projetos) == 2
    assert projetos[0].destaque is True  # Destacado primeiro
    assert projetos[1].destaque is False
    repositorio_mock.obter_projetos.assert_called_once()


def test_obter_projeto_por_id_encontrado(repositorio_mock):
    """Testa busca de projeto existente por ID."""
    uc = ObterProjetoPorIdUseCase(repositorio_mock)
    
    projeto = uc.executar("projeto-1")
    
    assert projeto is not None
    assert projeto.id == "projeto-1"
    assert projeto.nome == "Projeto A"


def test_obter_projeto_por_id_nao_encontrado(repositorio_mock):
    """Testa busca de projeto inexistente retorna None."""
    uc = ObterProjetoPorIdUseCase(repositorio_mock)
    
    projeto = uc.executar("projeto-inexistente")
    
    assert projeto is None


def test_obter_stack_agrupa_por_categoria(repositorio_mock):
    """Testa que stack é agrupado por categoria."""
    uc = ObterStackUseCase(repositorio_mock)
    
    resultado = uc.executar()
    
    assert "backend" in resultado
    assert "frontend" in resultado
    assert len(resultado["backend"]) == 1
    assert resultado["backend"][0]["nome"] == "Python"
    repositorio_mock.obter_stack.assert_called_once()


def test_obter_experiencias_ordena_cronologicamente(repositorio_mock):
    """Testa que experiências são ordenadas (atual primeiro)."""
    uc = ObterExperienciasUseCase(repositorio_mock)
    
    experiencias = uc.executar()
    
    assert len(experiencias) == 2
    assert experiencias[0].atual is True  # Atual primeiro
    assert experiencias[1].atual is False
    repositorio_mock.obter_experiencias.assert_called_once()


@pytest.mark.asyncio
async def test_enviar_contato_sucesso(email_adaptador_mock, logger_mock):
    """Testa envio de mensagem com sucesso."""
    uc = EnviarContatoUseCase(email_adaptador_mock, logger_mock)
    email_adaptador_mock.enviar_mensagem.return_value = True
    
    sucesso = await uc.executar(
        nome="Maria",
        email="maria@example.com",
        assunto="Teste",
        mensagem="Mensagem de teste",
    )
    
    assert sucesso is True
    email_adaptador_mock.enviar_mensagem.assert_called_once()
    logger_mock.info.assert_called()
    

@pytest.mark.asyncio
async def test_enviar_contato_falha(email_adaptador_mock, logger_mock):
    """Testa envio de mensagem com falha."""
    uc = EnviarContatoUseCase(email_adaptador_mock, logger_mock)
    email_adaptador_mock.enviar_mensagem.return_value = False
    
    sucesso = await uc.executar(
        nome="Maria",
        email="maria@example.com",
        assunto="Teste",
        mensagem="Mensagem de teste",
    )
    
    assert sucesso is False
    email_adaptador_mock.enviar_mensagem.assert_called_once()
    logger_mock.erro.assert_called()
