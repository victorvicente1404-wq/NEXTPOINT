"""
Contexto da conversa.
"""


class Contexto:

    def __init__(self):

        self.assunto = ""

        self.topicos = []

    def atualizar(self, texto):

        self.assunto = texto
