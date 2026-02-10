"""
Caso de uso: Enviar mensagem de contato.

Lógica pura com operação assíncrona, sem dependência de FastAPI.
"""

from app.entidades.mensagem import Mensagem
from app.adaptadores.email_adaptador import EmailAdaptador
from app.adaptadores.logger_adaptador import LoggerAdaptador


class EnviarContatoUseCase:
    """
    Caso de uso para enviar mensagem de contato.

    Responsabilidade:
        - Criar entidade Mensagem
        - Enviar via adaptador de email
        - Registrar logs de sucesso/falha
        - Retornar resultado da operação

    Attributes:
        email_adaptador: Adaptador para envio de emails.
        logger: Adaptador para logging.
    """

    def __init__(
        self,
        email_adaptador: EmailAdaptador,
        logger: LoggerAdaptador,
    ):
        """
        Inicializa caso de uso.

        Args:
            email_adaptador: Implementação de EmailAdaptador.
            logger: Implementação de LoggerAdaptador.
        """
        self.email_adaptador = email_adaptador
        self.logger = logger

    async def executar(
        self,
        nome: str,
        email: str,
        assunto: str,
        mensagem: str,
    ) -> bool:
        """
        Executa caso de uso de envio de mensagem.

        Args:
            nome: Nome de quem enviou.
            email: Email para resposta.
            assunto: Assunto da mensagem.
            mensagem: Conteúdo da mensagem.

        Returns:
            bool: True se enviado com sucesso, False caso contrário.

        Example:
            >>> email_adaptador = FormspreeEmailAdaptador(url, form_id)
            >>> logger = LoggerEstruturado()
            >>> uc = EnviarContatoUseCase(email_adaptador, logger)
            >>> sucesso = await uc.executar(
            ...     "Maria",
            ...     "maria@example.com",
            ...     "Teste",
            ...     "Mensagem de teste"
            ... )
        """
        # Criar entidade de domínio
        mensagem_entidade = Mensagem(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem,
        )

        # Tentar enviar
        self.logger.info(
            "Tentando enviar mensagem de contato",
            remetente=nome,
            email=email,
        )

        sucesso = await self.email_adaptador.enviar_mensagem(mensagem_entidade)

        if sucesso:
            self.logger.info(
                "Mensagem de contato enviada com sucesso",
                remetente=nome,
            )
        else:
            self.logger.erro(
                "Falha ao enviar mensagem de contato",
                remetente=nome,
            )

        return sucesso
