import mysql.connector

def conexaoBD():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Dados!951',
        database='projetobd',
    )

def comandoEscrita(comando):
    conexao = conexaoBD()
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def comandoEscritaParametros(comando, parametros):
    conexao = conexaoBD()
    cursor = conexao.cursor()
    cursor.execute(comando, parametros)
    conexao.commit()
    cursor.close()
    conexao.close()

def comandoLeitura(comando):
    conexao = conexaoBD()
    cursor = conexao.cursor()
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado