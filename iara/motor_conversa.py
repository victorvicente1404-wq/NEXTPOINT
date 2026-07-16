"""
Motor principal da Iara - Versão Inteligente
"""

from .pipeline.interpretador import interpretar
from .pipeline.memoria import carregar, aprender
from .pipeline.contexto import obter, atualizar
from .planejamento.raciocinio import decidir
from .planejamento.planejador import planejar
from .planejamento.executor import executar_plano
from .cognitivo.gerador_respostas import gerador   # ← Novo
from .pipeline.respostas import responder   # Ainda mantemos como fallback


def conversar(evento):
    """Fluxo principal com respostas inteligentes."""
    
    evento.memoria = carregar()
    evento.contexto = obter()

    interpretar(evento)

    # Aprendizado
    if evento.entidades:
        aprender(evento.entidades)
        evento.memoria = carregar()

    # Raciocínio
    decidir(evento)
    planejar(evento)
    executar_plano(evento)

    # === GERAÇÃO INTELIGENTE DE RESPOSTA ===
    evento.resposta = gerador.gerar(evento)

    # Atualiza contexto
    atualizar(evento.mensagem, evento.intencao, evento.resposta)

    return evento.resposta
