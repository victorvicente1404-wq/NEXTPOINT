"""
Evento da Iara.
"""

from .objetivo import Objetivo


class Evento:

    def __init__(self, mensagem):

        self.mensagem = mensagem

        self.texto = ""

        self.intencao = "desconhecido"

        self.confianca = 0.0

        self.entidades = []

        self.contexto = {}

        self.memoria = {}

        self.decisao = {}

        self.objetivo = Objetivo()

        self.resposta = ""
