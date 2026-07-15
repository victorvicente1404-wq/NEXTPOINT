"""
Gerencia as configurações da Iara.
"""

import json
from pathlib import Path


class Configuracao:

    def __init__(self):

        self.caminho = Path("data/config.json")

        self.caminho.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.caminho.exists():

            self.salvar({})

    def carregar(self):

        with open(self.caminho, "r", encoding="utf-8") as f:

            return json.load(f)

    def salvar(self, dados):

        with open(self.caminho, "w", encoding="utf-8") as f:

            json.dump(
                dados,
                f,
                indent=4,
                ensure_ascii=False
            )

    def obter(self, chave, padrao=None):

        dados = self.carregar()

        return dados.get(chave, padrao)

    def definir(self, chave, valor):

        dados = self.carregar()

        dados[chave] = valor

        self.salvar(dados)
