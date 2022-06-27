import matplotlib.pyplot as plt
def map(nome_arquivo):
    
    arquivo = open(nome_arquivo + ".csv", "r", encoding="utf-8")
    nomes = []
    tamanho = arquivo.readlines()
    cont = 0
    
    while(len(tamanho) > cont):
        linha = tamanho[cont]
        dados = linha.split(";")   
        if(cont == 0):
            cont += 1
            continue;
        nome = dados[1].split(" ")
        cont += 1
        
        for i in range(len(nome)):
            if(nome[i] == " " or nome[i] == "" or nome[i] == "de" or nome[i] == "da" or nome[i] == "do" or nome[i] == "dos" or nome[i] == "e"):
                continue
            nomes.append(nome[i])
            
    nomes.sort(key=None, reverse=False)
    mapa = {}
    for nome in nomes:
        mapa[nome] = nomes.count(nome)
    
    return mapa

def reduce_mapa(mapa):
    chave = ""
    valor = 0
    
    for nome in mapa:
        if(mapa[nome] > valor):
            chave = nome
            valor = mapa[nome]
    
    reduce = {}
    reduce[chave] = valor
    return reduce

def grava_imagem(mapa):
    mapaPlot = {}
    cont = 0
    for i in sorted(mapa, key=mapa.get, reverse=True):
        if(cont > 10):
            break;
        
        cont += 1
        mapaPlot[i] = mapa[i]
        
    plt.barh(list(mapaPlot.keys()), mapaPlot.values())
    plt.gca().invert_yaxis()
    plt.savefig('teste.png', format='png')
    plt.show()
    plt.close()

mapa = map("alunos2022")

mapa_reduce = reduce_mapa(mapa)    

grava_imagem(mapa)