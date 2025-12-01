from persistencia.crudHorariosLinha import *
from persistencia. crudLinha import ler_linha

def menuHorariosLinha():
    while True:
        print("\n==== MENU HORÁRIOS DA LINHA ====")
        print("1 - Cadastrar Horário")
        print("2 - Listar Horários")
        print("3 - Editar Horário")
        print("4 - Remover Horário")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                idLinha = input("Código da linha: ")
                temp=ler_linha(idLinha)
                horario = input("Horário (HH:MM:SS): ")
                criarHorarioLinha(idLinha, horario)
                print("Horário cadastrado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            try:
                idLinha = input("Código da linha: ")
                dado = lerHorarioLinha(idLinha)
                for h in dado:
                    print(f'Horário: {h[1]}')
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "3":
            try:
                idLinha = input("Código da linha: ")
                horarioAntigo = input("Horário atual (HH:MM:SS): ")
                novoHorario = input("Novo horário: ")
                editarHorarioLinha(idLinha, horarioAntigo, novoHorario)
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                idLinha = input("Código da linha: ")
                horario = input("Horário (HH:MM:SS): ")
                deletarHorarioLinha(idLinha, horario)
                print("Deletado!")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")