from connector import *

def listar_passagens():
    comando = 'SELECT * FROM passagem'
    return comandoLeitura(comando)


def cadastrar_passagem(id_passagem, num_cartao,id_viagem, data_hora):
    comando = f'CALL registrar_passagem({id_passagem}, {num_cartao}, {id_viagem}, "{data_hora}")'
    comandoEscrita(comando)


def ler_passagem(id_passagem):
    comando = f'SELECT * FROM passagem WHERE id = {id_passagem}'
    return comandoLeitura(comando)


def editar_passagem(id_passagem, num_cartao=None, id_viagem=None,  data_hora=None):
    if num_cartao is not None:
        comando = f'UPDATE passagem SET numCartao = {num_cartao} WHERE id = {id_passagem}'
        comandoEscrita(comando)
    if data_hora is not None:
        comando = f'UPDATE passagem SET dataHora = "{data_hora}" WHERE id = {id_passagem}'
        comandoEscrita(comando)
    if id_viagem is not None:
        comando = f'UPDATE passagem SET idViagem = {id_viagem} WHERE id = {id_passagem}'
        comandoEscrita(comando)

def deletar_passagem(id_passagem):
    comando = f'DELETE FROM passagem WHERE id = {id_passagem}'
    comandoEscrita(comando)
