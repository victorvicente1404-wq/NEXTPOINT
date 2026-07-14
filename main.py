from iara import NOME_PROJETO, VERSAO_PROJETO
from iara.cerebro import iniciar
from iara.chat import conversar

print(f"Iniciando {NOME_PROJETO}...")
print(f"Versão {VERSAO_PROJETO}")

iniciar()

conversar()
