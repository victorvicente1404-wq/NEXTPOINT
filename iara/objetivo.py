"""
Representa o objetivo que a Iara deseja alcançar.
"""


class Objetivo:

    def __init__(self):

        self.tipo = None

        self.parametros = {}

        self.prioridade = 1

        self.plano = []

        self.concluido = False

        self.resultado = None
