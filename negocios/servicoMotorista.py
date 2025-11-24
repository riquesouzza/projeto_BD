from persistencia.crudMotorista import (
    cadastrar_motorista,
    listar_motoristas,
    editar_motorista,
    deletar_motorista
)




# SERVICOS

def servico_cadastrar_motorista(cnh, nome, telefone):
  
    cadastrar_motorista(cnh, nome, telefone)


def servico_listar_motoristas():
    return listar_motoristas()


def servico_editar_motorista(cnh, nome=None, telefone=None):
    
    editar_motorista(cnh, nome, telefone)


def servico_deletar_motorista(cnh):
 
    deletar_motorista(cnh)