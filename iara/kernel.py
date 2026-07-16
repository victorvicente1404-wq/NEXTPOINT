"""
Kernel da Iara - Núcleo do sistema
"""

from iara.motor_conversa import conversar
from iara.servicos.logger import Logger


class Kernel:
    def __init__(self):
        self.logger = Logger()
        self.logger.info("Kernel inicializado.")

    def processar(self, mensagem: str) -> str:
        """Processa a mensagem do usuário e retorna a resposta."""
        try:
            from iara.modelos.evento import Evento
            
            evento = Evento(mensagem)
            resposta = conversar(evento)
            return resposta
        except Exception as e:
            self.logger.erro(f"Erro ao processar mensagem: {e}")
            return "Desculpe, tive um problema interno. Pode tentar novamente?"


# Para facilitar importação
__all__ = ["Kernel"]
