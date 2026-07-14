def responder(frase):

    texto = frase.lower()

    if "oi" in texto or "olá" in texto:
        return "Oi! 😊 Como você está?"

    elif "tudo bem" in texto:
        return "Estou bem! E você?"

    elif "qual seu nome" in texto:
        return "Meu nome é Iara."

    elif "quem criou você" in texto:
        return "Fui criada pelo Black através do projeto NextPoint."

    else:
        return "Ainda não sei responder isso, mas vou aprender."
