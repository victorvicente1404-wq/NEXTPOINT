from .interpretador import identificar_intencao
from .respostas import responder
from .contexto import atualizar


def conversar(mensagem):

    intencao = identificar_intencao(mensagem)

    resposta = responder(intencao)

    atualizar(
        mensagem,
        intencao,
        resposta
    )

    return resposta
