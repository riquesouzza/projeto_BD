from connector import *
from .crudPassageiro import buscar_passageiro

# LISTAR CARTOES
def listar_cartoes():
    comando = 'SELECT * FROM cartaoTransporte'
    return comandoLeitura(comando)

# CADASTRA CARTAO
def cadastrar_cartao(id, usuario, saldo):
  
    if not buscar_passageiro(usuario):
        print(f"Erro: Passageiro com CPF {usuario} nao existe.")
        return

    comando = (
        f'INSERT INTO cartaoTransporte (id, Usuario, saldo) '
        f'VALUES ("{id}", "{usuario}", "{saldo}")'
    )
    comandoEscrita(comando)

# LER CARTAO
def ler_cartao(id):
    comando = f'SELECT * FROM cartaoTransporte WHERE id="{id}"'
    return comandoLeitura(comando)

# DELETAR  CARTAO
def deletar_cartao(id):
    comando = f'DELETE FROM cartaoTransporte WHERE id="{id}"'
    comandoEscrita(comando)

# UPDATES CARTAO
def editar_cartao(id, usuario=None, saldo=None):
    # Se alterar usuario, valida se passageiro existe
    if usuario is not None and not buscar_passageiro(usuario):
        print(f"Erro: Passageiro com CPF {usuario} nao existe.")
        return

    if usuario is not None:
        comando = f'UPDATE cartaoTransporte SET Usuario = "{usuario}" WHERE id = "{id}"'
        comandoEscrita(comando)
    if saldo is not None:
        comando = f'UPDATE cartaoTransporte SET saldo = "{saldo}" WHERE id = "{id}"'
        comandoEscrita(comando)
