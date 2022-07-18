'''
Created on 5 de jul. de 2022

@author: nelsonjunior
'''

import os
import boto3
from Municipio import Municipio
import matplotlib.pyplot as plt
from AmazonS3 import AmazonS3
import ssl
import pandas as pd


def le_arquivoS3(qtde_expectativa, flag_ordenacao, tipo_expectativa):
    s3 = boto3.resource('s3', aws_access_key_id='AKIAUSA6HND622LYXMPD', aws_secret_access_key='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')
    bucket = s3.Bucket('datalake-pucminas')
    lista= []
    cont = 0
    for obj in bucket.objects.filter(Prefix='planilhas/IDH2010.csv'):
        for line in obj.get()['Body'].read().decode('utf-8').splitlines():
            if(cont == 0):
                cont += 1
                continue
            
            dados = line.split(";")
            m = Municipio()
            m.ano = dados[0]
            m.cod_municipio = int(dados[1])
            m.nome_municipio = dados[2]
            m.expectativa = float(dados[3].replace("," , "."))
            m.mortalidade = float(dados[4].replace("," , "."))
            lista.append(m)
            
     
    if(tipo_expectativa == "E"):
        lista.sort(key=lambda municipio: municipio.expectativa, reverse = flag_ordenacao)   
    else:
        lista.sort(key=lambda municipio: municipio.mortalidade, reverse = flag_ordenacao)   

    
    mapa = {}
    cont = 0
    for m in lista:
        if(cont >= qtde_expectativa):
            break
        
        cont += 1
        if(tipo_expectativa == "E"):
            mapa[m.nome_municipio] = m.expectativa
        else:
            mapa[m.nome_municipio] = m.mortalidade
    return mapa


def grava_imagem(mapa, nome_arquivo):
    mapaPlot = {}
    cont = 0
    for i in sorted(mapa, key=mapa.get, reverse=True):
        cont += 1
        mapaPlot[i] = mapa[i]
        
    plt.barh(list(mapaPlot.keys()), mapaPlot.values())
    plt.gca().invert_yaxis()
    plt.savefig(nome_arquivo, format='png')
    plt.show()
    plt.close()
    
def grava_Json_excel(mapa):
    lista = []
    for m in mapa:
        municipio = Municipio()
        municipio.nome_municipio = m
        municipio.mortalidade = mapa[m]
        lista.append(municipio)
    df = pd.DataFrame([x.as_dict_mortalidade() for x in lista])
    file_name_excel = os.path.join(os.path.dirname(__file__),'Mortalidade.xlsx')
    file_name_json = os.path.join(os.path.dirname(__file__),'Mortalidade.json')
    df.to_excel(file_name_excel)
    df.to_json(file_name_json)
    print("ok")

file_name_grafico = 'Mortalidade.png'        
file_name_excel = 'Mortalidade.xlsx'
file_name_json = 'Mortalidade.json'    
qtde_expectativa = 5
flag_ordenacao =  True
tipo_expectativa =  "M"
titulo = "Mortalidade.png"
mapa =  le_arquivoS3(qtde_expectativa, flag_ordenacao, tipo_expectativa)
grava_imagem(mapa, os.path.join(os.path.dirname(__file__), titulo))
grava_Json_excel(mapa)

ssl._create_default_https_context = ssl._create_unverified_context    
AS3 = AmazonS3()
AS3.post_receipt_image(file_name_grafico)
#AS3.post_receipt_json(file_name_json)
#AS3.post_receipt_json(file_name_excel)