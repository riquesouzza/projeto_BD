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
    try:
        cursor.execute(comando)
        conexao.commit()

    except Exception as e:
        if e.errno == 1451 or e.errno == 1217:
            raise Exception(
                "Não é possível excluir/alterar porque existem dados associados a essa informação, apague-os primeiro."
            ) from e

        if e.errno == 1452 or e.errno == 1216:
            raise Exception(
                "Você tentou inserir/alterar um valor que não existe."
            ) from e
    
    finally:
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
    if resultado:
        return resultado
    raise Exception("Não foi possivel encontrar dado!")