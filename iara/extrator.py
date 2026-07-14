"""
Extrator de informações da Iara.

Responsável por identificar dados importantes
na mensagem do usuário.
"""

import re


def extrair(texto: str) -> list:

    dados = []

    # Nome
    padrao_nome = re.search(
        r"meu nome e ([a-zA-ZÀ-ÿ]+)",
        texto
    )

    if padrao_nome:

        dados.append(
            {
                "tipo": "nome",
                "valor": padrao_nome.group(1).capitalize()
            }
        )

    # Idade

    padrao_idade = re.search(
        r"tenho (\d+) anos",
        texto
    )

    if padrao_idade:

        dados.append(
            {
                "tipo": "idade",
                "valor": int(
                    padrao_idade.group(1)
                )
            }
        )

    return dados
