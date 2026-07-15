"""
Executor da Iara.
"""

from ..acoes.base import executar

# Importa as ações para registrá-las
from ..acoes import memoria
from ..acoes import resposta


def executar_plano(evento):

    for passo in evento.objetivo.plano:

        executar(

            passo["acao"],

            evento,

            passo

        )

    return evento
