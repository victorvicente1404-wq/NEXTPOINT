"""
Interpretador da Iara.

Analisa a mensagem e preenche o Evento.
"""

from ..intencoes import identificar_intencao
from .extrator import extrair_entidades


def interpretar(evento):

    texto = evento.mensagem.strip()

    evento.texto = texto

    evento.intencao = identificar_intencao(texto)

    evento.entidades = extrair_entidades(texto)

    return evento
    return evento
