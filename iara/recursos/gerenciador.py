class GerenciadorRecursos:

    def __init__(self):

        self.agentes = {}

        self.ferramentas = {}

        self.modelos = {}

        self.plugins = {}

    def registrar_agente(self, agente):

        self.agentes[agente.nome] = agente

    def registrar_ferramenta(self, ferramenta):

        self.ferramentas[ferramenta.nome] = ferramenta

    def registrar_modelo(self, modelo):

        self.modelos[modelo.nome] = modelo

    def registrar_plugin(self, plugin):

        self.plugins[plugin.nome] = plugin
