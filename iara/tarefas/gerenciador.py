"""
Gerenciador de tarefas.
"""

from ..modelos.tarefa import Tarefa


class GerenciadorTarefas:

    def __init__(self):

        self.fila = []

    def adicionar(self, tarefa):

        self.fila.append(tarefa)

    def proxima(self):

        if not self.fila:

            return None

        return self.fila.pop(0)
