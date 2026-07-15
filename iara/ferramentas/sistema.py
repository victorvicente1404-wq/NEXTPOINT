"""
Ferramentas relacionadas ao sistema operacional.
"""

import os

from .base import (
    Ferramenta,
    registrar
)


@registrar
class AbrirPrograma(Ferramenta):

    nome = "abrir_programa"

    descricao = (
        "Abre programas instalados."
    )


    def executar(self, parametros):

        programa = parametros.get(
            "programa"
        )

        if not programa:

            return "Programa não informado."


        try:

            os.startfile(programa)

            return (
                f"Abrindo {programa}"
            )

        except Exception as erro:

            return (
                f"Erro ao abrir: {erro}"
            )
