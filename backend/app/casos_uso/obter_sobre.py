"""
Caso de uso: Obter informações da seção Sobre.

Lógica pura, sem dependência de FastAPI.
"""

from app.adaptadores.repositorio import RepositorioPortfolio


class ObterSobreUseCase:
    """
    Caso de uso para obter informações pessoais.

    Responsabilidade:
        - Buscar dados da seção Sobre no repositório
        - Retornar dados estruturados

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

    def executar(self) -> dict:
        """
        Executa caso de uso.

        Returns:
            dict: Informações pessoais do desenvolvedor.

        Example:
            >>> repo = RepositorioJSON()
            >>> uc = ObterSobreUseCase(repo)
            >>> dados = uc.executar()
            >>> dados["nome"]
            'Argenis Lopez'
        """
        return self.repositorio.obter_sobre()
