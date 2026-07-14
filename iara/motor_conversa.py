"""
Motor principal da conversa.
"""

from .interpretador import interpretar
from .contexto import atualizar, obter
from .memoria import carregar, aprender
from .raciocinio import decidir
from .respostas import responder
from .acoes import executar


def conversar(mensagem):

    dados = interpretar(mensagem)

    if dados["entidades"]:
        aprender(dados["entidades"])

    contexto = obter()

    memoria = carregar()

    decisao = decidir(
        dados,
        contexto,
        memoria
    )

    executar(decisao)

    resposta = responder(decisao)

    atualizar(
        mensagem,
        dados["intencao"],
        resposta
    )

    return resposta
