import json
import random
from pathlib import Path


CAMINHO_RESPOSTAS = (
    Path(__file__).parent.parent
    / "data"
    / "respostas.json"
)


def carregar_respostas():

    with open(
        CAMINHO_RESPOSTAS,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


RESPOSTAS = carregar_respostas()


def identificar_intencao(mensagem):

    texto = mensagem.lower().strip()


    cumprimentos = [
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite"
    ]

    despedidas = [
        "tchau",
        "até mais",
        "ate mais",
        "falou"
    ]


    if texto in cumprimentos:
        return "cumprimento"

    if texto in despedidas:
        return "despedida"

    return "desconhecido"



def conversar(mensagem):

    intencao = identificar_intencao(mensagem)

    return random.choice(
        RESPOSTAS[intencao]
    )
