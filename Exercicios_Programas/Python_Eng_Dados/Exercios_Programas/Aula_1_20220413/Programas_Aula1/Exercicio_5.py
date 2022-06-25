'''
5) Faca um programa que leia vários inteiros positivos e mostre, no final, a soma 
dos números pares e a soma dos números ímpares. O programa para quando 
entrar um número maior que 1000.  
'''
print("Exercício 5 - Soma pares e Soma ímpares\n")

print("Para sair insira um número maior que 1000.\n")
print("Apenas valores números positivos serão somados.\n")

numero = 0
somaPares = 0
somaImpares = 0


while numero <= 1000:
    numero = int(input("Insira um número inteiro: "))
    if numero <= 1000:
        if numero > 0 and numero % 2 == 0:
            somaPares += numero
        elif numero > 0:
            somaImpares += numero
    else:
        break

print("")
print ("Soma dos números pares: " + str(somaPares))
print ("Soma dos números impares: " + str(somaImpares))
