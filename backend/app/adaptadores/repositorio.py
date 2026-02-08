"""
Adaptador para repositório de dados do portfólio.

Interface abstrata + implementação com arquivos JSON.
"""

from abc import ABC, abstractmethod
import json
from pathlib import Path
from datetime import date

from app.entidades.projeto import Projeto
from app.entidades.experiencia import ExperienciaProfissional


class RepositorioPortfolio(ABC):
    """
    Interface abstrata para acesso aos dados do portfólio.

    Permite trocar implementação facilmente (JSON → Database → API).
    """

    @abstractmethod
    def obter_sobre(self) -> dict:
        """Retorna informações da seção Sobre."""
        pass

    @abstractmethod
    def obter_projetos(self) -> list[Projeto]:
        """Retorna lista de projetos."""
        pass

    @abstractmethod
    def obter_projeto_por_id(self, projeto_id: str) -> Projeto | None:
        """Retorna um projeto específico ou None se não encontrado."""
        pass

    @abstractmethod
    def obter_stack(self) -> list[dict]:
        """Retorna lista de tecnologias do stack."""
        pass

    @abstractmethod
    def obter_experiencias(self) -> list[ExperienciaProfissional]:
        """Retorna lista de experiências profissionais."""
        pass


class RepositorioJSON(RepositorioPortfolio):
    """
    Implementação de RepositorioPortfolio usando arquivos JSON.

    Lê dados de arquivos na pasta backend/dados/.

    Attributes:
        diretorio_dados: Caminho para pasta com arquivos JSON.
    """

    def __init__(self, diretorio_dados: str | Path = "dados"):
        """
        Inicializa repositório JSON.

        Args:
            diretorio_dados: Caminho para pasta com dados JSON.
        """
        self.diretorio_dados = Path(diretorio_dados)

    def _ler_json(self, nome_arquivo: str) -> dict | list:
        """
        Lê arquivo JSON do diretório de dados.

        Args:
            nome_arquivo: Nome do arquivo (ex: "sobre.json").

        Returns:
            Conteúdo do JSON parseado.

        Raises:
            FileNotFoundError: Se arquivo não existe.
            json.JSONDecodeError: Se JSON é inválido.
        """
        caminho = self.diretorio_dados / nome_arquivo
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    def obter_sobre(self) -> dict:
        """
        Obtém informações da seção Sobre.

        Returns:
            dict: Dados do arquivo sobre.json.
        """
        return self._ler_json("sobre.json")

    def obter_projetos(self) -> list[Projeto]:
        """
        Obtém lista de projetos.

        Returns:
            list[Projeto]: Lista de entidades Projeto.
        """
        dados = self._ler_json("projetos.json")
        return [
            Projeto(
                id=p["id"],
                nome=p["nome"],
                descricao_curta=p["descricao_curta"],
                descricao_completa=p["descricao_completa"],
                tecnologias=p["tecnologias"],
                funcionalidades=p["funcionalidades"],
                aprendizados=p["aprendizados"],
                repositorio=p.get("repositorio"),
                demo=p.get("demo"),
                destaque=p.get("destaque", False),
            )
            for p in dados
        ]

    def obter_projeto_por_id(self, projeto_id: str) -> Projeto | None:
        """
        Obtém projeto específico por ID.

        Args:
            projeto_id: ID do projeto a buscar.

        Returns:
            Projeto | None: Projeto encontrado ou None.
        """
        projetos = self.obter_projetos()
        for projeto in projetos:
            if projeto.id == projeto_id:
                return projeto
        return None

    def obter_stack(self) -> list[dict]:
        """
        Obtém lista de tecnologias do stack.

        Returns:
            list[dict]: Lista de tecnologias.
        """
        return self._ler_json("stack.json")

    def obter_experiencias(self) -> list[ExperienciaProfissional]:
        """
        Obtém lista de experiências profissionais.

        Returns:
            list[ExperienciaProfissional]: Lista de entidades ExperienciaProfissional.
        """
        dados = self._ler_json("experiencias.json")
        return [
            ExperienciaProfissional(
                id=e["id"],
                cargo=e["cargo"],
                empresa=e["empresa"],
                localizacao=e["localizacao"],
                data_inicio=date.fromisoformat(e["data_inicio"]),
                data_fim=date.fromisoformat(e["data_fim"]) if e.get("data_fim") else None,
                descricao=e["descricao"],
                tecnologias=e["tecnologias"],
                atual=e.get("atual", False),
            )
            for e in dados
        ]
