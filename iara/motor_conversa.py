"""
Motor principal da Iara - Versão Melhorada
Controla todo o fluxo da conversa de forma mais limpa.
"""

from .pipeline.interpretador import interpretar
from .pipeline.memoria import carregar, aprender
from .pipeline.contexto import obter, atualizar
from .planejamento.raciocinio import decidir
from .planejamento.planejador import planejar
from .planejamento.executor import executar_plano
from .pipeline.respostas import responder


def conversar(evento):
    """Fluxo principal da conversa."""
    
    # ====================== PREPARAÇÃO ======================
    evento.memoria = carregar()
    evento.contexto = obter()

    # ====================== PROCESSAMENTO ======================
    interpretar(evento)

    # Aprendizado automático
    if evento.entidades:
        aprender(evento.entidades)
        evento.memoria = carregar()

    # ====================== RACIOCÍNIO ======================
    decidir(evento)
    planejar(evento)
    executar_plano(evento)        # Usa o nome correto da função

    # ====================== RESPOSTA ======================
    evento.resposta = responder(evento)

    # Atualiza contexto da conversa
    atualizar(
        evento.mensagem,
        evento.intencao,
        evento.resposta
    )

    return evento.resposta
