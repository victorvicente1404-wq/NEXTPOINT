"""
Interpretador da Iara.

Responsável por analisar a mensagem do usuário
e retornar uma estrutura padronizada.
"""


def interpretar(mensagem: str) -> dict:

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
            "mensagem": mensagem,
            "intencao": "cumprimento",
            "confianca": 1.0,
            "entidades": []
        }

    if texto in despedidas:

        return {
            "mensagem": mensagem,
            "intencao": "despedida",
            "confianca": 1.0,
            "entidades": []
        }

    return {
        "mensagem": mensagem,
        "intencao": "desconhecido",
        "confianca": 0.0,
        "entidades": []
    }
