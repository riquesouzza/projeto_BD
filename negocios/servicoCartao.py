from persistencia.crudCartao import (
    cadastrar_cartao,
    ler_cartao,
    editar_cartao,
    deletar_cartao,
    listar_cartoes
)


def servico_cadastrar_cartao(id, usuario, saldo):
    cadastrar_cartao(id, usuario, saldo)


def servico_listar_cartoes():
    return listar_cartoes()


def servico_ler_cartao(id):
    return ler_cartao(id)


def servico_editar_cartao(id, usuario=None, saldo=None):
    editar_cartao(id, usuario, saldo)


def servico_deletar_cartao(id):
    deletar_cartao(id)
