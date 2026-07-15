from .eventos import EventBus

from .servicos.memoria import ServicoMemoria


class Kernel:

    def __init__(self):

        self.bus = EventBus()

        self.memoria = ServicoMemoria()

        self.agentes = []

        self.ferramentas = []

        self.plugins = []

    def iniciar(self):

        print("Kernel iniciado.")
