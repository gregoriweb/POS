'''
2. Crie uma classe chamada Ingresso, que possui um valor em reais e um método imprimirValor(). 
Crie uma classe IngressoVIP, que herda de Ingresso e possui um valor adicional. 
Crie um método que retorne o valor do ingresso VIP (com o adicional incluído). 
Crie um programa para criar as instâncias de Ingresso e IngressoVIP, mostrando a diferença de preços.
'''

from OO.Ingresso import Ingresso
from OO.IngressoVip import IngressoVIP

ingresso = Ingresso()
ingresso.imprimirValor()

ingressoVip = IngressoVIP()
print ("Valor do ingresso Vip: " + str (ingressoVip.valorIngressoVip()))

print ("A diferenção entre os dois ingressos é de: " + str ( ingressoVip.valorIngressoVip() - ingresso.valorReais))




