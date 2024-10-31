# models.py

class Historico:
    def __init__(self):
        self.transacoes = []

    def registrar(self, descricao):
        from datetime import datetime
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.transacoes.append(f'{data_hora} - {descricao}')

    def mostrar_historico(self):
        print("\n=============== HISTÓRICO ===============")
        if self.transacoes:
            for transacao in self.transacoes:
                print(transacao)
        else:
            print("Nenhuma transação registrada.")
        print("=======================================\n")


class Conta:
    contador_contas = 1  # Inicia contador de contas em 1

    def __init__(self, cliente, saldo=0, limite_diario=500, limite_saques=3):
        self.agencia = "0001"  # Agência fixa
        self.numero_conta = Conta.contador_contas
        Conta.contador_contas += 1
        self.saldo = saldo
        self.movimentacoes = []
        self.numero_saques = 0
        self.limite_diario = limite_diario
        self.limite_saques = limite_saques
        self._cliente = cliente
        self._historico = Historico()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
            self.movimentacoes.append(f'Depósito: R$ {valor:.2f}')
            self._historico.registrar(f'Depósito: R$ {valor:.2f}')
        else:
            print('Valor inválido! O depósito precisa ser positivo.')

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente!')
        elif valor > self.limite_diario:
            print(f'O valor máximo para saque é de R$ {self.limite_diario:.2f} por transação.')
        elif self.numero_saques >= self.limite_saques:
            print('Número máximo de saques diários excedido.')
        else:
            self.saldo -= valor
            self.numero_saques += 1
            self.movimentacoes.append(f'Saque: R$ {valor:.2f}')

    def extrato(self):
        print("\n=============== EXTRATO ===============")
        if self.movimentacoes:
            for movimentacao in self.movimentacoes:
                print(movimentacao)
        else:
            print("Não foram realizadas movimentações.")
        print(f'\nSaldo atual: R$ {self.saldo:.2f}')
        print("=======================================\n")

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco  # Endereço como string
        self.contas = []  # Cliente pode ter múltiplas contas
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco ):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf