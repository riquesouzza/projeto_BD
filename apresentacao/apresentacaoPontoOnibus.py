from persistencia.crudPontoOnibus import *

def menuPontoOnibus():
    while True:
        print("\n==== MENU PONTO DE ÔNIBUS ====")
        print("1 - Cadastrar Ponto")
        print("2 - Listar Pontos")
        print("3 - Buscar Ponto")
        print("4 - Editar Ponto")
        print("5 - Remover Ponto")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                endereco = input("Endereço: ")
                criarPontoOnibus(endereco)
                print("Ponto cadastrado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            try:
                pontos = lerPontosOnibus()
                for p in pontos:
                    print(f'Código: {p[0]} Endereço: {p[1]}')
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "3":
            try:
                idp = input("Código do ponto: ")
                dado = lerPontoOnibus(idp)
                print(f'Endereço: {dado[0][0]}')
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                idp = input("Código do ponto: ")
                temp = lerPontoOnibus(idp)
                print("Caso deseje manter o valor deixe o espaço em branco!")
                endereco = input("Novo endereço: ") or None
                if endereco is not None:
                    editarPontoOnibus(idp, endereco)
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "5":
            try:
                idp = input("Código do ponto: ")
                deletarPontoOnibus(idp)
                print("Deletado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")