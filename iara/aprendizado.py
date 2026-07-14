import json

ARQUIVO = "data/conhecimento.json"

def aprender(categoria, informacao):

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    if categoria not in dados:
        dados[categoria] = []

    if informacao not in dados[categoria]:
        dados[categoria].append(informacao)

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
