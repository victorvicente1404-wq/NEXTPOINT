import json

ARQUIVO = "data/usuario.json"

def salvar_interesse(interesse):

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    if interesse not in dados["interesses"]:
        dados["interesses"].append(interesse)

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
