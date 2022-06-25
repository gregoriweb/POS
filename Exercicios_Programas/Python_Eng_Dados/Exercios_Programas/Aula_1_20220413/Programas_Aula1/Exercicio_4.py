'''
4) Um circo deseja saber qual o preço ideal dos ingressos, de acordo com a cidade 
que visitam. Para tanto, eles descobriram que em média 120 pessoas 
comparecem em cada sessão, quando o preço do ingresso é R$ 5,00. A partir 
disso, a cada redução de R$ 0,50 há um aumento de publico, que difere em 
cada cidade. Cada sessão tem um custo de R$ 200,00 ao circo. Faca um 
programa que, dado o número adicional de pessoas a cada redução de R$ 0,50 
no preço do ingresso, imprima a tabela de lucro de cada sessão. Considere a 
variação de preço entre R$ 5,00 e R$ 1,00. Informe também ao usuário, qual é
o valor de ingresso que gera o maior lucro. Dica: para testar o algoritmo, 
considere taxas de aumento de 26 e 30 pessoas.
'''
print("Exercício 4 - Aumento de publico/Redução Ingresso\n")

adicionalPublico = int ( input("Aumento de público por redução de R$ 0.50: ") )
ingresso = 5.00
publicoEstimado = 120

custoEspetaculo = 200
taxaReducao = 0.5

maiorLucro = 0
ingressoMaiorLucro = 0

tabelaLucro = {}

while ingresso >= 1:
        print ( str(ingresso) + " - " + str(publicoEstimado))
        lucro = (publicoEstimado * ingresso) - custoEspetaculo
        tabelaLucro[ingresso] = lucro

        if (maiorLucro < lucro):
            maiorLucro = lucro
            ingressoMaiorLucro = ingresso

        ingresso -= taxaReducao
        publicoEstimado = publicoEstimado + adicionalPublico


print ("Com ingresso de R$ " + str(ingressoMaiorLucro) + " você obterá o maior lucro. Seu maior lucro será de R$ " + str(tabelaLucro[ingressoMaiorLucro]) +".")