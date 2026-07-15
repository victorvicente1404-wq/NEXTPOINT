from .plugin import Plugin


class PluginTeste(Plugin):

    nome = "Teste"

    versao = "1.0.0"

    autor = "Victor"

    descricao = "Plugin de teste."

    def carregar(self, kernel):

        kernel.logger.info(
            "Plugin Teste carregado."
        )


plugin = PluginTeste()
