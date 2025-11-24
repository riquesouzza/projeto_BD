
from connector import *

# CRIA MOTORISTA

def cadastrar_motorista(cnh, nome, telefone, jornada):
    comando = f'INSERT INTO motorista (CNH, nome, telefone, jornada) VALUES ("{cnh}", "{nome}","{telefone}",{jornada})'
    comandoEscrita(comando)


   
# LISTAR MOTORISTAS

def listar_motoristas():
    comando = 'SELECT * FROM motorista'
    return comandoLeitura(comando)


# ATUALIZAR MOTORISTA


def editar_motorista(cnh, nome=None, telefone=None, jornada=None):
    if nome is not None:
        comando = f'UPDATE motorista SET nome = "{nome}" WHERE CNH = "{cnh}"'
        comandoEscrita(comando)
    if telefone is not None:
        comando = f'UPDATE motorista SET telefone = "{telefone}" WHERE CNH = "{cnh}"'
        comandoEscrita(comando)
    if jornada is not None:
        comando = f'UPDATE motorista SET jornada = {jornada} WHERE CNH = "{cnh}"'
        comandoEscrita(comando)


# REMOVER MOTORISTA

def deletar_motorista(cnh):
    comando = f'DELETE FROM motorista WHERE CNH = "{cnh}"'
    comandoEscrita(comando)
