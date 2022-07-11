'''
Marcos Vinicius Barbosa Vieira
'''

import boto3
import pandas as pd
import ssl


def pesquisaArquivo():
    s3 = boto3.resource('s3', aws_access_key_id='AKIAUSA6HND622LYXMPD', aws_secret_access_key='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')
    bucket = s3.Bucket('datalake-pucminas')

    for obj in bucket.objects.filter(Prefix='graficos/291131834648.png'):
        if obj.key:
            print("Encontradooooo")
        else:
            print("Não Encontrado")
        break

ssl._create_default_https_context = ssl._create_unverified_context

data = pesquisaArquivo()