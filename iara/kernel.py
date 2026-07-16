def processar(self, mensagem):
        """Processa a mensagem do usuário e retorna a resposta da Iara."""
        from iara.modelos.evento import Evento
        
        evento = Evento(mensagem)
        
        try:
            resposta = conversar(evento)   # Chama o motor principal
            return resposta
        except Exception as e:
            return f"Desculpe, tive um problema: {str(e)}"
