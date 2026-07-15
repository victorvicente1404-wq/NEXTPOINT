"""
Registro de ações da Iara.
"""

ACOES = {}


def registrar(nome):

    def decorator(func):

        ACOES[nome] = func

        return func

    return decorator


def executar(nome, evento, passo):

    funcao = ACOES.get(nome)

    if funcao is None:

        raise Exception(
            f"Ação '{nome}' não registrada."
        )

    return funcao(evento, passo)
