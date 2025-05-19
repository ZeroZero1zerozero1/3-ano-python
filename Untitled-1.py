class ContaBancaria:
    def __init__(self, titular, saldo_inicial=3500, limite=1500):
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and (self.__saldo: + self.__limite) >= valor:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print(f"Saque de R${valor:.2f} realizado é invalido!")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")    

    def novo_limite(self, novo_limite):
        if novo_limite > 0:
            self.__limite = novo_limite
            print(f"Novo limite definido: R${self.__limite:.2f}")
        else:
            print("O limite deve ser positivo.")

     def __str__(self):
        return (f"Titular: {self.__titular}\n"
                f"Saldo: R${self.__saldo:.2f}\n""
                f"Limite: R${self.__limite:.2f}\n")
    



conta = ContaBancaria("João", 1000)
conta.exibir_saldo()
conta.depositar()
conta.exibir_saldo()
conta.sacar(5000)
conta.depositar(300)
conta.exibir_saldo()
conta.novo_limite(2000)