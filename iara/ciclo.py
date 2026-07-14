import time

from eventos import proximo_evento
from nucleo import pensar

def observar():

    while True:

        evento = proximo_evento()

        if evento:

            pensar(evento)

        else:

            print("👀 Observando...")

        time.sleep(2)
