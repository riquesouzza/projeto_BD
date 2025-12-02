from connector import *
from .crudEmpresa import lerEmpresa 

def listar_linhas():
    comando = 'SELECT * FROM linha'
    return comandoLeitura(comando)


def cadastrar_linha(cod_linha, id_empresa, nome, valor):
    if not lerEmpresa(id_empresa):
        print(f"Erro: Empresa com CNPJ {id_empresa} nao existe.")
        return
    comando = f'INSERT INTO linha (codLinha, idEmpresa, nome, valor) VALUES ("{cod_linha}", "{id_empresa}", "{nome}","{valor}" )'
    comandoEscrita(comando)


def ler_linha(cod_linha):
    comando = f'SELECT * FROM linha WHERE codLinha="{cod_linha}"'
    return comandoLeitura(comando)


def deletar_linha(cod_linha):
    comando = f'DELETE FROM linha WHERE codLinha="{cod_linha}"'
    comandoEscrita(comando)


def editar_linha(cod_linha, id_empresa=None, nome=None, valor= None):
    if id_empresa is not None:
        if not lerEmpresa(id_empresa):
            print(f"Erro: Empresa com CNPJ {id_empresa} nao existe.")
            return
        comando = f'UPDATE linha SET idEmpresa = "{id_empresa}" WHERE codLinha = "{cod_linha}"'
        comandoEscrita(comando)
    if nome is not None:
        comando = f'UPDATE linha SET nome = "{nome}" WHERE codLinha = "{cod_linha}"'
        comandoEscrita(comando)
    if valor is not None:
        comando = f'UPDATE linha SET valor = "{valor}" WHERE codLinha = "{cod_linha}"'
        comandoEscrita(comando)
 
def listar_historico_linhas():
    comando = 'SELECT * FROM historico_linha'
    return comandoLeitura(comando)

def listar_historico_linha(cod_linha):
    comando = f'SELECT * FROM historico_linha WHERE codLinha = "{cod_linha}"'
    return comandoLeitura(comando)