"""
Memória temporária da conversa.
"""


class MemoriaTrabalho:

    def __init__(self):

        self.historico = []

    def adicionar(self, usuario, iara):

        self.historico.append({

            "usuario": usuario,

            "iara": iara

        })

        if len(self.historico) > 20:

            self.historico.pop(0)

    def obter(self):

        return self.historico
