'''
8) Crie uma função que calcule os descontos do salário bruto informado, 
considere para incidência de descontos INSS, IR e retorne o salário líquido.
'''
print("Exercício 8 - Função calculo salário líquido\n")

def calculaSalarioLiquido (salarioBruto):

    salarioMinimo = 1212.00

    faixaINSS = 0 #Chave Inicial Dicionário de Faixas Salariais
    faixaSalario = salarioBruto # Referencia Inicial para iteração com Faixas saláriais
    
    descontoINSSFaixa = 0

    diferencaSalarioFaixaSalarialINSS = salarioBruto
    
    faixaSalarialINSS = {}
    faixaSalarialINSS [0] = 1212.00
    faixaSalarialINSS [1] = 2427.35
    faixaSalarialINSS [2] = 3641.03
    faixaSalarialINSS [3] = 7087.22

    alicotasINSS = {}
    alicotasINSS [faixaSalarialINSS [0]] = 0.075
    alicotasINSS [faixaSalarialINSS [1]] = 0.09
    alicotasINSS [faixaSalarialINSS [2]] = 0.12
    alicotasINSS [faixaSalarialINSS [3]] = 0.14

    def caculaValorINSSFaixa (teste):
        teste


    if (salarioBruto < salarioMinimo):
        print ("Salário menor que o mínimo")
        exit

    #    while faixaSalario >= faixaSalarialINSS [faixaINSS] :

# vai ter que mudar para for pq as alicotas acontecem apenas nas quatro faixas enquanto a diferenca entre as faixa não atinte o limite da ultima

    while diferencaSalarioFaixaSalarialINSS > 0 or diferencaSalarioFaixaSalarialINSS < faixaSalarialINSS [3]  :
        faixaINSSAnterior = (faixaINSS - 1, 0) [faixaINSS == 0]
        
        if faixaINSS == 0: 
            faixaSalarialINSSAnterior = 0
        else:
            faixaSalarialINSSAnterior = faixaSalarialINSS [faixaINSSAnterior]
        
        # print (str (faixaSalarialINSSAnterior))
        # print ( "salarioBruto:"+ str(salarioBruto) + ". \n"+
        #         "faixaSalario:"+ str(faixaSalario) + ". \n"+
        #         "faixaINSS:"+ str(faixaINSS) + ". \n"+
        #         "Limite chave:" + str(faixaINSS) + ". \n" + 
        #         "Limite INSS:" + str(faixaSalarialINSS [faixaINSS]) + ". \n" + 
        #         "Alícota INSS:" + str(alicotasINSS[faixaSalarialINSS [faixaINSS]]) + ". \n" 
        #         "INSS na faixa: "+ str(alicotasINSS[faixaSalarialINSS [faixaINSS]]) + " * " + str(faixaSalarialINSS [faixaINSS]) + " = " + str(alicotasINSS[faixaSalarialINSS [faixaINSS]] * faixaSalarialINSS [faixaINSS])  + ". \n" 
        #         "INSS na faixa 2: "+ str(alicotasINSS[faixaSalarialINSS [faixaINSS]]) + " * (" + str(faixaSalarialINSS [faixaINSS]) +"-"+ str(faixaSalarialINSS [faixaSalarialINSSAnterior]) + ") = " + str(alicotasINSS[faixaSalarialINSS [faixaINSS]] * faixaSalarialINSS [faixaINSS])  + ". \n" 
        #         "ternteste: " + " - " + (str(faixaSalarialINSS [ faixaINSS  ]), str(0)) [faixaINSS == 0] + ". \n" 
        #         "faixaINSS type: " + str(type(faixaINSS))
        #       )
        # 

        # print ("INSS na faixa 2: "+ str(alicotasINSS[faixaSalarialINSS [faixaINSS]]) + " * (" + str(faixaSalarialINSS [faixaINSS]) +"-"+ str(faixaSalarialINSS [faixaSalarialINSSAnterior]) + ") = " + str(alicotasINSS[faixaSalarialINSS [faixaINSS]] * faixaSalarialINSS [faixaINSS])  + ". \n"  )

        print ("INSS na faixa 2: "+ str(alicotasINSS[faixaSalarialINSS [faixaINSS]]) + " * (" + str(faixaSalarialINSS [faixaINSS]) +"-"+ str(faixaSalarialINSSAnterior) + ") = " + str(alicotasINSS[faixaSalarialINSS [faixaINSS]] * faixaSalarialINSS [faixaINSS])  + ". \n"  )


        descontoINSSFaixa += (faixaSalarialINSS[faixaINSS] - faixaSalarialINSSAnterior) *  alicotasINSS[faixaSalarialINSS [faixaINSS]]

        print((faixaSalarialINSS[faixaINSS] - faixaSalarialINSSAnterior) *  alicotasINSS[faixaSalarialINSS [faixaINSS]])
        print (descontoINSSFaixa)

        print(faixaINSS)
        print(faixaSalario )
        faixaSalario -= faixaSalarialINSS [faixaINSS]
        faixaINSS += 1

        diferencaSalarioFaixaSalarialINSS = faixaSalarialINSS [faixaINSS] - faixaSalarialINSSAnterior
        print (diferencaSalarioFaixaSalarialINSS)

        

calculaSalarioLiquido (10000)
    

# IR  = 
# Até 1.903,98	0%	0,00
# De 1.903,99 até 2.826,65	7,5%	142,80
# De 2.826,66 até 3.751,05	15%	354,80
# De 3.751,06 até 4.664,68	22,5%	636,13
# Acima de 4.664,69	27,5%	869,36