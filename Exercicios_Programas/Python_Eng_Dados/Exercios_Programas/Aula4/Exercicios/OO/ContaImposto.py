'''
1. Considere a classe ContaBancaria apresentada no slide. 
Crie uma classe ContaImposto que herda de conta e possui um atributo percentualImposto. 
Esta classe também deve possuir um método calcularImposto() que subtrai do saldo, 
o valor do próprio saldo multiplicado pelo percentual do imposto. Crie um programa 
para criar as instâncias de ContaImposto e utilizar todos 
os métodos das 3 classes (ex.: sacar, depositar, calcularImposto).
'''

from OO.ContaBancaria import ContaBancaria

class ContaImposto (ContaBancaria):

    def __init__(self, numero, agencia, saldo, codigo_tipo, percentualImposto):
        super().__init__(numero, agencia, saldo, codigo_tipo)
        self.percentualImposto = percentualImposto

    def calcularImposto(self):
        return self.saldo - (self.saldo * self.percentualImposto)