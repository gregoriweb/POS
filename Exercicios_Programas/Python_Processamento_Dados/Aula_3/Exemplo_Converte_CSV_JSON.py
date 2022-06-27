'''
Created on 10 de Junho. de 2022
@author: nelsonjunior
'''

import pandas as pd


def converte_csv_json(nomeArquivo):
    df = pd.read_csv(r'ArquivoCSV.csv')
    df.to_json(r'ArquivoJson.json')


def converte_json_csv(nomeArquivo):
    df = pd.read_json(r'ArquivoJson.json')
    df.to_csv(r'ArquivoCSVConvertido.csv', index=False)


def le_arquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    tamanho = arquivo.readlines()
    cont = 0
    dados = []

    while(len(tamanho) > cont):
        linha = tamanho[cont]
        print(linha)
        dados.append(linha)
        cont += 1

    arquivo.close()
    return linha


def grava_arquivo(nomeArquivo, dados):
    arquivo = open(nomeArquivo + ".txt", "w+")
    for dado in dados:
        arquivo.write(dado)
        print(dado)
    arquivo.close()


nomeArquivo = "ArquivoCSV.csv"
##dados = le_arquivo(nomeArquivo)
converte_csv_json("")
converte_json_csv("")
