"""
Cérebro principal da Iara.
"""

from .estado import EstadoIA
from .contexto import Contexto
from .memoria_trabalho import MemoriaTrabalho


class Cerebro:

    def __init__(self):

        self.estado = EstadoIA()

        self.contexto = Contexto()

        self.memoria = MemoriaTrabalho()

    def iniciar_pensamento(self):

        self.estado.pensando = True

    def finalizar_pensamento(self):

        self.estado.pensando = False

    def registrar_conversa(self, usuario, resposta):

        self.memoria.adicionar(

            usuario,

            resposta

        )

        self.estado.ultima_resposta = resposta

        self.contexto.atualizar(usuario)
