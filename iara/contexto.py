"""
Contexto da conversa.
"""

CONTEXTO = {

    "ultima_mensagem": None,

    "ultima_intencao": None,

    "ultima_resposta": None
}


def atualizar(

    mensagem,

    intencao,

    resposta

):

    CONTEXTO["ultima_mensagem"] = mensagem

    CONTEXTO["ultima_intencao"] = intencao

    CONTEXTO["ultima_resposta"] = resposta


def obter():

    return CONTEXTO
