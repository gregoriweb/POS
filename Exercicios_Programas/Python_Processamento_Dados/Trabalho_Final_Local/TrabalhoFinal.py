from pathlib import Path
from matplotlib import pyplot as plt
import pandas as pd

root_path = Path(__file__).parent
plot_destiny='{}/{}'.format(root_path,'plot_output')
json_destiny='{}/{}'.format(root_path,'json_output')
csv_destiny='{}/{}'.format(root_path,'csv_output')
file_path = '{}/{}'.format(root_path,'IBGE_Escolar.csv')

'''
a) Extraia qual município possui maior numero de pessoas com ensino superior
completo por Etinia
Faca um gráfico ilustrando seu resultado e colocar no DataLake graficos
Gere o arquivo em formato .excel e coloque no DataLake planilha e um Json no
diretorio Json
'''
data = open(file_path, 'r', encoding='utf-8')

dt_file = pd.read_csv(data, sep = ';', decimal=',', encoding='utf-8')
df_file = pd.DataFrame(dt_file,  columns=[                                      
                                    'Nome da Microregião',
                                    'Superior completo - Amarela',
                                    'Superior completo - Branca',
                                    'Superior completo - Indígena',
                                    'Superior completo - Parda',
                                    'Superior completo - Preta'])

df=df_file.groupby('Nome da Microregião').sum().aggregate('max')
df=df.rename_axis('Escolaridade').reset_index()
df.insert(1, 'Macroregiao Maior N. Pess.', list(df_file.groupby('Nome da Microregião').sum().idxmax(0)), True)
df.rename( columns={0:'N. de Pessoas'}, inplace=True )
df=df.sort_values(by=['N. de Pessoas'])
#df.to_json('{}/{}'.format(Path(__file__).parent,'pessoas_etnia_escolaridade.json', orient='split'))
#df.to_csv('{}/{}'.format(Path(__file__).parent,'pessoas_etnia_escolaridade.csv', orient='split'))

plt.bar(df['Escolaridade'].tolist(), df['N. de Pessoas'].tolist())
plt.xticks(rotation=30, ha='right')
plt.title('Cidades Maior N. Habitantes com Superior Completo')
plt.xlabel('Raça')
plt.yticks(df['N. de Pessoas'].tolist(),df['Macroregiao Maior N. Pess.'].tolist()) 
plt.tight_layout()
plt.savefig('{}/{}'.format(plot_destiny,'maiores_pessoas_etnia_escolaridade.png') , format='png')
#plt.show()
plt.close()

df.to_json('{}/{}'.format(json_destiny,'maiores_pessoas_etnia_escolaridade.json', orient='split'))
df.to_csv('{}/{}'.format(csv_destiny,'maiores_pessoas_etnia_escolaridade.csv', orient='split'))

data.close()


'''
b) Como base na sua cidade Natal mostre os indices do ensino superior por Etinia.
Faca um gráfico ilustrando seu resultado e coloque no DataLake Imagens
Gere o arquivo em formato excel e coloque no DataLake planilha e um Json no
diretorio Json
'''
data = open(file_path, 'r', encoding='utf-8')
dt_file = pd.read_csv(data, sep = ';', decimal=',', encoding='utf-8')
df_file = pd.DataFrame(dt_file,  columns=[                                      
                                    'Nome da Microregião',
                                    'incompleto - Amarela',
                                    'Incompleto - Branca',
                                    ' incompleto - Indígena',
                                    'incompleto - Parda',
                                    'Incompleto - Preta',
                                    'Superior completo - Amarela',
                                    'Superior completo - Branca',
                                    'Superior completo - Indígena',
                                    'Superior completo - Parda',
                                    'Superior completo - Preta'])

df=df_file[df_file['Nome da Microregião'].str.strip()=='Curitiba']
df=df_file.groupby('Nome da Microregião').sum().aggregate('max')
df=df.rename_axis('Escolaridade').reset_index()
df.rename( columns={0:'N. de Pessoas'}, inplace=True )
df=df.sort_values(by=['N. de Pessoas'])


print(df['N. de Pessoas'].tolist())

plt.bar(df['Escolaridade'].tolist(), df['N. de Pessoas'].tolist())
plt.xticks(rotation=30, ha='right')
plt.xlabel('Situação Nivel Superior - Raça')
plt.title('Curitiba Situação Curso Superior Habitantes')
plt.yticks(df['N. de Pessoas'].tolist(), df['N. de Pessoas'].tolist()) 
plt.tight_layout()
plt.savefig('{}/{}'.format(plot_destiny,'curitiba_pessoas_etnia_escolaridade.png') , format='png')
#plt.show()
plt.close()

df.to_json('{}/{}'.format(json_destiny,'curitiba_pessoas_etnia_escolaridade.json', orient='split'))
df.to_csv('{}/{}'.format(csv_destiny,'curitiba_pessoas_etnia_escolaridade.csv', orient='split'))

data.close()

'''
c) Faça um gráfico com a média dos índices por sua região
'''

data = open(file_path, 'r', encoding='utf-8')
dt_file = pd.read_csv(data, sep = ';', decimal=',', encoding='utf-8')
df_file = pd.DataFrame(dt_file,  columns=[      
                                    'Nome das Grandes Regiões',
                                    'Nome da Microregião',
                                    'incompleto - Amarela',
                                    'Incompleto - Branca',
                                    ' incompleto - Indígena',
                                    'incompleto - Parda',
                                    'Incompleto - Preta',
                                    'Superior completo - Amarela',
                                    'Superior completo - Branca',
                                    'Superior completo - Indígena',
                                    'Superior completo - Parda',
                                    'Superior completo - Preta'])

df=df_file.groupby('Nome das Grandes Regiões').mean()

df.rename( columns={0:'Média Região'}, inplace=True )
df.plot(kind='bar')
plt.xlabel('Regiões')
plt.title('Regiões Situação Curso Superior Habitantes')
plt.tight_layout()
plt.savefig('{}/{}'.format(plot_destiny,'regiao_etnia_escolaridade.png'), format='png')
plt.close()

df.to_json('{}/{}'.format(json_destiny,'regiao_etnia_escolaridade.json', orient='split'))
df.to_csv('{}/{}'.format(csv_destiny,'regiao_pessoas_etnia_escolaridade.csv', orient='split'))

data.close()