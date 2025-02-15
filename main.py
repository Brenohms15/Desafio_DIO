from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta._saldo += self.valor
        conta._historico.adicionar_transacao(self)
        print(f"Depósito de R$ {self.valor:.2f} realizado.")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > conta._saldo:
            print("Saldo insuficiente!")
        else:
            conta._saldo -= self.valor
            conta._historico.adicionar_transacao(self)
            print(f"Saque de R$ {self.valor:.2f} realizado.")

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    def retornar_transacoes(self):
        return self._transacoes

class Conta:
    def __init__(self, cliente):
        self._saldo = 100  
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self):
        return self._saldo
    
    @staticmethod
    def nova_conta(cliente):
        print('Conta criada com sucesso')
        return Conta(cliente)

    def sacar(self, valor):
        saque = Saque(valor)
        saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

    def conferir_extrato(self):
        return self._historico.retornar_transacoes()

class ContaCorrente(Conta):
    def __init__(self, cliente, limite=1000, limite_saques=3):
        super().__init__(cliente)
        self.limite = limite
        self.limite_saques = limite_saques

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self._contas = []

    def realizar_transacao(self, transacao):
        if not self._contas:
            print('Você não tem nenhuma conta adicionada.')
            return
        
        conta = self._contas[0]
        transacao.registrar(conta)

    def extrato(self):
        if not self._contas:
            print('Você não tem nenhuma conta para consultar o extrato.')
            return []
        return self._contas[0].conferir_extrato()

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        print("Conta adicionada com sucesso!")

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Criando um cliente e uma variável para controlar saques
cliente = None
saques_realizados = 0

while True:
    operacao = input(
    '''O que você deseja fazer? 
    s: sacar
    d: depositar
    e: extrato
    q: sair
    nc: nova conta 
    nu: novo usuário
    '''
    ).strip().lower()

    match operacao:
        case 's':
            if cliente and saques_realizados < 3:
                valor = float(input('Quanto você deseja sacar: '))
                cliente.realizar_transacao(Saque(valor))
                saques_realizados += 1
            else:
                print('Você atingiu o limite de saques por hoje ou não tem uma conta!')

        case 'd':
            if cliente:
                valor = float(input('Quanto você deseja depositar: '))
                cliente.realizar_transacao(Deposito(valor))
            else:
                print("Você precisa criar um usuário primeiro.")

        case 'e':
            if cliente:
                print("\n==== EXTRATO ====")
                for transacao in cliente.extrato():
                    tipo = "Depósito" if isinstance(transacao, Deposito) else "Saque"
                    print(f"{tipo}: R$ {transacao.valor:.2f}")
                print("=================\n")
            else:
                print("Você precisa criar um usuário primeiro.")

        case 'nc':        
            if cliente:
                conta = Conta.nova_conta(cliente)
                cliente.adicionar_conta(conta)
            else:
                print("Você precisa criar um usuário primeiro.")

        case 'nu':
            endereco = input("Digite seu endereço: ")
            cpf = input("Digite seu CPF: ")
            nome = input("Digite seu nome: ")
            data_nascimento = datetime.strptime(input("Digite sua data de nascimento (dd/mm/aaaa): "), '%d/%m/%Y')

            cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
            print("Usuário criado com sucesso!")

        case 'q':
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida, tente novamente!")
