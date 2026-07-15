"""
Sistema de memória da Iara.
"""

import json
from pathlib import Path


CAMINHO = (
    Path(__file__).parent.parent.parent
    / "data"
    / "memoria.json"
)


def carregar():

    with open(
        CAMINHO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


def salvar(memoria):

    with open(
        CAMINHO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            memoria,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def aprender(entidades):

    memoria = carregar()

    for entidade in entidades:

        memoria[
            entidade["tipo"]
        ] = entidade["valor"]

    salvar(memoria)


def consultar(chave):

    memoria = carregar()

    return memoria.get(chave)


def esquecer(chave):

    memoria = carregar()

    if chave in memoria:

        del memoria[chave]

        salvar(memoria)
        json.dump(
            memoria,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def aprender(entidades):

    memoria = carregar()

    for entidade in entidades:

        if entidade["tipo"] == "nome":

            memoria["usuario"]["nome"] = entidade["valor"]

        elif entidade["tipo"] == "idade":

            memoria["usuario"]["idade"] = entidade["valor"]

    salvar(memoria)

    return memoria
