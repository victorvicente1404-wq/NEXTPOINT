from iara.estado import mudar_estado
from iara.conversa import falar

def iniciar():
    mudar_estado("iniciando")

    falar()

    mudar_estado("observando")
