from iara.estado import mudar_estado

def pensar(evento):

    print(f"🧠 Pensando sobre: {evento}")

    if evento == "sistema_iniciado":
        mudar_estado("observando")
        print("Tudo funcionando normalmente.")

    elif evento == "pessoa_detectada":
        mudar_estado("analisando")
        print("Uma pessoa foi detectada.")

    elif evento == "usuario_conhecido":
        mudar_estado("cumprimentando")
        print("Vou cumprimentar essa pessoa.")

    else:
        print("Ainda não sei como lidar com isso.")
