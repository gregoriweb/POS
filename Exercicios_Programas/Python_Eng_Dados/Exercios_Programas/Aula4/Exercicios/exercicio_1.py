'''
1. Considere a classe Conta  (Links para um site externo.)apresentada no slide. 
Crie uma classe ContaImposto que herda de conta e possui um atributo percentualImposto. 
Esta classe também deve possuir um método calcularImposto() que subtrai do saldo, 
o valor do próprio saldo multiplicado pelo percentual do imposto. Crie um programa 
para criar as instâncias de ContaImposto e utilizar todos 
os métodos das 3 classes (ex.: sacar, depositar, calcularImposto).
'''

from OO.ContaImposto import ContaImposto

conta = ContaImposto(1001,3445, 50000, "01", 0.1)
conta.depositar(2000)
conta.sacar(1000)
conta.calcularImposto()

print ("saldo sem imposto:" + str(conta.saldo))
print ("saldo saldo descontado imposto de " + str(conta.percentualImposto) + ": " + str(conta.calcularImposto()))




