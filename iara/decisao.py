def decidir(evento):

    if evento == "sistema_iniciado":
        return "observar"

    if evento == "pessoa_detectada":
        return "cumprimentar"

    if evento == "usuario_conhecido":
        return "conversar"

    if evento == "pergunta":
        return "responder"

    return "ignorar"
