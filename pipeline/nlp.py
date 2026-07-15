"""
Sistema de NLP (Processamento de Linguagem Natural).

Responsável por normalizar a entrada do usuário.
"""

import re
import unicodedata


def remover_acentos(texto: str) -> str:
    texto = unicodedata.normalize("NFD", texto)

    return "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


def limpar_texto(texto: str) -> str:

    texto = texto.lower()

    texto = remover_acentos(texto)

    texto = re.sub(r"[^\w\s]", "", texto)

    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()
