"""
Motor Principal da Iara - Versão Inteligente (JARVIS-like)
"""

from .pipeline.interpretador import interpretar
from .pipeline.memoria import carregar, aprender
from .pipeline.contexto import obter, atualizar
from .planejamento.raciocinio import decidir
from .planejamento.planejador import planejar
from .planejamento.executor import executar_plano
from .cognitivo.gerador_respostas import gerador


def conversar(evento):
    """Fluxo completo com inteligência e pesquisa."""
    
    # Preparação
    evento.memoria = carregar()
    evento.contexto = obter()

    # Processamento da entrada
    interpretar(evento)

    # Aprendizado contínuo
    if evento.entidades:
        aprender(evento.entidades)
        evento.memoria = carregar()

    # Raciocínio e planejamento
    decidir(evento)
    planejar(evento)
    executar_plano(evento)

    # Geração inteligente de resposta (com pesquisa se necessário)
    evento.resposta = gerador.gerar(evento)

    # Atualiza contexto
    atualizar(evento.mensagem, evento.intencao, evento.resposta)

    return evento.resposta
