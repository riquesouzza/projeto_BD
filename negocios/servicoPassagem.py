from persistencia.crudPassagem import (
    cadastrar_passagem,
    listar_passagens,
    ler_passagem,
    editar_passagem,
    deletar_passagem
)

# SERVICOS PASSAGEM

def servico_cadastrar_passagem(id_passagem, num_cartao, valor, data_hora, id_viagem):
    cadastrar_passagem(id_passagem, num_cartao, valor, data_hora, id_viagem)


def servico_listar_passagens():
    return listar_passagens()


def servico_ler_passagem(id_passagem):
    return ler_passagem(id_passagem)


def servico_editar_passagem(id_passagem, num_cartao=None, valor=None, data_hora=None, id_viagem=None):
    editar_passagem(id_passagem, num_cartao, valor, data_hora, id_viagem)


def servico_deletar_passagem(id_passagem):
    deletar_passagem(id_passagem)
