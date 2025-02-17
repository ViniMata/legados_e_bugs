class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def transferir(self, valor, destino):
        if valor <=0:
            print("O valor da transferência precisa ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente para transferência.")
        else:
            self.saldo -= valor
            destino.saldo += valor
            print(f"Transferência de R${valor:.2f} para {destino.titular} realizada com sucesso.")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

# Exemplo de uso
if __name__ == "__main__":
    conta1 = ContaBancaria("Alice", 1000)
    conta2 = ContaBancaria("Bob", 500)

    conta1.depositar(200)
    conta1.sacar(150)
    conta1.transferir(300, conta2)
    conta1.exibir_saldo()
    conta2.exibir_saldo()
