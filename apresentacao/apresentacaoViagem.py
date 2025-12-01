from persistencia.crudViagem import *
from persistencia import *

def menuViagem():
    while True:
        print("\n==== MENU VIAGEM ====")
        print("1 - Cadastrar Viagem")
        print("2 - Listar Viagens")
        print("3 - Buscar Viagem")
        print("4 - Editar Viagem")
        print("5 - Remover Viagem")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                motorista = input("Motorista (CNH): ")
                cobrador = input("Cobrador (Matricula): ")
                temp = lerCobrador(cobrador)
                placa = input("Placa do ônibus: ")
                temp = ler_onibus(placa)
                idLinha = input("Código da linha: ")
                temp = ler_linha(idLinha)
                horaChegada = input("Hora de chegada (HH:MM:SS): ")
                horaSaida = input("Hora de saída (HH:MM:SS): ")
                data = input("Data (AAAA-MM-DD): ")
                criarViagem(motorista, cobrador, placa, idLinha, horaChegada, horaSaida, data)
                print("Viagem cadastrada!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            try:
                viagens = lerViagens()
                for v in viagens:
                    print(f'ID: {v[0]} Motorista: {v[1]} Cobrador: {v[2]} Placa: {v[3]} Linha: {v[4]} Chegada: {v[5]} Saída: {v[6]} Data: {v[7]}')
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "3":
            try:
                idv = input("Digite o ID da viagem: ")
                viagem = lerViagem(idv)

                if not viagem:
                    print("Nenhuma viagem encontrada.")
                else:
                    v = viagem[0]
                    print("\n=== DADOS DA VIAGEM ===")
                    print(f"ID: {v[0]}")
                    print(f"Data: {v[1]}")
                    print(f"Saída: {v[2]}")
                    print(f"Chegada: {v[3]}")

                    print("\n=== DADOS DO MOTORISTA / COBRADOR ===")
                    print(f"Motorista: {v[4]}")
                    print(f"Cobrador: {v[5] if v[5] else '— Sem Cobrador —'}")

                    print("\n=== ÔNIBUS E LINHA ===")
                    print(f"Placa do Ônibus: {v[6]}")
                    print(f"Linha: {v[7]}")

                    print("\n=== PASSAGEIROS ===")
                    print(f"Quantidade: {v[8]}")

                    nomes_passageiros = v[9]

                    if nomes_passageiros:
                        nomes = nomes_passageiros.split(", ")
                        for nome in nomes:
                            print(f"- {nome}")
                    else:
                        print("Nenhum passageiro registrado.")

            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                idv = input("Digite o ID da viagem: ")
                print("Caso deseje manter o valor deixe o espaço em branco!")
                motorista = input("Novo motorista: ") or None
                cobrador = input("Novo cobrador: ") or None
                placa = input("Nova placa: ") or None
                idLinha = input("Nova linha: ") or None
                horaChegada = input("Nova hora de chegada: ") or None
                horaSaida = input("Nova hora de saída: ") or None
                data = input("Nova data: ") or None
                editarViagem(idv, motorista, cobrador, placa, idLinha, horaChegada, horaSaida, data)
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "5":
            try:
                idv = input("ID da viagem: ")
                lerViagem(idv)
                deletarViagem(idv)
                print("Deletado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção invalida!")
