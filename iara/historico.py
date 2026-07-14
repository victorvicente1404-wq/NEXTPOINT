import json

ARQUIVO = "data/historico.json"


def salvar(pergunta, resposta):

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    dados["conversas"].append({
        "usuario": pergunta,
        "iara": resposta
    })

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
