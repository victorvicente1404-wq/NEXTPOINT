def identificar_intencao(mensagem):

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
        return "cumprimento"

    if texto in despedidas:
        return "despedida"

    return "desconhecido"
