"""
Ações relacionadas à memória.
"""

from .base import registrar

from ..pipeline.memoria import (
    aprender,
    consultar
)


@registrar("ler_memoria")
def ler_memoria(evento, passo):

    chave = passo["chave"]

    evento.objetivo.resultado = consultar(chave)


@registrar("salvar_memoria")
def salvar_memoria(evento, passo):

    aprender(

        evento.objetivo.parametros["dados"]

    )
