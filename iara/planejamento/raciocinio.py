"""
Raciocínio da Iara.
"""


def decidir(evento):

    texto = evento.texto.lower()

    objetivo = evento.objetivo

    # -----------------------
    # CONSULTAR NOME
    # -----------------------

    if "meu nome" in texto and "qual" in texto:

        objetivo.tipo = "consultar_nome"

        return evento

    # -----------------------
    # CONSULTAR IDADE
    # -----------------------

    if "minha idade" in texto:

        objetivo.tipo = "consultar_idade"

        return evento

    # -----------------------
    # APRENDER
    # -----------------------

    if evento.entidades:

        objetivo.tipo = "aprender"

        objetivo.parametros = {

            "dados": evento.entidades

        }

        return evento

    # -----------------------
    # CONVERSA
    # -----------------------

    objetivo.tipo = "conversar"

    return evento
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
