"""
Sistema de raciocínio da Iara.

Responsável por decidir qual ação tomar
após interpretar a mensagem do usuário.
"""


def decidir(dados_interpretados, contexto, memoria):

    intencao = dados_interpretados["intencao"]

    if intencao == "cumprimento":

        return {
            "acao": "responder",
            "tipo": "cumprimento"
        }

    if intencao == "despedida":

        return {
            "acao": "responder",
            "tipo": "despedida"
        }

    return {
        "acao": "responder",
        "tipo": "desconhecido"
    }
