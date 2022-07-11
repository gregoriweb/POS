'''
Created on 7 de dez de 2021

@author: Nelson
'''

import boto3
import pandas as pd
import ssl

 
def leArquivo():
    s3 = boto3.resource('s3', aws_access_key_id='AKIAUSA6HND622LYXMPD', aws_secret_access_key='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')
    bucket = s3.Bucket('datalake-pucminas')
      
    for obj in bucket.objects.filter(Prefix='planilhas/IDH2010.csv'):      
        file_content  = obj.get()['Body'].read().decode('utf-8')
        return file_content
        break

def leArquivo_original():
    s3 = boto3.resource('s3', aws_access_key_id='AKIAUSA6HND622LYXMPD', aws_secret_access_key='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')
    bucket = s3.Bucket('datalake-pucminas')
      
    for obj in bucket.objects.filter(Prefix='json/271836337568.json'):      
        file_content  = obj.get()['Body'].read().decode('utf-8')
        print (file_content)
        return file_content
        break


def converteCSV (data):
    data.to_csv (r'venda.csv', index = None)

ssl._create_default_https_context = ssl._create_unverified_context    
data = leArquivo()
#dt = pd.read_json(data)
dt_csv = pd.read_csv(data)
#print(dt)
#converteCSV(dt)
print (dt_csv)



