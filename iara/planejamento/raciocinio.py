"""
Sistema de raciocínio da Iara.
"""

from .evento import Evento


def decidir(
    evento: Evento,
    contexto: dict,
    memoria: dict
) -> dict:

    if evento.intencao == "cumprimento":

        return {
            "acao": "responder",
            "tipo": "cumprimento"
        }

    if evento.intencao == "despedida":

        return {
            "acao": "responder",
            "tipo": "despedida"
        }

    if evento.intencao == "consultar_nome":

        nome = memoria["usuario"].get("nome")

        return {
            "acao": "consultar_memoria",
            "tipo": "nome",
            "valor": nome
        }

    if evento.entidades:

        return {
            "acao": "confirmar_aprendizado",
            "tipo": evento.entidades[0]["tipo"],
            "valor": evento.entidades[0]["valor"]
        }

    return {
        "acao": "responder",
        "tipo": "desconhecido"
    }
