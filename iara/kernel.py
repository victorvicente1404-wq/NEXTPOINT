"""
Kernel da Iara.

Coordena todo o funcionamento da IA.
"""

from .evento import Evento
from .interpretador import interpretar
from .memoria import carregar, aprender
from .contexto import obter, atualizar
from .raciocinio import decidir
from .planejador import planejar
from .executor import executar_plano
from .respostas import responder


class Kernel:

    def __init__(self):

        self.memoria = carregar()

        self.contexto = obter()

    def processar(self, mensagem):

        evento = Evento(mensagem)

        interpretar(evento)

        if evento.entidades:
            aprender(evento.entidades)
            self.memoria = carregar()

        evento.memoria = self.memoria
        evento.contexto = self.contexto

        decidir(evento)

        planejar(evento.objetivo)

        executar_plano(evento)

        evento.resposta = responder(evento.decisao)

        atualizar(
            evento.mensagem,
            evento.intencao,
            evento.resposta
        )

        self.contexto = obter()

        return evento.resposta
