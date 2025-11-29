from persistencia.crudEmpresa import *

def menuEmpresa():
    while True:
        print("\n==== MENU EMPRESA ====")
        print("1 - Cadastrar Empresa")
        print("2 - Listar Empresas")
        print("3 - Buscar Empresa")
        print("4 - Editar Empresa")
        print("5 - Remover Empresa")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                cnpj = input("Cnpj: ")
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                endereco = input("Endereço: ")
                criarEmpresa(cnpj, telefone, nome, endereco)
                print("Empresa cadastrado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            try:
                Empresas = lerEmpresas()
                for Empresa in Empresas:
                    print(f'Cnpj: {Empresa[0]} Nome: {Empresa[1]} Telefone: {Empresa[2]} endereco: {Empresa[3]}')
            except Exception as erro:
                print(f'Erro: {erro}')

        elif opcao == "3":
            try:
                cnpj = input("Digite a Cnpj: ")
                dado = lerEmpresa(cnpj)
                print(f'Nome: {dado[0][2]}\nTelefone: {dado[0][1]}\nendereco: {dado[0][3]}')
            except Exception as erro:
                print(f'Erro: {erro}')

        elif opcao == "4":
            try:
                cnpj = input("Digite a Cnpj da Empresa: ")
                print("Caso deseje manter o valor deixe o espaço em branco!")
                nome = input("Novo nome: ") or None
                telefone = input("Novo telefone: ") or None
                endereco = input("Nova endereco: ") or None
                editarEmpresa(cnpj, telefone, nome, endereco)
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "5":
            try:
                cnpj = input("Digite o Cnpj da empresa a ser deletado: ")
                deletarEmpresa(cnpj)
                print("Deletado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção invalida!")