from apresentacao import *

def menuPrincipal():
    while True:
        print("\n==== SISTEMA DE GERENCIAMENTO ====")
        print("1 - Empresa")
        print("2 - Cobrador")
        print("3 - Motorista")
        print("4 - Passageiro")
        print("5 - Ponto de Onibus")
        print("6 - Viagem")
        print("7 - Cartao de Transporte")
        print("8 - Linha")
        print("9 - Onibus")
        print("10 - Passagem")
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
            menuViagem()
        elif opcao == "7":
            menu_cartao()
        elif opcao == "8":
            menu_linha() 
        elif opcao == "9":
            menu_onibus()
        elif opcao == "10":
            menu_passagem()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")
