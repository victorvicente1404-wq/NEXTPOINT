from iara.motor_conversa import responder

def conversar():

    while True:

        mensagem = input("Você: ")

        if mensagem.lower() == "sair":
            print("Iara: Até logo! 😊")
            break

        resposta = responder(mensagem)

        print(f"Iara: {resposta}")
