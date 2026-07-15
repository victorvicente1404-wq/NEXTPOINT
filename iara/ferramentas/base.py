"""
Sistema base de ferramentas da Iara.
"""


FERRAMENTAS = []


class Ferramenta:

    nome = "Ferramenta"

    descricao = ""

    def executar(self, parametros):

        raise NotImplementedError



def registrar(classe):

    FERRAMENTAS.append(
        classe()
    )

    return classe



def encontrar(nome):

    for ferramenta in FERRAMENTAS:

        if ferramenta.nome == nome:

            return ferramenta

    return None
