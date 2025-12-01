from persistencia. crudViagem import lerViagem
from persistencia. crudCartao import ler_cartao
from negocios.servicoPassagem import (
    servico_cadastrar_passagem,
    servico_listar_passagens,
    servico_ler_passagem,
    servico_editar_passagem,
    servico_deletar_passagem
)


def exibir_passagens():
    passagens = servico_listar_passagens()
    print("\n----- LISTA DE PASSAGENS -----")
    for p in passagens:
        print(f"ID: {p[0]}, Cartao ID: {p[1]}, Valor: R$ {p[2]}, Data/Hora: {p[3]}, Viagem ID: {p[4]}")
    print("--------------------------------\n")


def menu_passagem():
    while True:
        print("\n==== MENU PASSAGEM ====")
        print("1 - Cadastrar Passagem")
        print("2 - Listar Passagens")
        print("3 - Buscar Passagem")
        print("4 - Editar Passagem")
        print("5 - Remover Passagem")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        # CREATE
        if opcao == "1":
            try:
                idp = input("ID da passagem: ")
                num_cartao = input("ID do cartao: ")
                temp = ler_cartao(num_cartao)
                data_hora = input("Data e hora (AAAA-MM-DD HH:MM:SS): ")
                id_viagem = input("ID da viagem: ")
                temp = lerViagem(id_viagem)
                servico_cadastrar_passagem(idp, num_cartao, id_viagem, data_hora)
                print("Passagem cadastrada com sucesso!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # READ – LISTAR
        elif opcao == "2":
            exibir_passagens()

        # READ – BUSCAR
        elif opcao == "3":
            try:
                idp = input("Digite o ID da passagem: ")
                dados = servico_ler_passagem(idp)
                if dados:
                    p = dados[0]
                    print(f"\nID: {p[0]}\nCartao ID: {p[1]}\nValor: R$ {p[2]}\nData/Hora: {p[3]}\nViagem ID: {p[4]}")
                else:
                    print("Passagem nao encontrada!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # UPDATE
        elif opcao == "4":
            try:
                idp = input("ID da passagem que deseja editar: ")
                print("Deixe vazio para manter o valor atual")

                num_cartao = input("Novo ID do cartao (opcional): ") or None
                data_hora = input("Nova data/hora (opcional): ") or None
                id_viagem = input("Novo ID da viagem (opcional): ") or None

                servico_editar_passagem(idp, num_cartao, id_viagem, data_hora)
                print("Passagem atualizada!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # DELETE
        elif opcao == "5":
            try:
                idp = input("ID da passagem que deseja remover: ")
                servico_deletar_passagem(idp)
                print("Passagem removida!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # SAIR
        elif opcao == "0":
            break

        else:
            print("Opcao invalida!")
