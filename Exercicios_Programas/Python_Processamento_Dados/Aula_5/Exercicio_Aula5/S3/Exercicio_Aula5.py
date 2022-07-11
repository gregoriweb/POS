import boto3
import pandas as pd
import ssl
import io
import matplotlib.pyplot as plt

def leArquivo():
    s3 = boto3.resource('s3', aws_access_key_id='AKIAUSA6HND622LYXMPD', aws_secret_access_key='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')
    bucket = s3.Bucket('datalake-pucminas')
      
    for obj in bucket.objects.filter(Prefix='planilhas/IDH2010.csv'):      
        file_content  = obj.get()['Body'].read().decode('utf-8')
        return file_content
        break


ssl._create_default_https_context = ssl._create_unverified_context    
data = io.StringIO(leArquivo())
dt = pd.read_csv(data, sep = ';', decimal=',')
#print(dt)
#converteCSV(dt)
print (dt.head())
print (dt.columns)
print (dt.nlargest(5, 'Esperança de vida ao nascer'))
print ("")
print (dt.nlargest(5, 'Mortalidade infantil'))
#print(dt_csv.dtypes)

df = pd.DataFrame(dt.nlargest(5, 'Mortalidade infantil'), columns=['Município','Mortalidade infantil'])
#df.plot(x='Município', y='Esperança de vida ao nascer', marker='.')
df.plot(x='Município', y='Mortalidade infantil', kind = 'bar')
plt.show()

df = pd.DataFrame(dt.nlargest(5, 'Esperança de vida ao nascer'), columns=['Município','Esperança de vida ao nascer'])
#df.plot(x='Município', y='Esperança de vida ao nascer', marker='.')
df.plot(x='Município', y='Esperança de vida ao nascer', kind = 'bar')
plt.show()