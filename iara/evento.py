"""
Evento de processamento da Iara.

Representa uma mensagem durante todo o pipeline.
"""


class Evento:

    def __init__(self, mensagem: str):

        # Entrada original
        self.mensagem = mensagem

        # Texto normalizado
        self.texto = ""

        # Dados de interpretação
        self.intencao = "desconhecido"
        self.confianca = 0.0
        self.entidades = []

        # Estado interno
        self.contexto = {}
        self.memoria = {}

        # Decisão tomada
        self.decisao = {}

        # Resposta final
        self.resposta = ""
