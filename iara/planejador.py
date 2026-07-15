"""
Planejador da Iara.

Transforma um objetivo em um plano de execução.
"""


def planejar(objetivo):

    objetivo.plano.clear()

    if objetivo.tipo == "consultar_nome":

        objetivo.plano.append(

            {
                "acao": "consultar_memoria"
            }

        )

        objetivo.plano.append(

            {
                "acao": "responder"
            }

        )

        return objetivo

    if objetivo.tipo == "aprender":

        objetivo.plano.append(

            {
                "acao": "salvar_memoria"
            }

        )

        objetivo.plano.append(

            {
                "acao": "confirmar"
            }

        )

        return objetivo

    return objetivo
