import time
from iara.eventos import proximo_evento

def observar():
    while True:

        evento = proximo_evento()

        if evento:
            print(f"📩 Evento recebido: {evento}")

        else:
            print("👀 Observando o ambiente...")

        time.sleep(2)
