"""
Sistema de respostas da Iara.

Responsável por carregar as respostas
e escolher uma resposta adequada.
"""

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


def responder(decisao: dict) -> str:

    tipo = decisao["tipo"]

    if tipo not in RESPOSTAS:
        tipo = "desconhecido"

    return random.choice(
        RESPOSTAS[tipo]
    )
