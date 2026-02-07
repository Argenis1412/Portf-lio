"""
Adaptador para envio de emails.

Interface abstrata + implementação com Formspree.
"""

from abc import ABC, abstractmethod
import httpx
from app.entidades.mensagem import Mensagem


class EmailAdaptador(ABC):
    """
    Interface abstrata para envio de emails.

    Permite trocar implementação facilmente (Formspree → SendGrid → SES).
    """

    @abstractmethod
    async def enviar_mensagem(self, mensagem: Mensagem) -> bool:
        """
        Envia uma mensagem por email.

        Args:
            mensagem: Mensagem a ser enviada.

        Returns:
            bool: True se enviado com sucesso, False caso contrário.
        """
        pass


class FormspreeEmailAdaptador(EmailAdaptador):
    """
    Implementação de EmailAdaptador usando Formspree.

    Formspree é um serviço gratuito que aceita formulários via POST
    e envia para um email configurado.

    Attributes:
        url_endpoint: URL completa do endpoint Formspree.
    """

    def __init__(self, formspree_url: str, form_id: str):
        """
        Inicializa o adaptador Formspree.

        Args:
            formspree_url: URL base do Formspree (ex: "https://formspree.io/f").
            form_id: ID do formulário Formspree.
        """
        self.url_endpoint = f"{formspree_url}/{form_id}"

    async def enviar_mensagem(self, mensagem: Mensagem) -> bool:
        """
        Envia mensagem via Formspree.

        Args:
            mensagem: Mensagem a ser enviada.

        Returns:
            bool: True se status 200-299, False caso contrário.

        Raises:
            Não levanta exceções - captura erros e retorna False.
        """
        if not self.url_endpoint or "//" in self.url_endpoint[-2:]:
            # Form ID vazio - retorna False sem tentar
            return False

        try:
            async with httpx.AsyncClient() as cliente:
                resposta = await cliente.post(
                    self.url_endpoint,
                    json={
                        "nome": mensagem.nome,
                        "email": mensagem.email,
                        "assunto": mensagem.assunto,
                        "mensagem": mensagem.mensagem,
                    },
                    timeout=10.0,
                )
                return resposta.status_code in range(200, 300)
        except Exception:
            return False
