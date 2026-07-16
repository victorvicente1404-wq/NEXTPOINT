"""
Sistema de Respostas da Iara - Personalidade Parceira
"""

import random
from ..pipeline.memoria import consultar

def responder(evento):
    """Gera respostas naturais e contextuais."""
    
    tipo = evento.objetivo.tipo
    memoria = evento.memoria
    nome = consultar("perfil_usuario.nome") or "amigo"

    # Respostas personalizadas
    if tipo == "cumprimento":
        return random.choice([
            f"Oi, {nome}! Que bom te ver.",
            f"E aí, {nome}? Tudo bem por aí?",
            f"Bom te ver por aqui! 😊"
        ])

    elif tipo == "consultar_perfil":
        if nome:
            return f"Você é o {nome}. Estou aqui pra te ajudar no que precisar."
        return "Ainda não sei seu nome direito. Me conta mais sobre você?"

    elif tipo == "aprender":
        return random.choice([
            "Entendi! Vou guardar isso.",
            "Legal, obrigado por me contar. Vou lembrar disso.",
            "Certo! Aprendido. 😊"
        ])

    # Resposta padrão mais natural
    respostas_padrao = [
        "Entendi... Me conta mais?",
        "Interessante! O que você acha disso?",
        "Tô aqui ouvindo. Pode falar.",
        "Hum... e aí, o que mais?"
    ]
    
    return random.choice(respostas_padrao)
