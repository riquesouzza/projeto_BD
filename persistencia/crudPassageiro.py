from connector import *


def listarPassageiros():
    comando = 'SELECT * FROM passageiro'
    return comandoLeitura(comando)



def cadastrar_passageiro(cpf, nome, telefone, email, data_nascimento):
    comando = (
        f'INSERT INTO passageiro (CPF, nome, telefone, email, dataNascimento) '
        f'VALUES ("{cpf}", "{nome}", "{telefone}", "{email}", "{data_nascimento}")'
    )
    comandoEscrita(comando)




def buscar_passageiro(cpf):
    comando = f'SELECT * FROM passageiro WHERE CPF="{cpf}"'
    return comandoLeitura(comando)


def deletar_passageiro(cpf):
    comando = f'DELETE FROM passageiro WHERE CPF="{cpf}"'
    comandoEscrita(comando)



def editar_passageiro(cpf, nome=None, telefone=None, email=None, data_nascimento=None):
    if nome is not None:
        comando = f'UPDATE passageiro SET nome = "{nome}" WHERE CPF = "{cpf}"'
        comandoEscrita(comando)
    if telefone is not None:
        comando = f'UPDATE passageiro SET telefone = "{telefone}" WHERE CPF = "{cpf}"'
        comandoEscrita(comando)
    if email is not None:
        comando = f'UPDATE passageiro SET email = "{email}" WHERE CPF = "{cpf}"'
        comandoEscrita(comando)
    if data_nascimento is not None:
        comando = f'UPDATE passageiro SET dataNascimento = "{data_nascimento}" WHERE CPF = "{cpf}"'
        comandoEscrita(comando)
