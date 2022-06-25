from email.errors import NonASCIILocalPartDefect
import os
import matplotlib.pyplot as plt
from OO.F1 import F1

endereco_arquivo = os.path.join(os.path.dirname(__file__) , "./arquivo", "formula1.txt")
arquivo = open(endereco_arquivo, "r")


lista_pilotos = []
nacionalidade = {}
equipe = {}
equipeOrdenado = {}
nacionalidadeOrdenado = {}


for i in (arquivo.readlines()):
    linha = arquivo.readline
    matriz = i.split(";")
    piloto = F1()
    piloto.anocampeao = matriz[0]
    piloto.nacionalidade = matriz[1]
    piloto.piloto = matriz[2]
    piloto.equipe = matriz[3]
    lista_pilotos.append(piloto)

for i in lista_pilotos:
    if i.nacionalidade in nacionalidade:
        nacionalidade[i.nacionalidade] += 1
    else :
        nacionalidade[i.nacionalidade] = 1 


for i in lista_pilotos:
    print (i.equipe)
    if i.equipe.strip() in equipe:
        equipe[i.equipe.strip()] += 1
    else :
        equipe[i.equipe.strip()] = 1 



for i in sorted(equipe, key = equipe.get, reverse=True)[:5]:
    equipeOrdenado[i] = equipe[i]
plt.plot(equipeOrdenado.keys(), equipeOrdenado.values())

plt.show()

for i in sorted(nacionalidade, key = nacionalidade.get, reverse=True)[:5]:
    nacionalidadeOrdenado[i] = nacionalidade[i]
plt.plot(nacionalidadeOrdenado.keys(), nacionalidadeOrdenado.values())

plt.show()



arquivo.close()