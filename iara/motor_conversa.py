def responder(frase):

    texto = frase.lower().strip()

    if any(palavra in texto for palavra in ["oi", "olá", "eae", "opa"]):
        return "Oi! 😊 Como você está?"

    elif "tudo bem" in texto:
        return "Estou bem! E você?"

    elif "qual seu nome" in texto or "quem é você" in texto:
        return "Meu nome é Iara."

    elif "quem criou você" in texto:
        return "Fui criada pelo Black através do projeto NextPoint."

    elif "obrigado" in texto or "valeu" in texto:
        return "Disponha! 😄"

    elif "bom dia" in texto:
        return "Bom dia! Espero que seu dia seja ótimo!"

    elif "boa tarde" in texto:
        return "Boa tarde! Como posso ajudar?"

    elif "boa noite" in texto:
        return "Boa noite! Como foi seu dia?"

    else:
        return "Ainda não sei responder isso, mas vou aprender."
