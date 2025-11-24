from servicos.servicoMotorista import (
    servico_cadastrar_motorista,
    servico_listar_motoristas,
    servico_editar_motorista,
    servico_deletar_motorista
)


def exibir_motoristas():
    motoristas = servico_listar_motoristas()
    print("\n----- LISTA DE MOTORISTAS -----")
    for m in motoristas:
        print(f"CNH: {m[0]}, Nome: {m[1]}, Telefone: {m[2]}, Jornada: {m[3]}")
    print("---------------------------------\n")


def menu_motorista():
    while True:
        print("\n==== MENU MOTORISTA ====")
        print("1 - Cadastrar motorista")
        print("2 - Listar motoristas")
        print("3 - Editar motorista")
        print("4 - Remover motorista")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                cnh = input("CNH: ")
                nome = input("Nome: ")
                tel = input("Telefone: ")
                jornal = input("Jornada: ")
                servico_cadastrar_motorista(cnh, nome, tel, jornal)
                print("Motorista cadastrado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            exibir_motoristas()

        elif opcao == "3":
            try:
                cnh = input("CNH do motorista: ")
                print("Deixe vazio para manter o valor.")
                nome = input("Novo nome: ") or None
                tel = input("Novo telefone: ") or None
                jornal = input("Nova jornada: ") or None

                servico_editar_motorista(cnh, nome, tel, jornal)
                print("Motorista atualizado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                cnh = input("CNH do motorista: ")
                servico_deletar_motorista(cnh)
                print("Motorista removido!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção invalida!")
