'''
6) Faca um programa que leia um número n e imprima se ele é primo ou não. (um 
número  primo  tem  apenas  2  divisores:  1  e  ele  mesmo!  O  número  1  não  é 
primo!!!)
'''
print("Exercício 6 - Identifica número primo\n")

numero = int(input("Insira um número inteiro: "))
numeroDivisores = 0

for div in range(2,numero+1):
    if (numero % div) == 0:
        numeroDivisores += 1
    if numeroDivisores > 1:
        break

if (numeroDivisores == 1):
    print ("Número É primo")
else:
    print ("Número NÃO É primo")