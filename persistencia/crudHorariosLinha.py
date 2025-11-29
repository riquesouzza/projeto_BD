from connector import *

def criarHorarioLinha(idLinha, horario):
    comando = f'INSERT INTO horariosLinha (idLinha, horario) VALUES ("{idLinha}", "{horario}")'
    comandoEscrita(comando)

def lerHorarioLinha(idLinha):
    comando = f'SELECT * FROM horariosLinha WHERE idLinha = {idLinha};'
    return comandoLeitura(comando)

def editarHorarioLinha(idLinha, horarioAntigo, novoHorario):
    comando = f'UPDATE horariosLinha SET horario = "{novoHorario}" WHERE idLinha = {idLinha} AND horario = "{horarioAntigo}"'
    comandoEscrita(comando)

def deletarHorarioLinha(idLinha, horario):
    comando = f'DELETE FROM horariosLinha WHERE idLinha = {idLinha} AND horario = "{horario}"'
    comandoEscrita(comando)

def lerHorariosLinha():
    comando = 'SELECT * FROM horariosLinha'
    return comandoLeitura(comando)