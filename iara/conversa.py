from iara.memoria import lembrar_nome
from iara.respostas import responder_boas_vindas

def falar():

    print("Olá! Eu sou a Iara.")

    nome = lembrar_nome()

    responder_boas_vindas(nome)
