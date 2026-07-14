from iara.contexto import CONTEXTO


def identificar_intencao(texto):

    texto = texto.lower().strip()

    if any(palavra in texto for palavra in ["oi", "olá", "eae", "opa"]):
        return "cumprimento"

    elif "tudo bem" in texto:
        return "como_esta"

    elif "qual seu nome" in texto or "quem é você" in texto:
        return "identidade"

    elif "quem criou você" in texto:
        return "criador"

    elif "obrigado" in texto or "valeu" in texto:
        return "agradecimento"

    elif "bom dia" in texto:
        return "bom_dia"

    elif "boa tarde" in texto:
        return "boa_tarde"

    elif "boa noite" in texto:
        return "boa_noite"

    return "desconhecido"


def detectar_assunto(texto):

    texto = texto.lower()

    if "f1" in texto or "fórmula" in texto:
        return "formula1"

    elif "python" in texto:
        return "python"

    elif "pokemon" in texto:
        return "pokemon"

    elif "ia" in texto or "inteligência artificial" in texto:
        return "inteligencia_artificial"

    return None


def responder(frase):

    CONTEXTO["ultima_pergunta"] = frase

    assunto = detectar_assunto(frase)

    if assunto:
        CONTEXTO["assunto"] = assunto

    intencao = identificar_intencao(frase)

    if intencao == "cumprimento":
        resposta = "Oi! 😊 Como você está?"

    elif intencao == "como_esta":
        resposta = "Estou bem! E você?"

    elif intencao == "identidade":
        resposta = "Meu nome é Iara."

    elif intencao == "criador":
        resposta = "Fui criada pelo Black através do projeto NextPoint."

    elif intencao == "agradecimento":
        resposta = "Disponha! 😄"

    elif intencao == "bom_dia":
        resposta = "Bom dia! Espero que seu dia seja ótimo!"

    elif intencao == "boa_tarde":
        resposta = "Boa tarde! Como posso ajudar?"

    elif intencao == "boa_noite":
        resposta = "Boa noite! Como foi seu dia?"

    else:
        resposta = "Ainda não sei responder isso, mas vou aprender."

    CONTEXTO["ultima_resposta"] = resposta

    return resposta
