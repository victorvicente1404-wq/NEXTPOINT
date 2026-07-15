"""
Estado interno da Iara.
"""


class EstadoIA:

    def __init__(self):

        self.ocupada = False

        self.pensando = False

        self.executando = False

        self.ultima_resposta = ""

        self.humor = "neutro"

        self.confianca = 1.0
