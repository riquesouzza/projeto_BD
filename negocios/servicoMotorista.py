from persistencia.crudMotorista import (
    cadastrar_motorista,
    listar_motoristas,
    editar_motorista,
    deletar_motorista
)




# SERVICOS

def servico_cadastrar_motorista(cnh, nome, telefone,jornada):
  
    cadastrar_motorista(cnh, nome, telefone,jornada)


def servico_listar_motoristas():
    return listar_motoristas()


def servico_editar_motorista(cnh, nome=None, telefone=None,jornada=None):
    
    editar_motorista(cnh, nome, telefone,jornada)


def servico_deletar_motorista(cnh):
 
    deletar_motorista(cnh)
