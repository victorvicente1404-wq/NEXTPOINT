"""
Raciocínio da Iara - Versão Melhorada
"""

def decidir(evento):
    """Decide o objetivo principal com base na mensagem do usuário."""
    
    texto = evento.texto.lower().strip()
    objetivo = evento.objetivo

    # === INTENÇÕES PRIORITÁRIAS ===

    # Cumprimentos e conversa casual
    if any(p in texto for p in ["oi", "olá", "eae", "fala", "bom dia", "boa tarde", "boa noite"]):
        objetivo.tipo = "cumprimento"
        return evento

    # Despedidas
    if any(p in texto for p in ["tchau", "até logo", "falou", "adeus"]):
        objetivo.tipo = "despedida"
        return evento

    # Consultar informações pessoais
    if "meu nome" in texto or "quem sou eu" in texto:
        objetivo.tipo = "consultar_nome"
        return evento

    if "idade" in texto and ("tenho" in texto or "minha" in texto or "quantos anos" in texto):
        objetivo.tipo = "consultar_idade"
        return evento

    # Aprendizado (quando o usuário se apresenta ou conta algo)
    if evento.entidades:
        objetivo.tipo = "aprender"
        objetivo.parametros = {"dados": evento.entidades}
        return evento

    # === EXPANSÃO FUTURA (já preparado) ===
    # if "como vai" in texto or "tudo bem" in texto:
    #     objetivo.tipo = "bem_estar"

    # Padrão: conversa normal
    objetivo.tipo = "conversar"
    return evento
