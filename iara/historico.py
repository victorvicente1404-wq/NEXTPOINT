import json
import os

ARQUIVO = "data/historico.json"

def carregar():

    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar(usuario, resposta):

    historico = carregar()

    historico.append({
        "usuario": usuario,
        "iara": resposta
    })

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, indent=4, ensure_ascii=False)
