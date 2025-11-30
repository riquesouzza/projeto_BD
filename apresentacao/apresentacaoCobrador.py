from negocios.servicoCobrador import *
from PIL import Image
import tempfile

def menuCobrador():
    while True:
        print("\n==== MENU COBRADOR ====")
        print("1 - Cadastrar cobrador")
        print("2 - Listar cobradores")
        print("3 - Buscar cobrador")
        print("4 - Editar dados do cobrador")
        print("5 - Remover cobrador")
        print("6 - Atualizar foto do cobrador")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                matricula = input("matricula: ")
                nome = input("nome: ")
                telefone = input("telefone: ")
                escala = input("Jornada: ")
                cadastrarCobrador(matricula, telefone, nome, escala)
                print("cobrador cadastrado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            try:
                cobradores = lerCobradores()
                for cobrador in cobradores:
                    print(f'Matrícula: {cobrador[0]} Nome: {cobrador[1]} Telefone: {cobrador[2]} Escala: {cobrador[3]}')
            except Exception as erro:
                print(f'Erro: {erro}')

        elif opcao == "3":
            try:
                matricula = input("Digite a matrícula: ")
                dado = verCobrador(matricula)
                print(f'Nome: {dado[0][1]}\nTelefone: {dado[0][2]}\nEscala: {dado[0][3]}')
                foto = dado[0][4]
                if foto:
                    mostrarFoto(foto)
                else:
                    print("Cobrador sem foto cadastrada")
            except Exception as erro:
                print(f'Erro: {erro}')

        elif opcao == "4":
            try:
                matricula = input("Digite a matrícula do cobrador: ")
                print("Caso deseje manter o valor deixe o espaço em branco!")
                nome = input("Novo nome: ") or None
                telefone = input("Novo telefone: ") or None
                escala = input("Nova escala: ") or None
                editarCobrador(matricula, telefone, nome, escala)
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "5":
            try:
                matricula = input("Digite a matrícula do funcionario a ser deletado: ")
                deletarCobrador(matricula)
                print("Deletado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "6":
            try:
                matricula = input("Digite a matrícula do cobrador: ")
                caminhoFoto = input("Digite o caminho absoluto até a foto: ")
                atualizarFoto(matricula, caminhoFoto)
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção invalida!")

def mostrarFoto(foto_data):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpeg') as temp_file:
        temp_file.write(foto_data)
        temp_path = temp_file.name
    img = Image.open(temp_path)
    img.verify()
    img = Image.open(temp_path)
    img.show()