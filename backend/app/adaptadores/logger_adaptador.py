"""
Adaptador para logging.

Interface abstrata + implementação com módulo logging padrão.
"""

from abc import ABC, abstractmethod
import logging
from typing import Any


class LoggerAdaptador(ABC):
    """
    Interface abstrata para logging.

    Permite trocar implementação facilmente (logging → structlog → sentry).
    """

    @abstractmethod
    def info(self, mensagem: str, **kwargs: Any) -> None:
        """Loga mensagem de informação."""
        pass

    @abstractmethod
    def erro(self, mensagem: str, **kwargs: Any) -> None:
        """Loga mensagem de erro."""
        pass

    @abstractmethod
    def aviso(self, mensagem: str, **kwargs: Any) -> None:
        """Loga mensagem de aviso."""
        pass


class LoggerPadrao(LoggerAdaptador):
    """
    Implementação de LoggerAdaptador usando módulo logging padrão.

    Attributes:
        logger: Instância do logger Python padrão.
    """

    def __init__(self, nome: str = "portfolio"):
        """
        Inicializa logger padrão.

        Args:
            nome: Nome do logger (usado para identificação).
        """
        self.logger = logging.getLogger(nome)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def info(self, mensagem: str, **kwargs: Any) -> None:
        """
        Loga mensagem de informação.

        Args:
            mensagem: Mensagem a logar.
            **kwargs: Contexto adicional (convertido em string).
        """
        contexto = " ".join(f"{k}={v}" for k, v in kwargs.items())
        mensagem_completa = f"{mensagem} {contexto}".strip()
        self.logger.info(mensagem_completa)

    def erro(self, mensagem: str, **kwargs: Any) -> None:
        """
        Loga mensagem de erro.

        Args:
            mensagem: Mensagem a logar.
            **kwargs: Contexto adicional (convertido em string).
        """
        contexto = " ".join(f"{k}={v}" for k, v in kwargs.items())
        mensagem_completa = f"{mensagem} {contexto}".strip()
        self.logger.error(mensagem_completa)

    def aviso(self, mensagem: str, **kwargs: Any) -> None:
        """
        Loga mensagem de aviso.

        Args:
            mensagem: Mensagem a logar.
            **kwargs: Contexto adicional (convertido em string).
        """
        contexto = " ".join(f"{k}={v}" for k, v in kwargs.items())
        mensagem_completa = f"{mensagem} {contexto}".strip()
        self.logger.warning(mensagem_completa)
