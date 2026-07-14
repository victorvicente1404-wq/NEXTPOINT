import json
import random
from pathlib import Path


CAMINHO = (
    Path(__file__).parent.parent
    / "data"
    / "respostas.json"
)


def carregar():

    with open(
        CAMINHO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


RESPOSTAS = carregar()


def responder(intencao):

    return random.choice(
        RESPOSTAS[intencao]
    )
