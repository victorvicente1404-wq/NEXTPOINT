from collections import defaultdict

from .evento import EventoSistema


class EventBus:

    def __init__(self):

        self._listeners = defaultdict(list)

        self._historico = []

    def registrar(self, tipo, callback):

        self._listeners[tipo].append(callback)

    def emitir(self, evento: EventoSistema):

        self._historico.append(evento)

        for callback in self._listeners[evento.tipo]:

            if evento.cancelado:

                break

            callback(evento)

    def historico(self):

        return list(self._historico)

    def limpar(self):

        self._historico.clear()
