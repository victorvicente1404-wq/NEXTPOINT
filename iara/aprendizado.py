import re

from memoria import guardar_informacao


def analisar_aprendizado(texto):

    texto = texto.lower()


    # Eu gosto de X

    padrao_gosto = r"eu gosto de (.+)"

    resultado = re.search(
        padrao_gosto,
        texto
    )


    if resultado:

        valor = resultado.group(1)

        guardar_informacao(
            "preferencias",
            "gostos",
            valor
        )

        return "gosto"


    # Minha cor favorita é X

    padrao_cor = r"minha cor favorita é (.+)"

    resultado = re.search(
        padrao_cor,
        texto
    )


    if resultado:

        valor = resultado.group(1)

        guardar_informacao(
            "preferencias",
            "cor",
            valor
        )

        return "cor"


    # Eu estudo X

    padrao_estudo = r"eu estudo (.+)"

    resultado = re.search(
        padrao_estudo,
        texto
    )


    if resultado:

        valor = resultado.group(1)

        guardar_informacao(
            "usuario",
            "estudo",
            valor
        )

        return "estudo"


    return None
