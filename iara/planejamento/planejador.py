"""
Planejador da Iara - Versão Melhorada
Transforma o objetivo em um plano de ações concreto.
"""

def planejar(evento):
    """Cria um plano de execução baseado no tipo de objetivo."""
    
    objetivo = evento.objetivo
    objetivo.plano = []  # Limpa plano anterior

    if objetivo.tipo == "consultar_nome":
        objetivo.plano.extend([
            {"acao": "ler_memoria", "chave": "usuario.nome"},
            {"acao": "responder_nome"}
        ])

    elif objetivo.tipo == "consultar_idade":
        objetivo.plano.extend([
            {"acao": "ler_memoria", "chave": "usuario.idade"},
            {"acao": "responder_idade"}
        ])

    elif objetivo.tipo == "aprender":
        objetivo.plano.extend([
            {"acao": "salvar_memoria"},
            {"acao": "confirmar_aprendizado"}
        ])

    elif objetivo.tipo == "cumprimento":
        objetivo.plano.append({"acao": "responder_cumprimento"})

    elif objetivo.tipo == "despedida":
        objetivo.plano.append({"acao": "responder_despedida"})

    else:
        # Conversa normal
        objetivo.plano.append({"acao": "responder_padrao"})

    return evento
