"""
Serviço de memória da Iara.
"""

from ..pipeline import memoria as memoria_pipeline


class ServicoMemoria:

    def carregar(self):
        return memoria_pipeline.carregar()

    def consultar(self, chave):
        return memoria_pipeline.consultar(chave)

    def aprender(self, entidades):
        memoria_pipeline.aprender(entidades)

    def esquecer(self, chave):
        memoria_pipeline.esquecer(chave)
