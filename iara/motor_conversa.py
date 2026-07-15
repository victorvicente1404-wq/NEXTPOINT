"""
Motor principal da conversa.
"""

from .evento import Evento
from .interpretador import interpretar
from .contexto import atualizar, obter
from .memoria import carregar, aprender
from .raciocinio import decidir
from .acoes import executar
from .respostas import responder


def conversar(mensagem: str):

    # Cria o evento
    evento = Evento(mensagem)

    # Interpreta a mensagem
    interpretar(evento)

    # Aprende automaticamente
    if evento.entidades:
        aprender(evento.entidades)

    # Carrega contexto e memória
    evento.contexto = obter()
    evento.memoria = carregar()

    # Decide o que fazer
    evento.decisao = decidir(
        evento,
        evento.contexto,
        evento.memoria
    )

    # Executa ações
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
