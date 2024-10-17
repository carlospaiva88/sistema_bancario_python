# main.py

from views import criar_cliente, criar_conta_corrente, selecionar_cliente, operacao_conta

menu_principal = """ 
[c] Criar Cliente
[cc] Criar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu_principal)

    if opcao == 'c':
        criar_cliente()
    elif opcao == 'cc':
        criar_conta_corrente()
    elif opcao in ['d', 's', 'e']:
        cliente = selecionar_cliente()
        if cliente:
            operacao_conta(cliente, opcao)
    elif opcao == 'q':
        print("Saindo...")
        break
    else:
        print("Operação inválida, por favor selecione uma das opções.")
