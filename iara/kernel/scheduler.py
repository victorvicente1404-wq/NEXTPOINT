"""
Escalonador da Iara.
"""


class Scheduler:

    def __init__(self):

        self.fila = []

    def adicionar(self, tarefa):

        self.fila.append(tarefa)

    def executar(self):

        while self.fila:

            tarefa = self.fila.pop(0)

            tarefa.executar()
