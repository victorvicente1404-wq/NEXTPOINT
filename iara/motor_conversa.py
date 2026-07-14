def responder(frase):

    intencao = identificar_intencao(frase)

    if intencao == "cumprimento":
        return "Oi! 😊 Como você está?"

    elif intencao == "agradecimento":
        return "Disponha! 😄"

    elif intencao == "criador":
        return "Fui criada pelo Black através do projeto NextPoint."

    elif intencao == "identidade":
        return "Meu nome é Iara."

    else:
        return "Ainda estou aprendendo. Pode me explicar melhor?"
