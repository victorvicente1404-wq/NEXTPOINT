"""
Modelo de Tarefa.
"""


class Tarefa:

    def __init__(self):

        self.id = None

        self.nome = ""

        self.estado = "nova"

        self.progresso = 0

        self.resultado = None

        self.erro = None

        self.passos = []

        self.atual = 0
