from iara.memoria import lembrar_nome
from iara.personalidade import NOME

def falar():
    print(APRESENTACAO)

    nome = lembrar_nome()

    print(f"Bem-vindo, {nome}!")
