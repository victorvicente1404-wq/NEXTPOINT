from iara.memoria import lembrar_nome
from iara.personalidade import NOME

def falar():
    print("Olá! Eu sou a Iara.")

    nome = lembrar_nome()

    print(f"Bem-vindo, {nome}!")
