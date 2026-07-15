"""
Sistema de Memória da Iara - Versão JARVIS
Suporta aprendizado contínuo e observações do ambiente.
"""

import json
from pathlib import Path
from datetime import datetime

CAMINHO = Path(__file__).parent.parent.parent / "data" / "memoria.json"

def carregar():
    """Carrega a memória."""
    if not CAMINHO.exists():
        memoria_padrao = {
            "perfil_usuario": {"nome": "", "apelido": "", "idade": None},
            "preferencias": {},
            "rotina": {},
            "observacoes": {
                "ultima_atividade": None,
                "estado_emocional": "neutro",
                "ultima_observacao": None
            },
            "historico": [],
            "conhecimento_ambiente": {}
        }
        salvar(memoria_padrao)
        return memoria_padrao
    
    with open(CAMINHO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar(memoria):
    """Salva a memória."""
    CAMINHO.parent.mkdir(parents=True, exist_ok=True)
    with open(CAMINHO, "w", encoding="utf-8") as arquivo:
        json.dump(memoria, arquivo, indent=4, ensure_ascii=False)

def aprender(dados):
    """Aprende novas informações (de conversa ou observação)."""
    memoria = carregar()
    
    if isinstance(dados, dict):
        # Aprendizado estruturado
        for chave, valor in dados.items():
            if chave in memoria:
                memoria[chave] = valor
            else:
                memoria["observacoes"][chave] = valor
    
    # Registra no histórico
    memoria["historico"].append({
        "timestamp": datetime.now().isoformat(),
        "dados": dados
    })
    
    # Mantém histórico razoável
    if len(memoria["historico"]) > 100:
        memoria["historico"] = memoria["historico"][-100:]
    
    salvar(memoria)
    return memoria

def consultar(chave):
    """Consulta informação na memória."""
    memoria = carregar()
    # Suporte a chaves aninhadas (ex: "perfil_usuario.nome")
    chaves = chave.split(".")
    valor = memoria
    for k in chaves:
        valor = valor.get(k) if isinstance(valor, dict) else None
    return valor
