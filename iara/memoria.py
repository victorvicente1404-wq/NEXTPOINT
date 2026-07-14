"""
Memória permanente.

Tudo que estiver aqui continua existindo
mesmo depois que a Iara for fechada.
"""

import json
from pathlib import Path


CAMINHO = (
    Path(__file__).parent.parent
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
