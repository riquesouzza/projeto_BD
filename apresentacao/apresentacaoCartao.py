from persistencia. crudPassageiro import buscar_passageiro
from negocios.servicoCartao import (
    servico_cadastrar_cartao,
    servico_listar_cartoes,
    servico_ler_cartao,
    servico_editar_cartao,
    servico_deletar_cartao
)


def exibir_cartoes():
    cartoes = servico_listar_cartoes()
    print("\n----- LISTA DE CARTOES -----")
    for c in cartoes:
        print(f"ID: {c[0]}, Usuario (CPF): {c[1]}, Saldo: R$ {c[2]}")
    print("-----------------------------\n")


def menu_cartao():
    while True:
        print("\n==== MENU CARTAO DE TRANSPORTE ====")
        print("1 - Cadastrar Cartao")
        print("2 - Listar Cartoes")
        print("3 - Buscar Cartao")
        print("4 - Editar Cartao")
        print("5 - Remover Cartao")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        # CREATE
        if opcao == "1":
            try:
                idc = input("ID do cartao: ")
                usuario = input("CPF do passageiro dono do cartao: ")
                temp= buscar_passageiro(usuario)
                saldo = input("Saldo inicial: ")
                servico_cadastrar_cartao(idc, usuario, saldo)
                print("Cartao cadastrado com sucesso!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # READ – LISTAR
        elif opcao == "2":
            exibir_cartoes()

        # READ – BUSCAR
        elif opcao == "3":
            try:
                idc = input("Digite o ID do cartao: ")
                dados = servico_ler_cartao(idc)
                if dados:
                    c = dados[0]
                    print(f'\nID: {c[0]}\nUsuario (CPF): {c[1]}\nSaldo: R$ {c[2]}')
                else:
                    print("Cartao nao encontrado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # UPDATE
        elif opcao == "4":
            try:
                idc = input("ID do cartao que deseja editar: ")
                print("Deixe vazio para manter o valor atual")

                novoUsuario = input("Novo CPF do passageiro (opcional): ") or None
                novoSaldo = input("Novo saldo (opcional): ") or None

                servico_editar_cartao(idc, novoUsuario, novoSaldo)
                print("Cartao atualizado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # DELETE
        elif opcao == "5":
            try:
                idc = input("ID do cartao que deseja remover: ")
                servico_deletar_cartao(idc)
                print("Cartao removido!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # SAIR
        elif opcao == "0":
            break

        else:
            print("Opcao invalida!")
