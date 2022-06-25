'''
3) Escreva um programa em Pyhton para ler o nome e a idade de uma pessoa, e 
exibir quantos dias de vida ela possui. Considere sempre anos completos, e que 
um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; 
veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 DIAS
'''

print("Exercício 3 - Dias vividos\n")

nome = input("Informe seu nome: ")
idade = int( input("Informe sua idade: ") )
diasVida = idade*365

print (str(nome) + ", VOCÊ JÁ VIVEU " + str(diasVida) + " DIAS")

