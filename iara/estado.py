ESTADO = "iniciando"


def mudar_estado(novo_estado):
    global ESTADO
    ESTADO = novo_estado


def estado_atual():
    return ESTADO
