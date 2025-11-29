from negocios.servicoOnibus import (
    servico_cadastrar_onibus,
    servico_listar_onibus,
    servico_ler_onibus,
    servico_editar_onibus,
    servico_deletar_onibus
)


def exibir_onibus():
    onibus = servico_listar_onibus()
    print("\n----- LISTA DE ONIBUS -----")
    for o in onibus:
        print(f"Placa: {o[0]}, Capacidade: {o[1]}, Empresa (CNPJ): {o[2]}")
    print("----------------------------\n")


def menu_onibus():
    while True:
        print("\n==== MENU ONIBUS ====")
        print("1 - Cadastrar Onibus")
        print("2 - Listar Onibus")
        print("3 - Buscar Onibus")
        print("4 - Editar Onibus")
        print("5 - Remover Onibus")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        # CREATE
        if opcao == "1":
            try:
                placa = input("Placa do onibus: ")
                capacidade = input("Capacidade: ")
                id_empresa = input("CNPJ da empresa responsavel: ")
                servico_cadastrar_onibus(placa, capacidade, id_empresa)
                print("Onibus cadastrado com sucesso!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # READ – LISTAR
        elif opcao == "2":
            exibir_onibus()

        # READ – BUSCAR
        elif opcao == "3":
            try:
                placa = input("Digite a placa do onibus: ")
                dados = servico_ler_onibus(placa)
                if dados:
                    o = dados[0]
                    print(f"\nPlaca: {o[0]}\nCapacidade: {o[1]}\nEmpresa (CNPJ): {o[2]}")
                else:
                    print("Onibus nao encontrado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # UPDATE
        elif opcao == "4":
            try:
                placa = input("Placa do onibus para editar: ")
                print("Deixe vazio para manter o valor atual")

                nova_capacidade = input("Nova capacidade (opcional): ") or None
                novo_id_empresa = input("Novo CNPJ da empresa (opcional): ") or None

                servico_editar_onibus(placa, nova_capacidade, novo_id_empresa)
                print("Onibus atualizado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # DELETE
        elif opcao == "5":
            try:
                placa = input("Placa do onibus para remover: ")
                servico_deletar_onibus(placa)
                print("Onibus removido!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # VOLTAR
        elif opcao == "0":
            break

        else:
            print("Opcao invalida!")
