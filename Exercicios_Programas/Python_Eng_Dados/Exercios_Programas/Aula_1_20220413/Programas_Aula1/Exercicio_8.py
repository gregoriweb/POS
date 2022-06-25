'''
8) Crie uma função que calcule os descontos do salário bruto informado, 
considere para incidência de descontos INSS, IR e retorne o salário líquido.
'''
print("Exercício 8 - Função calculo salário líquido\n")


def calcula_INSS_2022 (salarioBruto):
    faixaSalarialINSS = {}
    faixaSalarialINSS [0] = 1212.00
    faixaSalarialINSS [1] = 2427.35 
    faixaSalarialINSS [2] = 3641.03 
    faixaSalarialINSS [3] = 7087.22 

    alicotaINSS = {}
    alicotaINSS [0] = 0.075 
    alicotaINSS [1] = 0.09  
    alicotaINSS [2] = 0.12  
    alicotaINSS [3] = 0.14  

    faixaSalarialINSSLiquida = {}
    totalDescontoINSS = 0

    if salarioBruto == faixaSalarialINSS [0]:
        faixaSalarialINSSLiquida[0] = salarioBruto
        totalDescontoINSS = (faixaSalarialINSSLiquida[0] * alicotaINSS [0])
    
    elif salarioBruto > faixaSalarialINSS [0] and salarioBruto <= faixaSalarialINSS [1]:
        faixaSalarialINSSLiquida[0] = faixaSalarialINSS [0]
        faixaSalarialINSSLiquida[1] = salarioBruto - faixaSalarialINSS [0]
        totalDescontoINSS = (faixaSalarialINSSLiquida[0] * alicotaINSS [0]) + (faixaSalarialINSSLiquida[1] * alicotaINSS [1])

    elif salarioBruto > faixaSalarialINSS [1] and salarioBruto <= faixaSalarialINSS [2]:
        faixaSalarialINSSLiquida[0] = faixaSalarialINSS [0]
        faixaSalarialINSSLiquida[1] = faixaSalarialINSS [1] - faixaSalarialINSS [0]
        faixaSalarialINSSLiquida[2] = salarioBruto - faixaSalarialINSS [1]
        totalDescontoINSS = (faixaSalarialINSSLiquida[0] * alicotaINSS [0]) + (faixaSalarialINSSLiquida[1] * alicotaINSS [1]) + (faixaSalarialINSSLiquida[2] * alicotaINSS [2])

    elif salarioBruto > faixaSalarialINSS [2] and salarioBruto <= faixaSalarialINSS [3]:
        faixaSalarialINSSLiquida[0] = faixaSalarialINSS [0]
        faixaSalarialINSSLiquida[1] = faixaSalarialINSS [1] - faixaSalarialINSS [0]
        faixaSalarialINSSLiquida[2] = faixaSalarialINSS [2] - faixaSalarialINSS [1]
        faixaSalarialINSSLiquida[3] = salarioBruto - faixaSalarialINSS [2]
        totalDescontoINSS = (faixaSalarialINSSLiquida[0] * alicotaINSS [0]) + (faixaSalarialINSSLiquida[1] * alicotaINSS [1]) + (faixaSalarialINSSLiquida[2] * alicotaINSS [2]) + (faixaSalarialINSSLiquida[3] * alicotaINSS [3])

    elif salarioBruto > faixaSalarialINSS [3]:
        faixaSalarialINSSLiquida[0] = faixaSalarialINSS [0]
        faixaSalarialINSSLiquida[1] = faixaSalarialINSS [1] - faixaSalarialINSS [0]
        faixaSalarialINSSLiquida[2] = faixaSalarialINSS [2] - faixaSalarialINSS [1]
        faixaSalarialINSSLiquida[3] = faixaSalarialINSS [3] - faixaSalarialINSS [2]
        totalDescontoINSS = (faixaSalarialINSSLiquida[0] * alicotaINSS [0]) + (faixaSalarialINSSLiquida[1] * alicotaINSS [1]) + (faixaSalarialINSSLiquida[2] * alicotaINSS [2]) + (faixaSalarialINSSLiquida[3] * alicotaINSS [3])

    return totalDescontoINSS


def calcula_IRRF_2022 (salarioBruto):
    descontoINSS2022 = calcula_INSS_2022(salarioBruto)

    renda = salarioBruto - descontoINSS2022

    faixaRendaIRRF = {}
    faixaRendaIRRF [0] = 0
    faixaRendaIRRF [1] = 1903.98
    faixaRendaIRRF [2] = 2826.65 
    faixaRendaIRRF [3] = 3751.06 
    faixaRendaIRRF [4] = 4664.68 

    faixaReducaoIRRF = {}
    faixaReducaoIRRF [0] = 0
    faixaReducaoIRRF [1] = 142.8
    faixaReducaoIRRF [2] = 354.8
    faixaReducaoIRRF [3] = 636.13
    faixaReducaoIRRF [4] = 869.36

    alicotaRendaIRRF = {}
    alicotaRendaIRRF [0] = 0
    alicotaRendaIRRF [1] = 0.075
    alicotaRendaIRRF [2] = 0.15
    alicotaRendaIRRF [3] = 0.225
    alicotaRendaIRRF [4] = 0.275


    if renda > faixaRendaIRRF [0] and renda <= faixaRendaIRRF [1]:
        return ( renda *  alicotaRendaIRRF [0] ) - faixaReducaoIRRF [0]
    elif renda > faixaRendaIRRF [1] and renda <= faixaRendaIRRF [2]:
        return (renda *  alicotaRendaIRRF [1] ) - faixaReducaoIRRF [1]
    elif renda > faixaRendaIRRF [2] and renda <= faixaRendaIRRF [3]:
        return (renda * alicotaRendaIRRF [2] ) - faixaReducaoIRRF [2]
    elif renda > faixaRendaIRRF [3] and renda <= faixaRendaIRRF [4]:
        return (renda * alicotaRendaIRRF [3] ) - faixaReducaoIRRF [3]
    elif renda > faixaRendaIRRF [4]:
        return (renda * alicotaRendaIRRF [4] ) - faixaReducaoIRRF [4]

def calculaSalarioLiquido(salarioBruto):
    return salarioBruto - calcula_INSS_2022(salarioBruto) - calcula_IRRF_2022(salarioBruto)

salarioBruto = input("Informe o salário Bruto: R$ " )
print("Salário Líquido: R$ " + str( calculaSalarioLiquido(float( salarioBruto)) ) )