"""
Sistema de raciocínio da Iara.

Recebe tudo que o interpretador descobriu
e decide qual ação tomar.
"""


def decidir(intencao, contexto, memoria):

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
