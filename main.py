from iara.kernel import Kernel
from iara.config import *

kernel = Kernel()

print("=" * 40)
print(f"{NOME_PROJETO} - {NOME_IA}")
print(f"Versão {VERSAO}")
print("=" * 40)

while True:

    mensagem = input("\nVocê: ")

    if mensagem.lower() in ("sair", "exit", "quit"):

        print("Iara: Até mais!")

        break

    resposta = kernel.processar(mensagem)

    print(f"Iara: {resposta}")
