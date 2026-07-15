"""
Gerenciador de Plugins.
"""

import importlib
import pkgutil

from .plugin import Plugin


class GerenciadorPlugins:

    def __init__(self, kernel):

        self.kernel = kernel

        self.plugins = {}

    def carregar_plugins(self):

        import iara.plugins as plugins

        for _, modulo, _ in pkgutil.iter_modules(
            plugins.__path__
        ):

            if modulo in (
                "plugin",
                "gerenciador"
            ):
                continue

            modulo_importado = importlib.import_module(
                f"iara.plugins.{modulo}"
            )

            if hasattr(modulo_importado, "plugin"):

                plugin = modulo_importado.plugin

                if isinstance(plugin, Plugin):

                    plugin.carregar(self.kernel)

                    self.plugins[
                        plugin.nome
                    ] = plugin

                    self.kernel.logger.info(
                        f"Plugin carregado: {plugin.nome}"
                    )

    def descarregar(self, nome):

        plugin = self.plugins.get(nome)

        if plugin:

            plugin.descarregar(self.kernel)

            del self.plugins[nome]

            self.kernel.logger.info(
                f"Plugin descarregado: {nome}"
            )
