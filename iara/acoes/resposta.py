"""
Ações de resposta.
"""

from .base import registrar


@registrar("confirmar_aprendizado")
def confirmar(evento, passo):

    evento.objetivo.resultado = "aprendido"


@registrar("responder_nome")
def responder_nome(evento, passo):

    pass


@registrar("responder_idade")
def responder_idade(evento, passo):

    pass


@registrar("responder_padrao")
def responder_padrao(evento, passo):

    pass
