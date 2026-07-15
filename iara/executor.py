"""
Executor da Iara.

Executa os passos definidos pelo planejador.
"""


def executar_plano(evento):

    objetivo = evento.objetivo

    for passo in objetivo.plano:

        acao = passo["acao"]

        if acao == "consultar_memoria":

            objetivo.resultado = evento.memoria

        elif acao == "salvar_memoria":

            pass

        elif acao == "confirmar":

            pass

        elif acao == "responder":

            pass

    objetivo.concluido = True

    return evento
