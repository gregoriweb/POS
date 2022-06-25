'''
2. Crie uma classe chamada Ingresso, que possui um valor em reais e um método imprimirValor(). 
Crie uma classe IngressoVIP, que herda de Ingresso e possui um valor adicional. 
Crie um método que retorne o valor do ingresso VIP (com o adicional incluído). 
Crie um programa para criar as instâncias de Ingresso e IngressoVIP, mostrando a diferença de preços.
'''

from OO.Ingresso import Ingresso


class IngressoVIP(Ingresso):

    def __init__(self) -> None:
        super().__init__()
        self.valorAdicional = 10
    
    def valorIngressoVip(self):
        return self.valorReais + self.valorAdicional
