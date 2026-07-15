"""
Interpretador da Iara.
"""

import re

from .evento import Evento
from .extrator import extrair
from .nlp import limpar_texto
from .padroes import PADROES


def interpretar(evento: Evento):

    evento.texto = limpar_texto(evento.mensagem)

    evento.entidades = extrair(
        evento.texto
    )

    evento.intencao = "desconhecido"
    evento.confianca = 0.0

    for nome, lista in PADROES.items():

        for padrao in lista:

            if re.fullmatch(
                padrao,
                evento.texto
            ):

                evento.intencao = nome
                evento.confianca = 1.0

                return evento

    return evento
