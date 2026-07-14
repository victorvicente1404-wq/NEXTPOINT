from .interpretador import interpretar

from .contexto import (

    atualizar,

    obter

)

from .memoria import carregar

from .raciocinio import decidir

from .respostas import responder


def conversar(mensagem):

    dados = interpretar(mensagem)

    contexto = obter()

    memoria = carregar()

    decisao = decidir(

        dados,

        contexto,

        memoria

    )

    resposta = responder(decisao)

    atualizar(

        mensagem,

        dados["intencao"],

        resposta

    )

    return resposta
