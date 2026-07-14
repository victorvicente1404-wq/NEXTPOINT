"""
Interpretador da Iara.

Responsável por descobrir a intenção do usuário.
"""


def interpretar(mensagem):

    texto = mensagem.lower().strip()

    cumprimentos = {
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite"
    }

    despedidas = {
        "tchau",
        "até mais",
        "ate mais",
        "falou"
    }

    if texto in cumprimentos:

        return {
            "intencao": "cumprimento",
            "confianca": 1.0,
            "entidades": []
        }

    if texto in despedidas:

        return {
            "intencao": "despedida",
            "confianca": 1.0,
            "entidades": []
        }

    return {
        "intencao": "desconhecido",
        "confianca": 0.5,
        "entidades": []
    }
