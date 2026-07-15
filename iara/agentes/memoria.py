"""
Agente responsável pela memória.
"""

from .base import Agente, registrar


@registrar
class AgenteMemoria(Agente):

    nome = "Memória"

    prioridade = 100

    descricao = "Consulta e grava informações."

    def aceita(self, evento):

        return evento.objetivo.tipo in (

            "consultar_nome",

            "consultar_idade",

            "aprender"

        )

    def executar(self, evento):

        return evento
