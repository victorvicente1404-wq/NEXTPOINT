"""
Executor da Iara.
"""

from ..acoes.base import executar

from ..acoes import memoria
from ..acoes import resposta

from ..agentes.base import encontrar

from ..agentes import memoria as agente_memoria
from ..agentes import sistema as agente_sistema


def executar_plano(evento):

    agente = encontrar(evento)

    if agente:

        agente.executar(evento)

    for passo in evento.objetivo.plano:

        executar(

            passo["acao"],

            evento,

            passo

        )

    return evento
