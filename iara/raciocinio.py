"""
Sistema de raciocínio.

Recebe os dados interpretados e decide
qual ação será realizada.
"""


def decidir(dados: dict) -> dict:

    intencao = dados["intencao"]

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
