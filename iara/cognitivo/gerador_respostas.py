"""
Gerador Inteligente de Respostas - Estilo JARVIS / Grok
"""

from ..pipeline.memoria import consultar

class GeradorRespostas:
    
    def gerar(self, evento):
        """Gera resposta inteligente e natural."""
        
        texto = evento.texto
        tipo = evento.objetivo.tipo
        nome = consultar("perfil_usuario.nome") or "você"

        # Lógica inteligente simples por enquanto (pode evoluir para chamar API)
        if "como vai" in texto or "tudo bem" in texto:
            return f"Tô bem, {nome}! E você, como tá o dia até agora?"

        elif "o que você pode fazer" in texto or "quem é você" in texto:
            return ("Sou a Iara, sua assistente pessoal. " 
                   "Estou aqui pra te ajudar, conversar, lembrar coisas importantes "
                   "e tornar seu dia mais fácil. Me conta o que você precisa.")

        # Resposta padrão inteligente
        return ("Entendi o que você disse. " 
                "Me dá mais detalhes que eu te ajudo melhor, pode ser?")


# Instância global
gerador = GeradorRespostas()
