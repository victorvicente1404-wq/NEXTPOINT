"""
Contexto temporário da conversa.

Tudo aqui é perdido quando o programa fecha.
"""

CONTEXTO = {
    "ultima_mensagem": None,
    "ultima_resposta": None,
    "ultima_intencao": None,
    "assunto": None
}


def atualizar(mensagem, intencao, resposta):

    CONTEXTO["ultima_mensagem"] = mensagem
    CONTEXTO["ultima_intencao"] = intencao
    CONTEXTO["ultima_resposta"] = resposta


def obter():

    return CONTEXTO
