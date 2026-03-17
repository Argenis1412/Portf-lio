"""
Configurações compartilhadas de pytest.

Define fixtures reutilizáveis para testes.
"""

import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock

from app.entidades.projeto import Projeto
from app.entidades.experiencia import ExperienciaProfissional
from app.entidades.formacao import FormacaoAcademica
from app.adaptadores.repositorio import RepositorioPortfolio
from app.adaptadores.email_adaptador import EmailAdaptador
from app.adaptadores.logger_adaptador import LoggerAdaptador


@pytest.fixture
def repositorio_mock() -> RepositorioPortfolio:
    """
    Mock de RepositorioPortfolio.

    Returns:
        Mock configurado com dados de exemplo.
    """
    mock = AsyncMock(spec=RepositorioPortfolio)
    
    # Mock obter_sobre
    mock.obter_sobre.return_value = {
        "nome": "Teste Silva",
        "titulo": "Desenvolvedor",
        "localizacao": "São Paulo, SP",
        "email": "teste@example.com",
        "telefone": "(11) 99999-9999",
        "github": "https://github.com/teste",
        "linkedin": "https://linkedin.com/in/teste",
        "descricao": {"pt": "Descrição de teste", "en": "Test description", "es": "Descripción de prueba"},
        "disponibilidade": {"pt": "Remoto", "en": "Remote", "es": "Remoto"},
    }
    
    # Mock obter_projetos
    mock.obter_projetos.return_value = [
        Projeto(
            id="projeto-1",
            nome="Projeto A",
            descricao_curta={"pt": "Projeto em destaque", "en": "Featured project", "es": "Proyecto destacado"},
            descricao_completa={"pt": "Descrição completa A", "en": "Full description A", "es": "Descripción completa A"},
            tecnologias=["Python"],
            funcionalidades=["Feature 1"],
            aprendizados=["Aprendizado 1"],
            repositorio="https://github.com/test/a",
            demo=None,
            destaque=True,
            imagem=None,
        ),
        Projeto(
            id="projeto-2",
            nome="Projeto B",
            descricao_curta={"pt": "Projeto normal", "en": "Normal project", "es": "Proyecto normal"},
            descricao_completa={"pt": "Descrição completa B", "en": "Full description B", "es": "Descripción completa B"},
            tecnologias=["JavaScript"],
            funcionalidades=["Feature 2"],
            aprendizados=["Aprendizado 2"],
            repositorio=None,
            demo=None,
            destaque=False,
            imagem=None,
        ),
    ]
    
    # Mock obter_projeto_por_id
    def obter_por_id(projeto_id: str):
        projetos = {
            "projeto-1": mock.obter_projetos.return_value[0],
            "projeto-2": mock.obter_projetos.return_value[1],
        }
        return projetos.get(projeto_id)
    
    mock.obter_projeto_por_id.side_effect = obter_por_id
    
    # Mock obter_stack
    mock.obter_stack.return_value = [
        {"nome": "Python", "categoria": "backend", "nivel": 4, "icone": "python"},
        {"nome": "React", "categoria": "frontend", "nivel": 3, "icone": "react"},
    ]
    
    # Mock obter_experiencias
    mock.obter_experiencias.return_value = [
        ExperienciaProfissional(
            id="exp-1",
            cargo="Dev Atual",
            empresa="Empresa A",
            localizacao="Remoto",
            data_inicio=date(2023, 1, 1),
            data_fim=None,
            descricao={"pt": "Trabalho atual", "en": "Current job", "es": "Trabajo actual"},
            tecnologias=["Python"],
            atual=True,
        ),
        ExperienciaProfissional(
            id="exp-2",
            cargo="Dev Anterior",
            empresa="Empresa B",
            localizacao="São Paulo",
            data_inicio=date(2022, 1, 1),
            data_fim=date(2022, 12, 31),
            descricao={"pt": "Trabalho anterior", "en": "Previous job", "es": "Trabajo anterior"},
            tecnologias=["Java"],
            atual=False,
        ),
    ]
    
    # Mock obter_formacao
    mock.obter_formacao.return_value = [
        FormacaoAcademica(
            id="edu-001",
            curso={"pt": "Tecnologia em Análise e Desenvolvimento de Sistemas", "en": "Associate's Degree in Systems Analysis", "es": "Tecnólogo en Análisis y Desarrollo"},
            instituicao="UFPR – Universidade Federal do Paraná",
            localizacao="Curitiba, PR",
            data_inicio=date(2026, 2, 1),
            data_fim=date(2029, 3, 6),
            descricao={"pt": "Em curso.", "en": "In progress.", "es": "En curso."},
            atual=True,
        ),
    ]

    return mock


@pytest.fixture
def email_adaptador_mock() -> EmailAdaptador:
    """
    Mock de EmailAdaptador.

    Returns:
        Mock configurado para simular envio de emails.
    """
    mock = AsyncMock(spec=EmailAdaptador)
    mock.enviar_mensagem.return_value = True
    return mock


@pytest.fixture
def logger_mock() -> LoggerAdaptador:
    """
    Mock de LoggerAdaptador.

    Returns:
        Mock configurado para capturar logs.
    """
    mock = MagicMock(spec=LoggerAdaptador)
    return mock
