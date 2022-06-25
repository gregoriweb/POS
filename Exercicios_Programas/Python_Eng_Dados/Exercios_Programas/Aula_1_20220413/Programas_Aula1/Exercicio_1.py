'''
1) Criar um programa que calcule a média de salários de uma empresa, pedindo 
ao usuário a grade de funcionários (Função e Salário), e devolvendo a média 
salarial. Obs. Utilize a estrutura de dicionários para resolver o exercício.
'''

gradeFuncionarios = {}


print("Exercício 1 - Média Salárial por função\n")

i = 1
while input("Tecle ENTER para inserir funções \n"+"Digite CALCULAR para obter a média\n") != 'CALCULAR':
    
    nomeFuncionario = input("Informe a função [" + str(i) + "]: ")
    salarioFuncionario = input("Informe o salário da função "+ nomeFuncionario + " ["+ str(i) + "]: ")
    gradeFuncionarios[nomeFuncionario] = salarioFuncionario

    i += 1

### Calcular Media

totalSalario = 0

for sal in gradeFuncionarios:
    print (sal + " - " + gradeFuncionarios[sal])
    totalSalario += int(gradeFuncionarios[sal])

print ("A média dos salários é: " + str( totalSalario/len(gradeFuncionarios) ))


    
