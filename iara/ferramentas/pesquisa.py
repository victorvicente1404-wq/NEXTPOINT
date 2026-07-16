"""
Pesquisa Avançada da Iara
"""

import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4 lxml (se precisar)

class Pesquisador:
    
    def pesquisar(self, query):
        """Pesquisa real na web usando DuckDuckGo."""
        print(f"🔍 Iara pesquisando: {query}")
        
        try:
            url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
            headers = {"User-Agent": "Mozilla/5.0"}
            
            response = requests.get(url, headers=headers, timeout=5)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                resultados = soup.find_all('a', class_='result__a')
                
                if resultados:
                    snippet = resultados[0].get_text()[:200]
                    return f"Encontrei isso: {snippet}..."
                
            return "Pesquisei, mas não achei algo muito preciso. Pode reformular?"
            
        except Exception:
            return "Não consegui acessar a internet agora. Me pergunta outra coisa ou tenta mais tarde."
            
pesquisador = Pesquisador()
