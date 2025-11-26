from connector import *
from .crudEmpresa import lerEmpresa 

# LISTAR ÔNIBUS
def listar_onibus():
    comando = 'SELECT * FROM onibus'
    return comandoLeitura(comando)

# CADASTRA ÔNIBUS
def cadastrar_onibus(placa, capacidade, id_empresa):
    if not lerEmpresa(id_empresa):
        print(f"Erro: Empresa com CNPJ {id_empresa} nao existe.")
        return
    comando = f'INSERT INTO onibus (placa, capacidade, idEmpresa) VALUES ("{placa}", "{capacidade}", "{id_empresa}")'
    comandoEscrita(comando)

# LER ÔNIBUS
def ler_onibus(placa):
    comando = f'SELECT * FROM onibus WHERE placa="{placa}"'
    return comandoLeitura(comando)

# DELETAR ÔNIBUS
def deletar_onibus(placa):
    comando = f'DELETE FROM onibus WHERE placa="{placa}"'
    comandoEscrita(comando)

# UPDATES ÔNIBUS
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
