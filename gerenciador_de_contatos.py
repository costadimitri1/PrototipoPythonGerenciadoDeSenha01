contatos = {} # dicionario com contatos

def adicionar_contato():
    nome = input("Digite o nome do contato: ").strip().lower()
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")

    if nome in contatos:
        print("contato ja existe !")
    else:
        contatos[nome] = {"telefone": telefone, "email": email}
        print(f"✅ Contato '{nome}' adicionado com sucesso")

def buscar_contato():
    nome = input("Digite o nome do contato: ").strip().lower()
    if nome in contatos:
        print(f"Nome: {nome.capitalize}")
        print(f"Telefone: {contatos[nome]['telefone']}")
        print(f"Email: {contatos[nome]["email"]}")
    else:
        print("Contato nao encontrado")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado !")
    else :
        for nome, info in contatos.items():
            print(f"Nome: {nome}, Telefone: {info['telefone']}, Email: {info['email']}")

def remover_contatos():
    nome = input("Digite o nome da qual deseja remover dos contatos: ").strip().lower()
    if nome in contatos:
        del contatos[nome]
        print(f"O contato {nome} foi excluído")
    else:
        print("O nome não está na agenda")


def atualizar_contatos():
    print("CONTATOS NÃO EXISTENTES SERÃO ADICIONADOS COMO NOVOS CONTATOS")
    nome = input("Digite o nome do usuario que deseja atualizar: ").strip().lower()
    telefone = input("Digite o novo numero de telefone")
    email = input("Digite o novo email")
    if nome in contatos:
        contatos[nome] = {"telefone":telefone, "email":email}
        print(f"Contato atualiado com sucesso")
    else:
        contatos[nome] = {"telefone":telefone, "email":email}
        print("O contato não existia previamente , então um novo foi criado")

#Loop principal
while True:
    print("Bem-vindo ao seu gerenciador de contatos ! segue suas funcionalidade")
    print("1 - para adicionar contatos")
    print("2 - para buscar contatos")
    print("3 - para listar contatos")
    print("4 - para remover contatos")
    print("5 - para atualizar contatos")
    print("6 - para terminar o programa")

    num = input("Digite o numero da função desejada")
    if num == "1":
        adicionar_contato()
    elif num =="2":
        buscar_contato()
    elif num =="3":
        listar_contatos()
    elif num =="4":
        remover_contatos()
    elif num =="5":
        atualizar_contatos()
    elif num =="6":
        print("FIM DO PROGRAMA")
        break
    else:
        print("Opção inválida, por favor digite um número de 1 a 6 conforme as opções :")
       