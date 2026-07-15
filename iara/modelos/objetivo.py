"""
Modelo de Objetivo.
"""


class Objetivo:

    def __init__(self):

        self.tipo = ""

        self.parametros = {}

        self.plano = []

        self.estado = "novo"

        self.resultado = None

        self.erro = None
