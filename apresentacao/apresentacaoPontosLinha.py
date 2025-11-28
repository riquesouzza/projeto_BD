from persistencia.crudLinhaPontos import *

def menuLinhaPontos():
    while True:
        print("\n==== MENU PARADAS POR LINHA ====")
        print("1 - Cadastrar parada na Linha")
        print("2 - Buscar paradas de uma Linha")
        print("3 - Editar parada da Linha")
        print("4 - Remover parada da Linha")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                idLinha = input("Código da linha: ")
                codPonto = input("Código da parada: ")
                criarLinhaPonto(idLinha, codPonto)
                print("Relação cadastrada!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            try:
                idLinha = input("Código da linha: ")
                dados = lerLinhaPontos(idLinha)
                for d in dados:
                    print(f'Ponto: {d[0][1]} Endereço: {d[0][2]}')
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "3":
            try:
                idLinha = input("Código da linha: ")
                codPonto = input("Código atual da parada: ")
                print("Digite o novo codigo da parada: ")
                novoCodPonto = input("Novo código da parada: ")
                editarLinhaPonto(idLinha, codPonto, novoCodPonto)
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                idLinha = input("Código da linha: ")
                codPonto = input("Código do ponto: ")
                deletarLinhaPonto(idLinha, codPonto)
                print("Deletado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")