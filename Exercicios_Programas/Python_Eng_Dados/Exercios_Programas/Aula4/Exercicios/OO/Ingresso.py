'''
2. Crie uma classe chamada Ingresso, que possui um valor em reais e um método imprimirValor(). 
Crie uma classe IngressoVIP, que herda de Ingresso e possui um valor adicional. 
Crie um método que retorne o valor do ingresso VIP (com o adicional incluído). 
Crie um programa para criar as instâncias de Ingresso e IngressoVIP, mostrando a diferença de preços.
'''

class Ingresso:
    
    def __init__(self) -> None:
        self.valorReais = 35

    def imprimirValor(self):
        print ("Valor do ingresso: " + str(self.valorReais))
