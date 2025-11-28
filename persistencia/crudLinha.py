from connector import *
from .crudEmpresa import lerEmpresa 

# LISTAR LINHAS
def listar_linhas():
    comando = 'SELECT * FROM linha'
    return comandoLeitura(comando)

# CADASTRA LINHA
def cadastrar_linha(cod_linha, id_empresa, nome):
    if not lerEmpresa(id_empresa):
        print(f"Erro: Empresa com CNPJ {id_empresa} nao existe.")
        return
    comando = f'INSERT INTO linha (codLinha, idEmpresa, nome) VALUES ("{cod_linha}", "{id_empresa}", "{nome}")'
    comandoEscrita(comando)

# LER LINHA
def ler_linha(cod_linha):
    comando = f'SELECT * FROM linha WHERE codLinha="{cod_linha}"'
    return comandoLeitura(comando)

# DELETAR LINHA
def deletar_linha(cod_linha):
    comando = f'DELETE FROM linha WHERE codLinha="{cod_linha}"'
    comandoEscrita(comando)

# UPDATES LINHA
def editar_linha(cod_linha, id_empresa=None, nome=None):
    if id_empresa is not None:
        if not lerEmpresa(id_empresa):
            print(f"Erro: Empresa com CNPJ {id_empresa} nao existe.")
            return
        comando = f'UPDATE linha SET idEmpresa = "{id_empresa}" WHERE codLinha = "{cod_linha}"'
        comandoEscrita(comando)
    if nome is not None:
        comando = f'UPDATE linha SET nome = "{nome}" WHERE codLinha = "{cod_linha}"'
        comandoEscrita(comando)
