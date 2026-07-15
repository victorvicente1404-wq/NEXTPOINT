"""
Agente do sistema operacional.
"""

from .base import (
    Agente,
    registrar
)

from ..ferramentas.base import encontrar


@registrar
class AgenteSistema(Agente):

    nome = "Sistema"

    prioridade = 50


    def aceita(self, evento):

        return evento.objetivo.tipo in (

            "abrir_programa",

        )


    def executar(self, evento):

        ferramenta = encontrar(
            "abrir_programa"
        )


        if ferramenta:

            resultado = ferramenta.executar(

                evento.objetivo.parametros

            )

            evento.objetivo.resultado = resultado


        return evento
