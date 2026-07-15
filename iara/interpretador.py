"""
Interpretador da Iara.

Responsável por descobrir a intenção
da mensagem do usuário.
"""

from .nlp import limpar_texto
from .extrator import extrair
from .intencoes import INTENCOES


def interpretar(mensagem: str):

    texto = limpar_texto(mensagem)

    entidades = extrair(texto)

    intencao = "desconhecido"

    for nome_intencao, frases in INTENCOES.items():

        if texto in frases:

            intencao = nome_intencao

            break

    return {

        "mensagem": mensagem,

        "texto": texto,

        "intencao": intencao,

        "confianca": 1.0,

        "entidades": entidades

    }
