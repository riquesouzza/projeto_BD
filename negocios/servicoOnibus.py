from persistencia.crudOnibus import (
    cadastrar_onibus,
    listar_onibus,
    ler_onibus,
    editar_onibus,
    deletar_onibus
)

# SERVICOS ONIBUS

def servico_cadastrar_onibus(placa, capacidade, id_empresa):
    cadastrar_onibus(placa, capacidade, id_empresa)


def servico_listar_onibus():
    return listar_onibus()


def servico_ler_onibus(placa):
    return ler_onibus(placa)


def servico_editar_onibus(placa, capacidade=None, id_empresa=None):
    editar_onibus(placa, capacidade, id_empresa)


def servico_deletar_onibus(placa):
    deletar_onibus(placa)
