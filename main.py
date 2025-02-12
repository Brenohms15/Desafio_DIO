saldo = 0
saques = 0
depositos = 0
saques_realizados = 0

def sacar(saldo, saques, saques_realizados):
    valor = float(input('Saque um valor: '))
    
    if valor > saldo:
        print('Saldo insuficiente!')
    elif valor > 500:
        print('O limite maximo para saque e de R$500,00!')
    else:
        saldo -= valor
        saques += valor
        print('Valor sacado com sucesso!')
    saques_realizados += 1
    return saldo, saques, saques_realizados

def depositar(saldo, depositos):
    valor = float(input('Deposite um valor: '))
    depositos += valor
    saldo += valor
    print('Valor depositado com sucesso!')
    return saldo, depositos

def extrato(saldo, saques, depositos):
    print(f'Depositos: R${depositos:,.2f}')
    print(f'Saques: R${saques:,.2f}')
    print()
    print(f'Saldo: R${saldo:,.2f}')

while True:
    operacao = input(
    '''O que você deseja fazer? 
    s: sacar
    d: depositar
    e: extrato
    q: sair 
    '''
    )

    match operacao:
        case 's':
            if saques_realizados < 3:
                saldo, saques, saques_realizados = sacar(saldo, saques, saques_realizados)
            else:
                print('Voce atingiu o limite de saques por hoje!')
        case 'd':
            saldo, depositos = depositar(saldo, depositos)
        case 'e':
            extrato(saldo, saques, depositos)
        case 'q':
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida, tente novamente!")
