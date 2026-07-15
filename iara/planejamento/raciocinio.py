"""
Raciocínio Avançado da Iara (Modo JARVIS)
"""

from ..pipeline.memoria import consultar

def decidir(evento):
    texto = evento.texto.lower().strip()
    objetivo = evento.objetivo

    # Memória rápida
    nome = consultar("perfil_usuario.nome")

    # Cumprimentos personalizados
    if any(saud in texto for saud in ["oi", "olá", "eae", "fala", "bom dia", "boa tarde"]):
        objetivo.tipo = "cumprimento"
        objetivo.parametros = {"nome": nome}
        return evento

    # Perguntas sobre si mesmo
    if "meu nome" in texto or "quem sou" in texto:
        objetivo.tipo = "consultar_perfil"
        return evento

    # Aprendizado de qualquer informação
    if evento.entidades or any(palavra in texto for palavra in ["meu", "eu", "gosto", "costumo", "sempre"]):
        objetivo.tipo = "aprender"
        objetivo.parametros = {"dados": evento.entidades or texto}
        return evento

    # Modo JARVIS: Observação implícita
    objetivo.tipo = "conversar"
    objetivo.parametros = {"contexto_personalizado": True}
    
    return evento
