def decidir(intencao, contexto, memoria):

    mapa = {
        "cumprimento": {
            "acao": "responder",
            "tipo": "cumprimento"
        },

        "despedida": {
            "acao": "responder",
            "tipo": "despedida"
        }
    }

    return mapa.get(
        intencao,
        {
            "acao": "responder",
            "tipo": "desconhecido"
        }
    )
