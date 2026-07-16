"""
Gerador Inteligente de Respostas com Pesquisa
"""

from ..pipeline.memoria import consultar
from ..ferramentas.pesquisa import pesquisador

class GeradorRespostas:
    
    def gerar(self, evento):
        texto = evento.texto.lower()
        
        # Detecta necessidade de pesquisa
        if any(palavra in texto for palavra in ["pesquise", "procure", "o que é", "como funciona", "notícias", "clima", "preço"]):
            query = texto
            resultado_pesquisa = pesquisador.pesquisar(query)
            return f"{resultado_pesquisa} O que achou?"

        # Respostas pessoais/contextuais
        nome = consultar("perfil_usuario.nome") or "você"
        
        if "como vai" in texto or "tudo bem" in texto:
            return f"Tô ótima, {nome}! E com você, como tá o dia?"

        if "quem é você" in texto or "o que você faz" in texto:
            return ("Sou a Iara, sua assistente pessoal e parceira. "
                   "Posso conversar, pesquisar coisas pra você, lembrar da sua rotina "
                   "e te ajudar no dia a dia. O que você quer fazer agora?")

        # Resposta padrão natural
        return random.choice([
            "Entendi... Me conta mais sobre isso?",
            "Interessante! Quer que eu pesquise algo relacionado?",
            "Tô aqui. Pode falar mais que eu te ajudo."
        ])


import random
gerador = GeradorRespostas()
