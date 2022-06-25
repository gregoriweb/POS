'''
1. Considere a classe ContaBancaria apresentada no slide. 
Crie uma classe ContaImposto que herda de conta e possui um atributo percentualImposto. 
Esta classe também deve possuir um método calcularImposto() que subtrai do saldo, 
o valor do próprio saldo multiplicado pelo percentual do imposto. Crie um programa 
para criar as instâncias de ContaImposto e utilizar todos 
os métodos das 3 classes (ex.: sacar, depositar, calcularImposto).
'''

class ContaBancaria:
    numero = "00000-0"
    agencia = "0000-0"
    saldo = 0.0
    codigo_tipo = "01" #01 = Conta Corrente, 02 = Poupança
    nome_tipo = ""

    def __init__(self, numero, agencia, saldo, codigo_tipo):
        if (self.validaTipo(codigo_tipo) == True):
            self.numero = numero
            self.agencia = agencia
            self.saldo = saldo
            self.codigo_tipo = codigo_tipo
            if (self.codigo_tipo == "01"):
                self.nome_tipo = "Conta Corrente"
            else:
                self.nome_tipo = "Poupança"
        else:
            print("Tipo de conta inválida: escolha Conta Corrente ou Poupança")

    def validaTipo(self, codigo_tipo):
        if (codigo_tipo == "01" or codigo_tipo == "02"):
            return True
        else:
            return False

    def mostrarSaldo(self):
        print(self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")