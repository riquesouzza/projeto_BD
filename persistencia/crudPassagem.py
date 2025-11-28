from connector import *

# LISTAR TODAS AS PASSAGENS
def listar_passagens():
    comando = 'SELECT * FROM passagem'
    return comandoLeitura(comando)

# CADASTRAR PASSAGEM
def cadastrar_passagem(id_passagem, num_cartao, valor, data_hora, id_viagem):
    comando = (
        f'INSERT INTO passagem (id, numCartao, valor, dataHora, idViagem) '
        f'VALUES ({id_passagem}, {num_cartao}, {valor}, "{data_hora}", {id_viagem})'
    )
    comandoEscrita(comando)

# LER UMA PASSAGEM PELO ID
def ler_passagem(id_passagem):
    comando = f'SELECT * FROM passagem WHERE id = {id_passagem}'
    return comandoLeitura(comando)

# EDITAR PASSAGEM
def editar_passagem(id_passagem, num_cartao=None, valor=None, data_hora=None, id_viagem=None):
    if num_cartao is not None:
        comando = f'UPDATE passagem SET numCartao = {num_cartao} WHERE id = {id_passagem}'
        comandoEscrita(comando)
    if valor is not None:
        comando = f'UPDATE passagem SET valor = {valor} WHERE id = {id_passagem}'
        comandoEscrita(comando)
    if data_hora is not None:
        comando = f'UPDATE passagem SET dataHora = "{data_hora}" WHERE id = {id_passagem}'
        comandoEscrita(comando)
    if id_viagem is not None:
        comando = f'UPDATE passagem SET idViagem = {id_viagem} WHERE id = {id_passagem}'
        comandoEscrita(comando)

# DELETAR PASSAGEM
def deletar_passagem(id_passagem):
    comando = f'DELETE FROM passagem WHERE id = {id_passagem}'
    comandoEscrita(comando)
