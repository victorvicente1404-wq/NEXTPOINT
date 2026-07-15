"""
Sistema de respostas da Iara.

Responsável por gerar respostas para o usuário.
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

    acao = decisao["acao"]

    if acao == "consultar_memoria":

        tipo = decisao["tipo"]

        valor = decisao["valor"]

        if tipo == "nome":

            if valor:

                return f"Seu nome é {valor}."

            return "Ainda não sei qual é o seu nome."

    tipo = decisao["tipo"]

    if tipo not in RESPOSTAS:

        tipo = "desconhecido"

    return random.choice(
        RESPOSTAS[tipo]
    )
