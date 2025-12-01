from persistencia.crudLinha import (
    cadastrar_linha,
    listar_linhas,
    ler_linha,
    editar_linha,
    deletar_linha,
    listar_historico_linhas, 
    listar_historico_linha
)

# SERVICOS LINHA

def servico_cadastrar_linha(cod_linha, id_empresa, nome, valor):
    cadastrar_linha(cod_linha, id_empresa, nome, valor)


def servico_listar_linhas():
    return listar_linhas()


def servico_ler_linha(cod_linha):
    return ler_linha(cod_linha)


def servico_editar_linha(cod_linha, id_empresa=None, nome=None, valor = None):
    editar_linha(cod_linha, id_empresa, nome, valor)


def servico_deletar_linha(cod_linha):
    deletar_linha(cod_linha)

def servico_listar_historico_linhas():
    return listar_historico_linhas()

def servico_listar_historico_linha(cod_linha):
    return listar_historico_linha(cod_linha)