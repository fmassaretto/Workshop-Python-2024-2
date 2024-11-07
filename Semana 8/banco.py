from cliente import Cliente

def principal():
    cliente1 = Cliente('Joao', 12345, 2000.00)
    cliente2 = Cliente('MAria', 54321, 1000.00)

    # print(cliente1.get_saldo())
    # print(cliente2.get_saldo())


    cliente1.sacar(500.00)
    cliente2.depositar(100.00)

    # print(cliente1.get_saldo())
    # print(cliente2.get_saldo())

    cliente1.transferir(900.00, cliente2)
    # print(cliente1.get_saldo())
    # print(cliente2.get_saldo())

    # cliente1.sacar(700.00)
    # cliente1.transferir(900.00, cliente2)
    print(cliente1)
    print(cliente2)




if __name__ == '__main__':
    principal()