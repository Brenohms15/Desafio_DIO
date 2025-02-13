import datetime

saldo = 0
saques = 0
depositos = 0
saques_realizados = 0
transacoes = []
transacoes_realizadas = 0

#=========================Sacar============================

def sacar(saldo, saques, saques_realizados, transacoes, transacoes_realizadas):
    valor = float(input('Saque um valor: '))
    
    if valor > saldo:
        print('Saldo insuficiente!')
    elif valor > 500:
        print('O limite máximo para saque é de R$500,00!')
    else:
        saldo -= valor
        saques += valor
        saques_realizados += 1
        data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        transacoes.append({'tipo': 'Saque', 'valor': -valor, 'data': data})
        print('Valor sacado com sucesso!')
    
    transacoes_realizadas += 1
    return saldo, saques, saques_realizados, transacoes, transacoes_realizadas

    #=========================Depositar============================

def depositar(saldo, depositos, transacoes, transacoes_realizadas):
    valor = float(input('Deposite um valor: '))
    depositos += valor
    saldo += valor
    data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    transacoes.append({'tipo': 'Depósito', 'valor': valor, 'data': data})
    print('Valor depositado com sucesso!')
    
    transacoes_realizadas += 1
    return saldo, depositos, transacoes, transacoes_realizadas

    #=========================Extrato============================

def extrato(saldo, saques, depositos, transacoes):
    print("\n==== EXTRATO ====")
    for transacao in transacoes:
        print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']:,.2f}")
    
    print("\nResumo:")
    print(f"Depósitos: R${depositos:,.2f}")
    print(f"Saques: R${saques:,.2f}")
    print(f"Saldo: R${saldo:,.2f}")
    print("=================\n")

while True:
    operacao = input(
    '''O que você deseja fazer? 
    s: sacar
    d: depositar
    e: extrato
    q: sair 
    '''
    ).strip().lower()

    match operacao:
        case 's':
            if saques_realizados < 3:
                saldo, saques, saques_realizados, transacoes, transacoes_realizadas = sacar(saldo, saques, saques_realizados, transacoes, transacoes_realizadas)
            else:
                print('Você atingiu o limite de saques por hoje!')
        case 'd':
            if transacoes_realizadas < 10:
                saldo, depositos, transacoes, transacoes_realizadas = depositar(saldo, depositos, transacoes, transacoes_realizadas)
            else:
                print('Você atingiu o limite de transacoes por hoje!')
        case 'e':
            extrato(saldo, saques, depositos, transacoes)
        case 'q':
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida, tente novamente!")
