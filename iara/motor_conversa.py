"""
Motor principal da Iara - Modo Parceira / JARVIS
"""

from .pipeline.interpretador import interpretar
from .pipeline.memoria import carregar, aprender
from .pipeline.contexto import obter, atualizar
from .planejamento.raciocinio import decidir
from .planejamento.planejador import planejar
from .planejamento.executor import executar_plano
from .pipeline.respostas import responder
from .cognitivo.proatividade import Proatividade   # ← Novo


proatividade = Proatividade()   # Instância global


def conversar(evento):
    """Fluxo principal com proatividade."""
    
    evento.memoria = carregar()
    evento.contexto = obter()

    interpretar(evento)

    # Aprendizado
    if evento.entidades:
        aprender(evento.entidades)
        evento.memoria = carregar()

    # Decisão + Planejamento
    decidir(evento)
    planejar(evento)
    executar_plano(evento)

    # Resposta normal
    evento.resposta = responder(evento)

    atualizar(evento.mensagem, evento.intencao, evento.resposta)

    return evento.resposta


# Função para modo proativo (chamada periodicamente ou por evento)
def iniciativa_proativa():
    """Iara pode falar por iniciativa própria."""
    tipo = proatividade.deve_iniciar(None)
    if tipo:
        mensagem = proatividade.gerar_iniciativa(tipo)
        proatividade.registrar_iniciativa()
        print(f"Iara (proativa): {mensagem}")
        return mensagem
    return None
