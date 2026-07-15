"""
Executor da Iara.

Executa o plano criado pelo planejador.
"""

from ..pipeline.memoria import (
    aprender,
    consultar
)


def executar(evento):

    objetivo = evento.objetivo

    for passo in objetivo.plano:

        acao = passo["acao"]

        # --------------------

        if acao == "ler_memoria":

            chave = passo["chave"]

            objetivo.resultado = consultar(chave)

        # --------------------

        elif acao == "salvar_memoria":

            aprender(

                objetivo.parametros["dados"]

            )

        # --------------------

        elif acao == "confirmar_aprendizado":

            objetivo.resultado = "aprendido"

        # --------------------

        elif acao == "responder_nome":

            pass

        # --------------------

        elif acao == "responder_idade":

            pass

        # --------------------

        elif acao == "responder_padrao":

            pass

    return evento
