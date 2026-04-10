class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar (self, valor):
        if valor > 0:
            self.__saldo + valor
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
    
    def mostrar_saldo (self):
        print(f"Seu saldo atual é: {self.__saldo}")
    
    def mostrar_titular (self):
        print(f"Correntista: {self.__titular}")

conta = ContaBancaria("Ana")
conta.depositar(5 * 1000)
conta.mostrar_saldo()
conta.mostrar_titular()