from apresentacao import *

#colocar os que tem linha para o menu de linha

def menuPrincipal():
    while True:
        print("\n==== SISTEMA DE GERENCIAMENTO ====")
        print("1 - Empresa")
        print("2 - Cobrador")
        print("3 - Motorista")
        print("4 - Passageiro")
        print("5 - Ponto de Ônibus")
        print("6 - Pontos da Linha")
        print("7 - Horários da Linha")
        print("8 - Viagem")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            menuEmpresa()
        elif opcao == "2":
            menuCobrador()
        elif opcao == "3":
            menu_motorista()
        elif opcao == "4":
            menu_passageiro()
        elif opcao == "5":
            menuPontoOnibus()
        elif opcao == "6":
            menuLinhaPontos()
        elif opcao == "7":
            menuHorariosLinha()
        elif opcao == "8":
            menuViagem()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
