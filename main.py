from config import NOME_PROJETO, VERSAO_PROJETO
from iara.estado import mudar_estado, estado_atual
from iara.conversa import falar

print(f"Iniciando {NOME_PROJETO}...")
print(f"Versão {VERSAO_PROJETO}")

mudar_estado("conversando")

falar()

mudar_estado("ociosa")

print(f"Estado atual: {estado_atual()}")
