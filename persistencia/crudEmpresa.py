from connector import *

def criarEmpresa(cnpj, telefone, nome, endereco):
    comando = f'INSERT INTO EMPRESA (CNPJ, telefone, nome, endereco) VALUES ("{cnpj}", "{telefone}", "{nome}", "{endereco}")'
    comandoEscrita(comando)

def lerEmpresa(cnpj):
    comando = f'SELECT * FROM EMPRESA WHERE CNPJ={cnpj}'
    return comandoLeitura(comando)

def editarEmpresa(cnpj, telefone=None, nome=None, endereco=None):
    if telefone is not None:
        comando = f'UPDATE EMPRESA SET telefone = "{telefone}" WHERE CNPJ = "{cnpj}"'
        comandoEscrita(comando)
    if nome is not None:
        comando = f'UPDATE EMPRESA SET nome = "{nome}" WHERE CNPJ = "{cnpj}"'
        comandoEscrita(comando)
    if endereco is not None:
        comando = f'UPDATE EMPRESA SET endereco = "{endereco}" WHERE CNPJ = "{cnpj}"'
        comandoEscrita(comando)
        
def deletarEmpresa(cnpj):
    comando = f'DELETE FROM EMPRESA WHERE CNPJ="{cnpj}"'
    comandoEscrita(comando)

def lerEmpresas():
    comando = 'SELECT * FROM EMPRESA'
    return comandoLeitura(comando)