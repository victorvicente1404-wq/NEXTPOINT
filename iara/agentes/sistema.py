"""
Agente do sistema operacional.
"""

from .base import Agente, registrar


@registrar
class AgenteSistema(Agente):

    nome = "Sistema"

    prioridade = 50

    descricao = "Interage com o sistema operacional."

    def aceita(self, evento):

        return evento.objetivo.tipo in (

            "abrir_programa",

            "executar_comando",

            "abrir_arquivo"

        )

    def executar(self, evento):

        return evento
