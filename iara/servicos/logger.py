"""
Sistema de logs da Iara.
"""

from pathlib import Path
from datetime import datetime


class Logger:

    def __init__(self, arquivo="data/logs/iara.log"):

        self.arquivo = Path(arquivo)

        self.arquivo.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def _escrever(self, nivel, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        linha = f"[{horario}] [{nivel}] {mensagem}\n"

        with open(self.arquivo, "a", encoding="utf-8") as f:

            f.write(linha)

    def info(self, mensagem):

        self._escrever("INFO", mensagem)

    def aviso(self, mensagem):

        self._escrever("AVISO", mensagem)

    def erro(self, mensagem):

        self._escrever("ERRO", mensagem)

    def debug(self, mensagem):

        self._escrever("DEBUG", mensagem)
