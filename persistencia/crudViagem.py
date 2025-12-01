from connector import *
from persistencia import *

def criarViagem(motorista, cobrador, placa, idLinha, horaChegada, horaSaida, data):
    comando = f'INSERT INTO viagem (motorista, cobrador, placa, idLinha, horaChegada, horaSaida, data) VALUES ("{motorista}", "{cobrador}", "{placa}", "{idLinha}", "{horaChegada}", "{horaSaida}", "{data}")'
    comandoEscrita(comando)

def lerViagem(idv):
    comando = f'SELECT * FROM viagem_envolvidos where idViagem = {idv};'
    return comandoLeitura(comando)

def editarViagem(idv, motorista=None, cobrador=None, placa=None, idLinha=None, horaChegada=None, horaSaida=None, data=None):
    if motorista is not None:
        comando = f'UPDATE viagem SET motorista = "{motorista}" WHERE id = "{idv}"'
        comandoEscrita(comando)
    if cobrador is not None:
        comando = f'UPDATE viagem SET cobrador = "{cobrador}" WHERE id = "{idv}"'
        comandoEscrita(comando)
    if placa is not None:
        comando = f'UPDATE viagem SET placa = "{placa}" WHERE id = "{idv}"'
        comandoEscrita(comando)
    if idLinha is not None:
        comando = f'UPDATE viagem SET idLinha = "{idLinha}" WHERE id = "{idv}"'
        comandoEscrita(comando)
    if horaChegada is not None:
        comando = f'UPDATE viagem SET horaChegada = "{horaChegada}" WHERE id = "{idv}"'
        comandoEscrita(comando)
    if horaSaida is not None:
        comando = f'UPDATE viagem SET horaSaida = "{horaSaida}" WHERE id = "{idv}"'
        comandoEscrita(comando)
    if data is not None:
        comando = f'UPDATE viagem SET data = "{data}" WHERE id = "{idv}"'
        comandoEscrita(comando)

def deletarViagem(idv):
    comando = f'DELETE FROM viagem WHERE id="{idv}"'
    comandoEscrita(comando)

def lerViagens():
    comando = 'SELECT * FROM viagem'
    return comandoLeitura(comando)