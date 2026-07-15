"""
Motor principal da Iara.

Controla todo o fluxo da conversa.
"""

from .pipeline.interpretador import interpretar
from .pipeline.memoria import (
    carregar,
    aprender
)
from .pipeline.contexto import (
    obter,
    atualizar
)
from .planejamento.raciocinio import decidir
from .planejamento.planejador import planejar
from .planejamento.executor import executar
from .pipeline.respostas import responder


def conversar(evento):

    # -------------------------
    # Memória e contexto
    # -------------------------

    evento.memoria = carregar()

    evento.contexto = obter()

    # -------------------------
    # Pipeline
    # -------------------------

    interpretar(evento)

    # -------------------------
    # Aprendizado
    # -------------------------

    if evento.entidades:

        aprender(evento.entidades)

        evento.memoria = carregar()

    # -------------------------
    # Planejamento
    # -------------------------

    decidir(evento)

    planejar(evento)

    executar(evento)

    # -------------------------
    # Resposta
    # -------------------------

    evento.resposta = responder(evento)

    # -------------------------
    # Contexto
    # -------------------------

    atualizar(

        evento.mensagem,

        evento.intencao,

        evento.resposta

    )

    return evento.resposta    # Executa ações
    executar(evento.decisao)

    # Gera resposta
    evento.resposta = responder(
        evento.decisao
    )

    # Atualiza contexto
    atualizar(
        evento.mensagem,
        evento.intencao,
        evento.resposta
    )

    return evento.resposta
