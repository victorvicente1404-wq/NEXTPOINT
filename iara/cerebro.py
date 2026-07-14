from iara.estado import mudar_estado
from iara.conversa import falar
from iara.ciclo import observar

def iniciar():
    mudar_estado("iniciando")

    falar()

    mudar_estado("observando")

    observar()
