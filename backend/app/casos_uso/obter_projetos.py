"""
Casos de uso: Obter projetos.

Lógica pura, sem dependência de FastAPI.
"""

from app.adaptadores.repositorio import RepositorioPortfolio
from app.entidades.projeto import Projeto


class ObterProjetosUseCase:
    """
    Caso de uso para listar projetos.

    Responsabilidade:
        - Buscar projetos no repositório
        - Ordenar (destacados primeiro, depois alfabético)
        - Retornar lista de projetos

    Attributes:
        repositorio: Repositório de dados do portfólio.
    """

    def __init__(self, repositorio: RepositorioPortfolio):
        """
        Inicializa caso de uso.

        Args:
            repositorio: Implementação de RepositorioPortfolio.
        """
        self.repositorio = repositorio

    def executar(self) -> list[Projeto]:
        """
        Executa caso de uso.

        Returns:
            list[Projeto]: Lista de projetos ordenada (destacados primeiro).

        Ordenação:
            1. Projetos em destaque vêm primeiro
            2. Dentro de cada grupo, ordem alfabética por nome

        Example:
            >>> repo = RepositorioJSON()
            >>> uc = ObterProjetosUseCase(repo)
            >>> projetos = uc.executar()
            >>> projetos[0].destaque
            True
        """
        projetos = self.repositorio.obter_projetos()
        return sorted(projetos, key=lambda p: (not p.destaque, p.nome))


class ObterProjetoPorIdUseCase:
    """
    Caso de uso para obter detalhes de um projeto específico.

    Responsabilidade:
        - Buscar projeto por ID no repositório
        - Retornar projeto ou None se não encontrado

    Attributes:
        repositorio: Repositório de dados do portfólio.
    """

    def __init__(self, repositorio: RepositorioPortfolio):
        """
        Inicializa caso de uso.

        Args:
            repositorio: Implementação de RepositorioPortfolio.
        """
        self.repositorio = repositorio

    def executar(self, projeto_id: str) -> Projeto | None:
        """
        Executa caso de uso.

        Args:
            projeto_id: ID do projeto a buscar.

        Returns:
            Projeto | None: Projeto encontrado ou None.

        Example:
            >>> repo = RepositorioJSON()
            >>> uc = ObterProjetoPorIdUseCase(repo)
            >>> projeto = uc.executar("portfolio-api")
            >>> projeto.nome if projeto else None
            'Portfolio API'
        """
        return self.repositorio.obter_projeto_por_id(projeto_id)
