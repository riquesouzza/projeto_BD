from negocios.servicoPassageiro import (
    servico_cadastrar_passageiro,
    servico_listar_passageiros,
    servico_editar_passageiro,
    servico_deletar_passageiro
)


def exibir_passageiros():
    passageiros = servico_listar_passageiros()
    print("\n----- LISTA DE PASSAGEIROS -----")
    for p in passageiros:
        print(f"CPF: {p[0]}, Nome: {p[1]}, Telefone: {p[2]}, Email: {p[3]}, Nascimento: {p[4]}")
    print("----------------------------------\n")


def menu_passageiro():
    while True:
        print("\n==== MENU PASSAGEIRO ====")
        print("1 - Cadastrar passageiro")
        print("2 - Listar passageiros")
        print("3 - Editar passageiro")
        print("4 - Remover passageiro")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                cpf = input("CPF: ")
                nome = input("Nome: ")
                tel = input("Telefone: ")
                email = input("Email: ")
                nasc = input("Data de nascimento (AAAA-MM-DD): ")
                servico_cadastrar_passageiro(cpf, nome, tel, email, nasc)
                print("Passageiro cadastrado com sucesso!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            exibir_passageiros()

        elif opcao == "3":
            try:
                cpf = input("CPF do passageiro: ")
                print("Deixe vazio para nao alterar.")
                nome = input("Novo nome: ") or None
                tel = input("Novo telefone: ") or None
                email = input("Novo email: ") or None
                nasc = input("Nova data nascimento: ") or None

                servico_editar_passageiro(cpf, nome, tel, email, nasc)
                print("Passageiro atualizado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                cpf = input("CPF do passageiro para deletar: ")
                servico_deletar_passageiro(cpf)
                print("Passageiro removido com sucesso!")
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "0":
            break

        else:
            print("Opção invalida!")
