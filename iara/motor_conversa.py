def conversar(mensagem):

    intencao = identificar_intencao(mensagem)

    contexto = obter()

    memoria = carregar()

    decisao = decidir(
        intencao,
        contexto,
        memoria
    )

    resposta = responder(decisao)

    atualizar(
        mensagem,
        intencao,
        resposta
    )

    return resposta
