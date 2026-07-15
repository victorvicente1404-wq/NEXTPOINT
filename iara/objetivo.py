"""
Modelo de Objetivo.
"""


class Objetivo:

    def __init__(self):

        self.tipo = ""

        self.parametros = {}

        self.plano = []

        self.resultado = None

        self.estado = "novo"

        self.erro = None

    def iniciar(self):

        self.estado = "executando"

    def concluir(self, resultado=None):

        self.estado = "concluido"

        self.resultado = resultado

    def falhar(self, erro):

        self.estado = "erro"

        self.erro = erro
