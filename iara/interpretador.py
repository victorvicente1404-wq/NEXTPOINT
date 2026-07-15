"""
Interpretador da Iara.

Responsável por entender a mensagem.
"""

from .nlp import limpar_texto
from .extrator import extrair


def interpretar(mensagem: str):

    texto = limpar_texto(mensagem)

    entidades = extrair(texto)

    cumprimentos = {
        "oi",
        "ola",
        "eae",
        "opa",
        "fala",
        "bom dia",
        "boa tarde",
        "boa noite"
    }

    despedidas = {
        "tchau",
        "falou",
        "ate mais",
        "ate logo"
    }

    if texto in cumprimentos:
        intencao = "cumprimento"

    elif texto in despedidas:
        intencao = "despedida"

    elif texto in (
        "qual e meu nome",
        "qual meu nome",
        "como eu me chamo"
    ):
        intencao = "consultar_nome"

    else:
        intencao = "desconhecido"

    return {
        "mensagem": mensagem,
        "texto": texto,
        "intencao": intencao,
        "confianca": 1.0,
        "entidades": entidades
    }
