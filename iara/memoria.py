import json
import os


def caminho_memoria():

    return os.path.join(
        os.path.dirname(__file__),
        "..",
        "dados",
        "memoria.json"
    )


def carregar_memoria():

    caminho = caminho_memoria()

    with open(
        caminho,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)



def salvar_memoria(memoria):

    caminho = caminho_memoria()

    with open(
        caminho,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            memoria,
            arquivo,
            indent=4,
            ensure_ascii=False
        )



def guardar_informacao(categoria, chave, valor):

    memoria = carregar_memoria()


    if categoria not in memoria:
        memoria[categoria] = {}


    memoria[categoria][chave] = valor


    salvar_memoria(memoria)



def buscar_informacao(categoria, chave):

    memoria = carregar_memoria()


    try:
        return memoria[categoria][chave]

    except KeyError:
        return None
