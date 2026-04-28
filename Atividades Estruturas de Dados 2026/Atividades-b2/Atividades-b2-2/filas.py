fila_aluno = []
fila_adm = []


def adicionar():
    print("\n1 - Aluno")
    print("2 - ADM")
    
    opcao = input("Escolha a fila: ")

    nome = input("Nome do arquivo: ")
    paginas = int(input("Quantidade de páginas: "))

    documento = [nome, paginas]

    if opcao == "1":
        fila_aluno.append(documento)
        print("O documento foi adicionado na fila de alunos.")

    elif opcao == "2":
        fila_adm.append(documento)
        print("Documento foi adicionado na fila ADM.")

    else:
        print("Essa opção não é valida!")


def consumir():
    if len(fila_adm) > 0:
        doc = fila_adm.pop(0)
        print("\n ADM:")
        print("Arquivo:", doc[0], "- Páginas:", doc[1])

    elif len(fila_aluno) > 0:
        doc = fila_aluno.pop(0)
        print("\n ALUNO:")
        print("Arquivo:", doc[0], "- Páginas:", doc[1])

    else:
        print("\nFilas vazias!")


def listar():
    print("\nFila ADM:", fila_adm)
    print("Total ADM:", len(fila_adm))

    print("\nFila ALUNO:", fila_aluno)
    print("Total ALUNO:", len(fila_aluno))


while True:
    print("\n===== MENU =====")
    print("1 - Adicionar documento")
    print("2 - Consumir fila")
    print("3 - Listar filas")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        adicionar()

    elif op == "2":
        consumir()

    elif op == "3":
        listar()

    elif op == "0":
        print("Encerrado.")
        break

    else:
        print("Opção inválida!")