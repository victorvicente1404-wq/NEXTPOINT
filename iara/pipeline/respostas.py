"""
Sistema de respostas da Iara.
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


def responder(decisao):

    acao = decisao["acao"]

    # -----------------------------
    # CONSULTAS À MEMÓRIA
    # -----------------------------

    if acao == "consultar_memoria":

        tipo = decisao["tipo"]
        valor = decisao["valor"]

        if tipo == "nome":

            if valor:

                return f"Seu nome é {valor}."

            return "Ainda não sei qual é o seu nome."

        if tipo == "idade":

            if valor:

                return f"Você tem {valor} anos."

            return "Ainda não sei sua idade."

    # -----------------------------
    # CONFIRMAÇÃO DE APRENDIZADO
    # -----------------------------

    if acao == "confirmar_aprendizado":

        tipo = decisao["tipo"]
        valor = decisao["valor"]

        if tipo == "nome":

            return (
                f"Prazer em conhecê-lo, {valor}! "
                "Vou lembrar do seu nome."
            )

        if tipo == "idade":

            return (
                f"Entendi! Vou lembrar que você tem {valor} anos."
            )

        return "Entendi! Vou guardar essa informação."

    # -----------------------------
    # RESPOSTAS PADRÃO
    # -----------------------------

    tipo = decisao["tipo"]

    if tipo not in RESPOSTAS:

        tipo = "desconhecido"

    return random.choice(
        RESPOSTAS[tipo]
    )
