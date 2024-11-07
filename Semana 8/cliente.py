class Cliente:
    def __init__(self, nome, numero_da_conta, saldo):
        self.nome = nome
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo <= 0:
            print('Você não tem saldo suficiente para sacar!')
            return

        if self.saldo < valor:
            print('O valor que quer sacar é maior que o saldo!')
            return

        self.saldo -= valor
        print(f'{self.nome} sacou: R${valor} e o saldo é de {self.saldo}')

    def transferir(self, valor, para_cliente):
        if self.saldo <= 0:
            print('Você não tem saldo suficiente para sacar!')
            return

        if self.saldo < valor:
            print('O valor que quer sacar é maior que o saldo!')
            return

        self.sacar(valor)

        para_cliente.depositar(valor)

        print(f'Sucesso! {self.nome} transferiu para {para_cliente.nome} a quantia de: R${valor}')

    def get_saldo(self):
        return self.saldo

    def __str__(self):
        return f'{self.nome} Saldo: {self.saldo}'