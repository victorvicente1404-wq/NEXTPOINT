from pensamentos import pensar
from estado import mudar_estado
from decisao import decidir
from acoes import executar

def processar_evento(evento):

    print(f"🧠 Evento: {evento}")

    pensar(evento)

    acao = decidir(evento)

    print(f"🎯 Decisão: {acao}")

    executar(acao)

    mudar_estado(acao)
