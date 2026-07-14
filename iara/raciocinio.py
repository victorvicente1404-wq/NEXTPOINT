"""
Sistema de raciocínio da Iara.

Responsável por decidir a próxima ação
com base na interpretação, contexto e memória.
"""


def decidir(
    dados: dict,
    contexto: dict,
    memoria: dict
) -> dict:

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
