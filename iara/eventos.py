EVENTOS = []

def adicionar_evento(evento):
    EVENTOS.append(evento)

def proximo_evento():
    if EVENTOS:
        return EVENTOS.pop(0)
    return None
