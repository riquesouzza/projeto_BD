from connector import *
from .crudEmpresa import lerEmpresa 


def listar_onibus():
    comando = 'SELECT * FROM onibus'
    return comandoLeitura(comando)


def cadastrar_onibus(placa, capacidade, id_empresa):
    if not lerEmpresa(id_empresa):
        print(f"Erro: Empresa com CNPJ {id_empresa} nao existe.")
        return
    comando = f'INSERT INTO onibus (placa, capacidade, idEmpresa) VALUES ("{placa}", "{capacidade}", "{id_empresa}")'
    comandoEscrita(comando)


def ler_onibus(placa):
    comando = f'SELECT * FROM onibus WHERE placa="{placa}"'
    return comandoLeitura(comando)

def deletar_onibus(placa):
    comando = f'DELETE FROM onibus WHERE placa="{placa}"'
    comandoEscrita(comando)


def editar_onibus(placa, capacidade=None, id_empresa=None):
    if id_empresa is not None:
        if not lerEmpresa(id_empresa):
            print(f"Erro: Empresa com CNPJ {id_empresa} nao existe.")
            return
        comando = f'UPDATE onibus SET idEmpresa = "{id_empresa}" WHERE placa = "{placa}"'
        comandoEscrita(comando)
    if capacidade is not None:
        comando = f'UPDATE onibus SET capacidade = "{capacidade}" WHERE placa = "{placa}"'
        comandoEscrita(comando)
