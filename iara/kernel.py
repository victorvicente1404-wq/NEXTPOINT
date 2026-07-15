"""
Kernel da Iara.

Coordena o funcionamento da IA.
"""

from .modelos.evento import Evento

from .motor_conversa import conversar


class Kernel:

    def processar(self, mensagem):

        evento = Evento(mensagem)

        resposta = conversar(evento)

        return resposta
        decidir(evento)

        planejar(evento.objetivo)

        executar_plano(evento)

        evento.resposta = responder(evento.decisao)

        atualizar(
            evento.mensagem,
            evento.intencao,
            evento.resposta
        )

        self.contexto = obter()

        return evento.resposta
