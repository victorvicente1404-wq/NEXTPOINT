from .interpretador import identificar_intencao
from .respostas import responder


def conversar(mensagem):

    intencao = identificar_intencao(mensagem)

    resposta = responder(intencao)

    return resposta
