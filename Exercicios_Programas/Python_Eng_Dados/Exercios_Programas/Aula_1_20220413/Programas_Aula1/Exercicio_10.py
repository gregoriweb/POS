'''
10) Com base no exercício anterior armazene em um novo dicionário somente os 
nomes com idade superior a 18 anos.
'''



print("Exercício 10 - Novo dicionário paraq maiores de 18 anos \n")

idadesPessoas = {}
idadesPessoas = {    "Maria": 10
                    ,"Joao" : 12
                    ,"Jose" : 15
                    ,"Vinicius" : 16
                    ,"Joel" : 16
                    ,"Ana" : 20
                    ,"Agne" : 23
                    ,"Mario" : 16
                    ,"Alberto" : 18}

idadePessoasMaior18 = {}


for i in idadesPessoas:
    if idadesPessoas[i] >= 18:
        idadePessoasMaior18[i] = idadesPessoas[i]

print ("Dicionário completo:")
print (idadesPessoas)

print()

print ("Dicionário maiores de 18:")
print (idadePessoasMaior18)