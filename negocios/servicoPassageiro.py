from persistencia.crudPassageiro import (
    cadastrar_passageiro,
    buscar_passageiro,
    listarPassageiros,
    editar_passageiro,
    deletar_passageiro
)

# SERVICOS 

def servico_cadastrar_passageiro(cpf, nome, telefone, email, nascimento):
   
    cadastrar_passageiro(cpf, nome, telefone, email, nascimento)


def servico_listar_passageiros():
    return listarPassageiros()

def servico_buscar_passageiro(cpf):
    return buscar_passageiro(cpf)


def servico_editar_passageiro(cpf, nome=None, telefone=None, email=None, nascimento=None):
    
    editar_passageiro(cpf, nome, telefone, email, nascimento)


def servico_deletar_passageiro(cpf):
   
    deletar_passageiro(cpf)
