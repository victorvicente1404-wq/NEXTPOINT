from iara.pensamentos import pensar
from iara.estado import mudar_estado
from iara.decisao import decidir
from iara.acoes import executar

def processar_evento(evento):

    print(f"🧠 Evento: {evento}")

    pensar(evento)

    acao = decidir(evento)

    print(f"🎯 Decisão: {acao}")

    executar(acao)

    mudar_estado(acao)
