"""
Interpretador da Iara.

Responsável por identificar a intenção
da mensagem utilizando padrões.
"""

import re

from .nlp import limpar_texto
from .extrator import extrair
from .padroes import PADROES


def interpretar(mensagem: str):

    texto = limpar_texto(mensagem)

    entidades = extrair(texto)

    intencao = "desconhecido"

    confianca = 0.0

    for nome, lista in PADROES.items():

        for padrao in lista:

            if re.fullmatch(padrao, texto):

                intencao = nome

                confianca = 1.0

                break

        if intencao != "desconhecido":

            break

    return {

        "mensagem": mensagem,

        "texto": texto,

        "intencao": intencao,

        "confianca": confianca,

        "entidades": entidades

    }
