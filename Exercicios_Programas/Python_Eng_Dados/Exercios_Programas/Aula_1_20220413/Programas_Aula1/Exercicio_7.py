'''
7) Crie  uma  função  para  pesquisar  dentro  do  dicionário  uma  chave  informada 
retornando seu valor. 
'''
print("Exercício 7 - Função de pesquisa em dicionário\n")

def retornaValorDicionario (dic, chave):
    return dic[chave]


dicionario = {}

dicionario[1] = "A"
dicionario[2] = "B"
dicionario[3] = "C"
dicionario[4] = "D"
dicionario[5] = "E"
dicionario[6] = "F"
dicionario[7] = "G"
dicionario[8] = "H"
dicionario[9] = "I"

print (retornaValorDicionario (dicionario, 8))