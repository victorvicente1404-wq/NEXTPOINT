from humor import obter_humor

def responder_boas_vindas(nome):

    humor = obter_humor()

    if humor == "feliz":
        print(f"😊 Oi, {nome}! Que bom te ver!")

    elif humor == "animada":
        print(f"😄 E aí, {nome}! Seja muito bem-vindo!")

    elif humor == "curiosa":
        print(f"🤔 Olá, {nome}. O que vamos fazer hoje?")

    else:
        print(f"Olá, {nome}.")
