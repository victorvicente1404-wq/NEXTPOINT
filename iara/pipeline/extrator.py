"""
Extrator de entidades.
"""

import re


def extrair_entidades(texto):

    entidades = []

    texto_lower = texto.lower()

    # Nome
    nome = re.search(

        r"meu nome é\s+([a-zA-ZÀ-ÿ]+)",

        texto_lower

    )

    if nome:

        entidades.append({

            "tipo": "nome",

            "valor": nome.group(1).title()

        })

    # Idade
    idade = re.search(

        r"(\d+)\s*anos",

        texto_lower

    )

    if idade:

        entidades.append({

            "tipo": "idade",

            "valor": idade.group(1)

        })

    return entidades    if padrao_idade:

        dados.append(
            {
                "tipo": "idade",
                "valor": int(
                    padrao_idade.group(1)
                )
            }
        )

    return dados
