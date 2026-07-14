from motor_conversa import responder
from historico import salvar
from estado import mudar_estado

def conversar():

    mudar_estado("conversando")

    while True:

        mensagem = input("Você: ")

        if mensagem.lower() == "sair":
            print("Iara: Até logo! 😊")
            mudar_estado("ociosa")
            break

        resposta = responder(mensagem)

        salvar(mensagem, resposta)

        print(f"Iara: {resposta}")
