from iara.memoria import lembrar_nome
from iara.personalidade import NOME

def falar():
    print(f"Olá! Eu sou a {NOME}.")

    nome = lembrar_nome()

    print(f"Bem-vindo, {nome}!")
