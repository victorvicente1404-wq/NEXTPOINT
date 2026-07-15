"""
Classe base para todos os agentes da Iara.
"""

AGENTES = []


class Agente:

    nome = "Agente"

    prioridade = 0

    descricao = ""

    def aceita(self, evento):

        return False

    def executar(self, evento):

        raise NotImplementedError


def registrar(classe):

    AGENTES.append(classe())

    return classe


def encontrar(evento):

    candidatos = []

    for agente in AGENTES:

        if agente.aceita(evento):

            candidatos.append(agente)

    if not candidatos:

        return None

    candidatos.sort(

        key=lambda a: a.prioridade,

        reverse=True

    )

    return candidatos[0]
