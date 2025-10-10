# Estado da conta
conta = {
    "saldo": 1000.0,
    "historico": []
}

def verSaldo(c):
    print(f"O seu saldo é de R${c['saldo']}")

def addHist(acao, c):
    c["historico"].append(acao)

def verHist(c):
    if not c["historico"]:
        print("Nenhuma transação registrada.")
    else:
        for transacao in c["historico"]:
            print(transacao)

def deposito(c):
    print(f'Saldo atual = {c["saldo"]}')
    qntd = float(input('Qual o valor que deseja depositar?\n> '))
    if qntd <= 0:
        print('Valor inválido')
    else:
        c["saldo"] += qntd
        print(f'Valor atual na conta: {c["saldo"]}')
        addHist(f"Depósito de R${qntd}", c)

def sacar(c):
    print(f'Saldo atual = {c["saldo"]}')
    qntd = float(input('Qual o valor que deseja sacar?\n> '))
    if qntd <= 0:
        print('Valor inválido')
    else:
        if c["saldo"] >= qntd:
            c["saldo"] -= qntd
            print(f'Valor atual na conta: {c["saldo"]}')
            addHist(f"Saque de R${qntd}", c)
        else:
            print('Saldo insuficiente!')

def menu(c):
    while True:
        print('\n== MENU DO CAIXA ELETRÔNICO ==')
        escolha = int(input(
            '1 - Depositar\n'
            '2 - Sacar\n'
            '3 - Ver saldo\n'
            '4 - Ver histórico\n'
            '5 - Sair\n> '
        ))
        if escolha == 1:
            deposito(c)
        elif escolha == 2:
            sacar(c)
        elif escolha == 3:
            verSaldo(c)
        elif escolha == 4:
            verHist(c)
        elif escolha == 5:
            print("Finalizando o sistema.")
            break
        else:
            print("Opção inválida.")

menu(conta)