from .eventos import EventBus

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

        self.plugins = {}

    def iniciar(self):

        self.logger.info("Kernel iniciado.")

    def registrar_agente(self, agente):

        self.agentes[agente.nome] = agente

        self.logger.info(
            f"Agente registrado: {agente.nome}"
        )

    def registrar_ferramenta(self, ferramenta):

        self.ferramentas[ferramenta.nome] = ferramenta

        self.logger.info(
            f"Ferramenta registrada: {ferramenta.nome}"
        )

    def registrar_plugin(self, plugin):

        self.plugins[plugin.nome] = plugin

        self.logger.info(
            f"Plugin registrado: {plugin.nome}"
        )
