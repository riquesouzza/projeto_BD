from negocios.servicoLinha import (
    servico_cadastrar_linha,
    servico_listar_linhas,
    servico_ler_linha,
    servico_editar_linha,
    servico_deletar_linha
)
from .apresentacaoPontosLinha import menuLinhaPontos  # supondo que você tenha esse menu
from .apresentacaoHorarioLinha import menuHorariosLinha  # supondo que você tenha esse menu

def exibir_linhas():
    linhas = servico_listar_linhas()
    print("\n----- LISTA DE LINHAS -----")
    for l in linhas:
        print(f"Codigo: {l[0]}, Empresa (CNPJ): {l[1]}, Nome: {l[2]}")
    print("----------------------------\n")

def menu_linha():
    while True:
        print("\n==== MENU LINHA ====")
        print("1 - Cadastrar Linha")
        print("2 - Listar Linhas")
        print("3 - Buscar Linha")
        print("4 - Editar Linha")
        print("5 - Remover Linha")
        print("6 - Pontos da Linha")
        print("7 - Horarios da Linha")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        # CREATE
        if opcao == "1":
            try:
                cod_linha = input("Codigo da linha: ")
                id_empresa = input("CNPJ da empresa responsavel: ")
                nome = input("Nome da linha: ")
                servico_cadastrar_linha(cod_linha, id_empresa, nome)
                print("Linha cadastrada com sucesso!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # READ – LISTAR
        elif opcao == "2":
            exibir_linhas()

        # READ – BUSCAR
        elif opcao == "3":
            try:
                cod_linha = input("Digite o codigo da linha: ")
                dados = servico_ler_linha(cod_linha)
                if dados:
                    l = dados[0]
                    print(f"\nCodigo: {l[0]}\nEmpresa (CNPJ): {l[1]}\nNome: {l[2]}")
                else:
                    print("Linha nao encontrada!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # UPDATE
        elif opcao == "4":
            try:
                cod_linha = input("Codigo da linha para editar: ")
                print("Deixe vazio para manter o valor atual")
                novo_id_empresa = input("Novo CNPJ da empresa (opcional): ") or None
                novo_nome = input("Novo nome da linha (opcional): ") or None
                servico_editar_linha(cod_linha, novo_id_empresa, novo_nome)
                print("Linha atualizada!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # DELETE
        elif opcao == "5":
            try:
                cod_linha = input("Codigo da linha para remover: ")
                servico_deletar_linha(cod_linha)
                print("Linha removida!")
            except Exception as erro:
                print(f"Erro: {erro}")

        # MENU DE PONTOS
        elif opcao == "6":
            menuLinhaPontos()

        # MENU DE HORARIOS
        elif opcao == "7":
            menuHorariosLinha()

        # VOLTAR
        elif opcao == "0":
            break

        else:
            print("Opcao invalida!")
