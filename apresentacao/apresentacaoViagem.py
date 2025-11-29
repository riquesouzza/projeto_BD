from persistencia.crudViagem import *

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
                placa = input("Placa do ônibus: ")
                idLinha = input("Código da linha: ")
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
                dado = lerViagem(idv)
                print(f'Motorista: {dado[0][1]}\nCobrador: {dado[0][2]}\nPlaca: {dado[0][3]}\nLinha: {dado[0][4]}\nChegada: {dado[0][5]}\nSaída: {dado[0][6]}\nData: {dado[0][7]}')
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
                deletarViagem(idv)
                print("Deletado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção invalida!")
