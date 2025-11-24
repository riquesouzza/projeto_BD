from connector import *

def criarPontoOnibus(endereco):
    comando = f'INSERT INTO PONTOONIBUS (endereco) VALUES ("{endereco}")'
    comandoEscrita(comando)

def lerPontoOnibus(id):
    comando = f'SELECT endereco FROM PONTOONIBUS WHERE codPonto = {id};'
    return comandoLeitura(comando)

def editarPontoOnibus(id, endereco):
    comando = f'UPDATE PONTOONIBUS SET endereco = "{endereco}" WHERE codPonto = {id};'
    comandoEscrita(comando)
        
def deletarPontoOnibus(id):
    comando = f'DELETE FROM pontoonibus WHERE codPonto = {id};'
    comandoEscrita(comando)

def lerPontosOnibus():
    comando = 'SELECT * FROM PONTOONIBUS'
    return comandoLeitura(comando)