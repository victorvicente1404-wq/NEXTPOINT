import time

from iara.eventos import proximo_evento
from iara.nucleo import pensar

def observar():

    while True:

        evento = proximo_evento()

        if evento:

            pensar(evento)

        else:

            print("👀 Observando...")

        time.sleep(2)
