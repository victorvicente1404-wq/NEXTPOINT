from iara.estado import mudar_estado
from iara.conversa import falar
from iara.ciclo import observar
from iara.eventos import adicionar_evento

def iniciar():

    mudar_estado("iniciando")

    falar()

    mudar_estado("observando")

    adicionar_evento("sistema_iniciado")

    observar()
