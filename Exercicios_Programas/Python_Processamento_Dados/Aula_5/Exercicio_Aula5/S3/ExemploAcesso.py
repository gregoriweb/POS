'''
Created on 7 de dez de 2021

@author: Nelson
'''

from boto.s3.connection import S3Connection
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context    
conn = S3Connection('AKIAUSA6HND622LYXMPD','tbm8JyvNQ5jJQxp3TgP1O7WGslQVmtiSmFFk0zvv')
bucket = conn.get_bucket('datalake-pucminas')
for key in bucket.list():
    print (key.name.encode('utf-8'))
    
