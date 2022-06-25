'''
2) Faça um programa em python para calcular quantas ferraduras são necessárias 
para equipar todos os cavalos comprados para um haras. A informação de 
cavalos comprados deve ser informada pelo usuário.
'''

print("Exercício 2 - Ferraduras necessárias\n")

cavalos = int( input("Informe o número de cavalos comprados: ") )
ferraduras = int(cavalos) * 4

print (str(ferraduras) + " ferraduras são necessárias para " + str(cavalos) + " cavalo(s).")

