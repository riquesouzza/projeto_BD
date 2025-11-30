from connector import *
import os

def criarCobrador(matricula, telefone, nome, escala):
    comando = f'INSERT INTO COBRADOR (matricula, telefone, nome, escala) VALUES ("{matricula}", "{telefone}", "{nome}", "{escala}");'
    comandoEscrita(comando)

def lerCobrador(matricula):
    comando = f'SELECT * FROM COBRADOR WHERE matricula="{matricula}";'
    return comandoLeitura(comando)

def atualizarCobrador(matricula, telefone=None, nome=None, escala=None):
    if telefone is not None:
        comando = f'UPDATE COBRADOR SET telefone = "{telefone}" WHERE matricula = "{matricula}";'
        comandoEscrita(comando)
    if nome is not None:
        comando = f'UPDATE COBRADOR SET nome = "{nome}" WHERE matricula = "{matricula}";'
        comandoEscrita(comando)
    if escala is not None:
        comando = f'UPDATE COBRADOR SET escala = "{escala}" WHERE matricula = "{matricula}";'
        comandoEscrita(comando)
        
def deletarCobrador(matricula):
    comando = f'DELETE FROM COBRADOR WHERE matricula="{matricula}";'
    comandoEscrita(comando)

def lerCobradores():
    comando = 'SELECT * FROM COBRADOR;'
    return comandoLeitura(comando)

def atualizarFoto(matricula, caminhoFoto):
    if not os.path.exists(caminhoFoto):
        raise Exception("Arquivo não encontrado")
    
    with open(caminhoFoto, 'rb') as file:
        foto = file.read()

    comando = f'UPDATE cobrador SET foto = %s WHERE matricula = %s;'
    parametros = (foto, matricula)
    comandoEscritaParametros(comando, parametros)