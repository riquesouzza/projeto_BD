from persistencia.crudLinha import (
    cadastrar_linha,
    listar_linhas,
    ler_linha,
    editar_linha,
    deletar_linha
)

# SERVICOS LINHA

def servico_cadastrar_linha(cod_linha, id_empresa, nome):
    cadastrar_linha(cod_linha, id_empresa, nome)


def servico_listar_linhas():
    return listar_linhas()


def servico_ler_linha(cod_linha):
    return ler_linha(cod_linha)


def servico_editar_linha(cod_linha, id_empresa=None, nome=None):
    editar_linha(cod_linha, id_empresa, nome)


def servico_deletar_linha(cod_linha):
    deletar_linha(cod_linha)
