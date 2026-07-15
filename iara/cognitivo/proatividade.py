"""
Sistema de Proatividade da Iara (Modo JARVIS)
Responsável por tomar iniciativas e sugestões.
"""

from datetime import datetime
from ..pipeline.memoria import consultar, aprender

class Proatividade:
    
    def __init__(self):
        self.ultima_iniciativa = None
    
    def deve_iniciar(self, evento):
        """Decide se deve tomar iniciativa."""
        # Regras simples por enquanto
        hora = datetime.now().hour
        
        # Bom dia / Boa noite
        if hora < 12 and not self.ultima_iniciativa:
            return "bom_dia"
        elif hora >= 22:
            return "boa_noite"
        
        # Sugestões baseadas em rotina (futuro)
        # if "rotina" in consultar("rotina"):
        #     return "sugestao_rotina"
        
        return None
    
    def gerar_iniciativa(self, tipo):
        """Gera uma mensagem proativa."""
        if tipo == "bom_dia":
            return "Bom dia! Como você dormiu? Tem algo que eu possa ajudar hoje?"
        elif tipo == "boa_noite":
            return "Já está tarde. Quer que eu te lembre de algo antes de dormir?"
        
        return "Tudo bem por aí? Estou aqui se precisar de mim."
    
    def registrar_iniciativa(self):
        self.ultima_iniciativa = datetime.now()
