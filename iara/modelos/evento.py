"""
Evento da Iara.
Representa uma interação completa entre o usuário e a IA.
"""

from .objetivo import Objetivo


class Evento:

    def __init__(self, mensagem):

        # Entrada
        self.mensagem = mensagem

        # Pipeline
        self.texto = mensagem
        self.intencao = "desconhecido"
        self.entidades = []

        # Estado
        self.contexto = {}
        self.memoria = {}

        # Planejamento
        self.objetivo = Objetivo()

        # Resultado
        self.decisao = {}
        self.resposta = ""
