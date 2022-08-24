#Inicia um dicionario vazio
dicionarioContato = {}

'''
Função utilizada para adicionar contatos.
Pergunta ao usuario quantos contatos vão ser adicionados e os adiciona perguntando o Nome, E-mail, Telefone, Twitter e Istagram.
'''
def adiciona_Contatos():
    numeroContatos = inputNumero("Digite a quantidade de contatos que quer adicionar?  ")
    contador = 1
    while contador <= numeroContatos:
        print()
        nome = input("Digite o nome do contato  ")

        if nome in dicionarioContato:
            print("-----------------------------------")
            print("Nome de contato ja cadastrado")
            print("-----------------------------------\n")
        else:
            email = input("Digite o e-mail do contato  ")
            telefone = input("Digite o telefone do contato  ")
            twitter = input("Digite o Twitter  ")
            insta = input("Digite o Instagram  " )
            dicionarioContato[nome.lower()]=[email.lower(), telefone, twitter.lower(), insta.lower()]
            contador = contador + 1
            print("-----------------------------------")
            print("Contato adicionado com sucesso")
            print("-----------------------------------\n")

'''
Função para pesquisar contatos na agenda.
Dado um nome, a função retorna todos os contatos com aquele nome.
'''
def pesquisa_Contato():
    if not dicionarioContato:
        print("-----------------------------------")
        print("Lista de contatos vazia")
        print("-----------------------------------\n")
    else:
        procuraContato = input("Digite o nome do contato  ")
        encontrado = False

        for item in dicionarioContato.keys():
            if procuraContato.lower() in item:
                encontrado = True
                print("-----------------------------------")
                print(item, dicionarioContato[item])
                print("-----------------------------------\n")

        if not encontrado:
            print("-----------------------------------")
            print("Contato não encontrado")
            print("-----------------------------------\n")

'''
Função para deletar contatos da agenda.
Dado um nome, a função retorna uma lista com todos os contatos com aquele nome e então o usuario escolhe qual contato quer excluir.
'''
def deleta_Contato():
    if not dicionarioContato:
        print("-----------------------------------")
        print("Lista de contatos vazia")
        print("-----------------------------------\n")
    else:
        nomeContato = localiza()
        if nomeContato:
            del dicionarioContato[nomeContato]
            print("-----------------------------------")
            print("Contato excluido com sucesso")
            print("-----------------------------------\n")


'''
Função para procurar e devolver lista de contatos a partir de nome digitado
'''
def localiza():
    nome = input("Digite o nome do contato  \n")
    encontrado = False
    lista = []
    n = 0

    for item in dicionarioContato.keys():
        if nome.lower() in item:
            lista.append(item)

    if not lista:
        print("-----------------------------------")
        print("Contato não encontrado")
        print("-----------------------------------\n")
        nomeContato = ''
    else:
        if len(lista) > 1:
            n = 1
            for item in lista:
                print(n, item)
                n += 1

            registro = int(input("Digite o número do registro \n"))
            nomeContato = lista[registro - 1]
        else:
            nomeContato = lista[0]

    return nomeContato

'''
Função para atualizar contatos da agenda.
Dado um nome, a função retorna uma lista com todos os contatos com aquele nome e então o usuario escolhe qual contato quer atualizar.
'''
def atualiza_Contato():
    if not dicionarioContato:
        print("-----------------------------------")
        print("Lista de contatos vazia")
        print("-----------------------------------\n")
    else:
        nomeContato = localiza()
        if nomeContato:
            email = input("Digite o novo e-mail  ")
            telefone = input("Digite o novo telefone  ")
            twitter = input("Digite o novo Twitter  ")
            insta = input("Digite o novo Instagram  " )
            dicionarioContato[nomeContato]=[email.lower(), telefone.lower(), twitter.lower(), insta.lower()]

            print("-----------------------------------")
            print("Contato atualizado com sucesso\n")
            print("-----------------------------------\n")

'''
Função para listar contatos.
A função devolve uma tabela com todos os contatos.
'''
def listar_Contatos():
    print("Nro\t Nome\t\t E-mail\t\t\t\t Twitter\t  Instagram")
    for i in dicionarioContato.keys():
        numero = list(dicionarioContato).index(i)
        print("{}\t {:<9}\t {:<25}\t {:<9}\t  {:<9}".format(int(numero + 1), i, dicionarioContato[i][0], dicionarioContato[i][2], dicionarioContato[i][3]))
    print()


'''
Função para gerar um backup dos contatos salvando em um arquivo txt 
'''
def backup_Contatos():
    with open('agenda_contato.txt', 'w') as arquivo:
        for item in dicionarioContato.keys():
            arquivo.write("{},{},{},{},{}\n".format(item, dicionarioContato[item][1],dicionarioContato[item][0],dicionarioContato[item][2],dicionarioContato[item][3]))
    with open('agenda_contato.txt', 'r') as arquivo:
        print("-----------------------------------")
        print("Backup de contatos feito com sucesso!!")
        print("-----------------------------------\n")
        print(arquivo.read())


'''
Função de tratamento de erro para devolver apenas numeros
'''
def inputNumero(label):
    while True:
        try:
            opcao = int(input(label))
            break
        except ValueError:
            print("Apenas números são validos")

    return opcao



'''
Função de menu principal da agenda de contatos.
'''
def menuPrincipal():
    continua = True
    while continua:
        print("1 - Adicionar Contato")
        print("2 - Pesquisar Contato")
        print("3 - Atualizar Contato")
        print("4 - Excluir Contato")
        print("5 - Listar Contatos")
        print("6 - Backup Contatos")
        print("7 - Sair\n")

        opcao = inputNumero("Escolha uma opção ")
        if opcao == 7:
            print("-----------------------------------")
            print("Saindo da agenda")
            print("-----------------------------------\n")
            continua = False
        elif opcao == 1:
            adiciona_Contatos()
        elif opcao == 2:
            pesquisa_Contato()
        elif opcao == 3:
            atualiza_Contato()
        elif opcao == 4:
            deleta_Contato()
        elif opcao == 5:
            listar_Contatos()
        elif opcao == 6:
            backup_Contatos()
        else:
            print("-----------------------------------")
            print("Opção invalida. Escolha uma nova opção")
            print("-----------------------------------\n")

menuPrincipal()

