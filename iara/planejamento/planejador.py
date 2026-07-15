"""
Planejador da Iara.

Transforma um objetivo em um plano de execução.
"""


def planejar(evento):

    objetivo = evento.objetivo

    objetivo.plano = []

    # -------------------------
    # Consultar nome
    # -------------------------

    if objetivo.tipo == "consultar_nome":

        objetivo.plano.extend([

            {
                "acao": "ler_memoria",
                "chave": "nome"
            },

            {
                "acao": "responder_nome"
            }

        ])

        return evento

    # -------------------------
    # Consultar idade
    # -------------------------

    if objetivo.tipo == "consultar_idade":

        objetivo.plano.extend([

            {
                "acao": "ler_memoria",
                "chave": "idade"
            },

            {
                "acao": "responder_idade"
            }

        ])

        return evento

    # -------------------------
    # Aprender

    if objetivo.tipo == "aprender":

        objetivo.plano.extend([

            {
                "acao": "salvar_memoria"
            },

            {
                "acao": "confirmar_aprendizado"
            }

        ])

        return evento

    # -------------------------
    # Conversa

    objetivo.plano.append(

        {
            "acao": "responder_padrao"
        }

    )

    return evento                "acao": "salvar_memoria"
            }

        )

        objetivo.plano.append(

            {
                "acao": "confirmar"
            }

        )

        return objetivo

    return objetivo

