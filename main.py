"""
Main - NextPoint / Iara
Versão melhorada com inteligência
"""

from iara.kernel import Kernel
from iara.config import *

# Inicializa o Kernel
kernel = Kernel()

print("=" * 50)
print(f"{NOME_PROJETO} - {NOME_IA}")
print(f"Versão {VERSAO} | Modo Parceira Ativada")
print("=" * 50)
print("Digite 'sair' para encerrar.\n")

while True:
    try:
        mensagem = input("Você: ").strip()

        if mensagem.lower() in ("sair", "exit", "quit", "tchau"):
            print("Iara: Até mais! Foi bom conversar com você. 👋")
            break

        if not mensagem:
            continue

        # Processa a mensagem
        resposta = kernel.processar(mensagem)
        print(f"Iara: {resposta}\n")

    except Exception as e:
        print(f"Iara: Desculpe, tive um probleminha interno. Pode repetir? ({str(e)[:100]}...)\n")
