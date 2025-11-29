from connector import *

def criarLinhaPonto(idLinha, codPonto):
    comando = f'INSERT INTO linhaPontos (idLinha, codPonto) VALUES ("{idLinha}", "{codPonto}")'
    comandoEscrita(comando)

def lerLinhaPontos(idLinha):
    comando = f'SELECT linhapontos.codPonto, endereco FROM linhaPontos JOIN pontoonibus on linhapontos.codPonto = pontoonibus.codPonto WHERE idLinha = "{idLinha}";'
    return comandoLeitura(comando)

def editarLinhaPonto(idLinha, codPontoAntigo, codPontoNovo):
    comando = f'UPDATE linhaPontos SET codPonto = "{codPontoNovo}" WHERE idLinha = {idLinha} AND codPonto = "{codPontoAntigo}"'
    comandoEscrita(comando)

def deletarLinhaPonto(idLinha, codPonto):
    comando = f'DELETE FROM linhaPontos WHERE idLinha = {idLinha} AND codPonto = "{codPonto}"'
    comandoEscrita(comando)

def lerLinhasPontos():
    comando = 'SELECT * FROM linhaPontos'
    return comandoLeitura(comando)