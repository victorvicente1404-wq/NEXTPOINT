"""
Ferramenta de Pesquisa da Iara
Permite pesquisar na web e usar conhecimento externo.
"""

import requests
# No futuro podemos integrar APIs como DuckDuckGo, Google, etc.

class Pesquisador:
    
    def pesquisar(self, query):
        """Pesquisa simples (pode ser expandida)."""
        print(f"Iara está pesquisando: {query}")
        
        # Simulação por enquanto (depois conectamos API real)
        respostas_simuladas = {
            "clima": "Hoje está ensolarado na sua região.",
            "noticias": "As principais notícias do dia...",
            "ajuda": "Claro! Em que posso te ajudar hoje?"
        }
        
        for chave in respostas_simuladas:
            if chave in query.lower():
                return respostas_simuladas[chave]
        
        return f"Pesquisei sobre '{query}'. Me dá mais detalhes do que você quer saber que eu aprofundo."


pesquisador = Pesquisador()
