from memoria import (
    guardar_informacao,
    buscar_informacao
)
import json
import random
import os


# =========================
# CARREGAR RESPOSTAS
# =========================

def carregar_respostas():

    caminho = os.path.join(
        os.path.dirname(__file__),
        "..",
        "dados",
        "respostas.json"
    )

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


RESPOSTAS = carregar_respostas()


# =========================
# CONTEXTO DA CONVERSA
# =========================

CONTEXTO = {
    "ultima_pergunta": None,
    "assunto": None,
    "ultima_resposta": None
}


# =========================
# GERADOR DE RESPOSTAS
# =========================

def gerar_resposta(intencao):

    if intencao in RESPOSTAS:
        return random.choice(
            RESPOSTAS[intencao]
        )

    return random.choice(
        RESPOSTAS["desconhecido"]
    )


# =========================
# INTERPRETAÇÃO BÁSICA
# =========================

def identificar_intencao(if "meu nome é" in texto:
    return "salvar_nome"


if "qual meu nome" in texto:
    return "lembrar_nome"):

    texto = texto.lower()


    if any(palavra in texto for palavra in [
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite"
    ]):
        return "cumprimento"


    if any(palavra in texto for palavra in [
        "quem é você",
        "quem e voce",
        "seu nome",
        "o que é você"
    ]):
        return "identidade"


    if any(palavra in texto for palavra in [
        "tudo bem",
        "como está",
        "como esta"
    ]):
        return "como_esta"


    if any(palavra in texto for palavra in [
        "obrigado",
        "valeu",
        "agradeço"
    ]):
        return "agradecimento"


    if any(palavra in texto for palavra in [
        "tchau",
        "até mais",
        "ate mais"
    ]):
        return "despedida"


    return "desconhecido"



# =========================
# MOTOR PRINCIPAL
# =========================

def conversar(mensagem):

    intencao = identificar_intencao(mensagem)

    resposta = gerar_resposta(intencao)


    CONTEXTO["ultima_pergunta"] = mensagem
    CONTEXTO["ultima_resposta"] = resposta


    return resposta
