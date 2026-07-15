"""
Classe base para plugins da Iara.
"""


class Plugin:

    nome = "Plugin"

    versao = "1.0.0"

    autor = ""

    descricao = ""

    def carregar(self, kernel):

        """
        Chamado quando o plugin é carregado.
        """
        pass

    def descarregar(self, kernel):

        """
        Chamado quando o plugin é descarregado.
        """
        pass
