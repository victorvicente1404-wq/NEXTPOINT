"""
Interpretador da Iara.

Responsável por descobrir a intenção da mensagem.
"""

from .nlp import limpar_texto


def interpretar(mensagem: str) -> dict:

    texto = limpar_texto(mensagem)

    cumprimentos = {
        "oi",
        "ola",
        "eae",
        "fala",
        "opa",
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

        return {
            "mensagem": mensagem,
            "texto": texto,
            "intencao": "cumprimento",
            "confianca": 1.0,
            "entidades": []
        }

    if texto in despedidas:

        return {
            "mensagem": mensagem,
            "texto": texto,
            "intencao": "despedida",
            "confianca": 1.0,
            "entidades": []
        }

    return {
        "mensagem": mensagem,
        "texto": texto,
        "intencao": "desconhecido",
        "confianca": 0.2,
        "entidades": []
    }
