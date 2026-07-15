from .brain.cerebro import Cerebro
from .eventos import EventBus

from .plugins import GerenciadorPlugins

from .servicos import (
    Logger,
    Configuracao,
    ServicoMemoria
)


class Kernel:

    def __init__(self):

        self.logger = Logger()

        self.config = Configuracao()

        self.memoria = ServicoMemoria()

        self.bus = EventBus()

        self.agentes = {}

        self.ferramentas = {}
        
        self.plugins = GerenciadorPlugins(
            self
        )
        
        self.cerebro = Cerebro()

    def iniciar(self):

        self.logger.info(
            "Inicializando Kernel..."
        )

        self.plugins.carregar_plugins()

        self.logger.info(
            "Kernel iniciado."
        )

    def registrar_agente(self, agente):

        self.agentes[
            agente.nome
        ] = agente

    def registrar_ferramenta(self, ferramenta):

        self.ferramentas[
            ferramenta.nome
        ] = ferramenta
