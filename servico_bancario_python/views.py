# views.py

from models import Cliente, Conta

clientes = []
contas = []

def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def criar_cliente():
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF (apenas números): ")

    if buscar_cliente(cpf):
        print("Erro: CPF já cadastrado!")
        return

    endereco = input("Endereço (logradouro, número, bairro, cidade/estado): ")
    novo_cliente = Cliente(nome, data_nascimento, cpf, endereco)
    clientes.append(novo_cliente)
    print(f"Cliente {nome} criado com sucesso!")

def criar_conta_corrente():
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf)
    if cliente:
        nova_conta = Conta(cliente)
        cliente.contas.append(nova_conta)
        contas.append(nova_conta)
        print(f"Conta criada com sucesso! Agência: {nova_conta.agencia}, Conta: {nova_conta.numero_conta}")
    else:
        print("Cliente não encontrado!")

def selecionar_cliente():
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf)
    if cliente:
        return cliente
    else:
        print("Cliente não encontrado!")
        return None

def operacao_conta(cliente, operacao):
    if not cliente.contas:
        print("O cliente não possui contas.")
        return
    
    # Para simplicidade, vamos usar a primeira conta da lista
    conta = cliente.contas[0]

    if operacao == 'd':
        valor = float(input("Quanto deseja depositar? "))
        conta.depositar(valor)
    elif operacao == 's':
        valor = float(input("Qual valor deseja sacar? "))
        conta.sacar(valor)
    elif operacao == 'e':
        conta.extrato()
