"""
Sistema de raciocínio da Iara.
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

    if intencao == "consultar_nome":

        nome = memoria["usuario"].get("nome")

        return {
            "acao": "consultar_memoria",
            "tipo": "nome",
            "valor": nome
        }

    return {
        "acao": "responder",
        "tipo": "desconhecido"
    }
