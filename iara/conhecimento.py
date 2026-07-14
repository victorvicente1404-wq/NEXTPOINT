import json

ARQUIVO = "data/conhecimento.json"

def saber(categoria):

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados.get(categoria, [])
