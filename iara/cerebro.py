from estado import mudar_estado
from conversa import falar
from ciclo import observar
from eventos import adicionar_evento

def iniciar():

    mudar_estado("iniciando")

    falar()

    mudar_estado("observando")

    adicionar_evento("sistema_iniciado")

    observar()
