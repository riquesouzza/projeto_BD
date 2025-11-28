from persistencia.crudCobrador import *

def validarMatricula(s):
    if (len(s) == 4 and s[0] == 'C' and s[1:].isdigit()):
        return
    raise Exception("Matrícula inválida!") 

def cadastrarCobrador(matricula, telefone, nome, escala):
    criarCobrador(matricula, telefone, nome, escala)

def listarCobradores():
    return lerCobradores()

def verCobrador(matricula):
    return lerCobrador(matricula)

def editarCobrador(matricula, telefone=None, nome=None, escala=None): 
    atualizarCobrador(matricula, telefone, nome, escala)


def apagarCobrador(matricula):
    apagarCobrador(matricula)