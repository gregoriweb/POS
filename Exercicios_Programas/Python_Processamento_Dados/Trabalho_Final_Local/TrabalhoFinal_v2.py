from pathlib import Path
from matplotlib import pyplot as plt
import pandas as pd

root_path = Path(__file__).parent
plot_destiny='{}/{}'.format(root_path,'plot_output')
json_destiny='{}/{}'.format(root_path,'json_output')
csv_destiny='{}/{}'.format(root_path,'csv_output')
file_path = '{}/{}'.format(root_path,'IBGE_Escolar.csv')

print (plot_destiny, json_destiny, csv_destiny)

data = open(file_path, 'r', encoding='utf-8')


#####       '''
#####       a) Extraia qual município possui maior numero de pessoas com ensino superior
#####       completo por Etinia
#####       Faca um gráfico ilustrando seu resultado e colocar no DataLake graficos
#####       Gere o arquivo em formato .excel e coloque no DataLake planilha e um Json no
#####       diretorio Json
#####       '''
#####       
#####       dt_file = pd.read_csv(data, sep = ';', decimal=',', encoding='utf-8')
#####       df_file = pd.DataFrame(dt_file,  columns=[                                      
#####                                           'Nome da Microregião',
#####                                           'Superior completo - Amarela',
#####                                           'Superior completo - Branca',
#####                                           'Superior completo - Indígena',
#####                                           'Superior completo - Parda',
#####                                           'Superior completo - Preta'])
#####       
#####       df=df_file.groupby('Nome da Microregião').sum().aggregate('max')
#####       df=df.rename_axis('Escolaridade').reset_index()
#####       df.insert(1, 'Macroregiao Maior N. Pess.', list(df_file.groupby('Nome da Microregião').sum().idxmax(0)), True)
#####       df.rename( columns={0:'N. de Pessoas'}, inplace=True )
#####       df=df.sort_values(by=['N. de Pessoas'])
#####       df.to_json('{}/{}'.format(Path(__file__).parent,'pessoas_etnia_escolaridade.json', orient='split'))
#####       df.to_csv('{}/{}'.format(Path(__file__).parent,'pessoas_etnia_escolaridade.csv', orient='split'))
#####       
#####       plt.bar(df['Escolaridade'].tolist(), df['N. de Pessoas'].tolist())
#####       plt.xticks(rotation=30, ha='right')
#####       plt.xlabel('Nível Superiror - Raça / Maior Microregião')
#####       plt.title('Maiores Microregiores por Escolaridade e Raça')
#####       plt.yticks(df['N. de Pessoas'].tolist(),df['Macroregiao Maior N. Pess.'].tolist()) 
#####       plt.tight_layout()
#####       plt.show()




#####       '''
#####       b) Como base na sua cidade Natal mostre os indices do ensino superior por Etinia.
#####       Faca um gráfico ilustrando seu resultado e coloque no DataLake Imagens
#####       Gere o arquivo em formato excel e coloque no DataLake planilha e um Json no
#####       diretorio Json
#####       '''
#####       
#####       dt_file = pd.read_csv(data, sep = ';', decimal=',', encoding='utf-8')
#####       df_file = pd.DataFrame(dt_file,  columns=[                                      
#####                                           'Nome da Microregião',
#####                                           'incompleto - Amarela',
#####                                           'Incompleto - Branca',
#####                                           'incompleto - Indígena',
#####                                           'incompleto - Parda',
#####                                           'Incompleto - Preta',
#####                                           'Superior completo - Amarela',
#####                                           'Superior completo - Branca',
#####                                           'Superior completo - Indígena',
#####                                           'Superior completo - Parda',
#####                                           'Superior completo - Preta'])
#####       
#####       df_file = df_file[df_file['Nome da Microregião'].str.strip()=='Curitiba']
#####       #user_df[user_df['sign_up_date'].str.contains('2022')]
#####       
#####       df=df_file.groupby('Nome da Microregião').sum().aggregate('max')
#####       df=df.rename_axis('Escolaridade').reset_index()
#####       
#####       df.insert(1, 'Macroregiao Maior N. Pess.', list(df_file.groupby('Nome da Microregião').sum().idxmax(0)), True)
#####       df.rename( columns={0:'N. de Pessoas'}, inplace=True )
#####       df=df.sort_values(by=['N. de Pessoas'])
#####       
#####       df.to_json('{}/{}'.format(Path(__file__).parent,'curitiba_pessoas_etnia_escolaridade.json', orient='split'))
#####       df.to_csv('{}/{}'.format(Path(__file__).parent,'curitiba_pessoas_etnia_escolaridade.csv', orient='split'))
#####       
#####       print(df)
#####       
#####       plt.bar(df['Escolaridade'].tolist(), df['N. de Pessoas'].tolist())
#####       plt.xticks(rotation=30, ha='right')
#####       plt.xlabel('Nível Superiror - Raça / Maior Microregião')
#####       plt.title('Maiores Microregiores por Escolaridade e Raça')
#####       plt.yticks(df['N. de Pessoas'].tolist()) 
#####       plt.tight_layout()
#####       plt.show()


'''
c) Faça um gráfico com a média dos índices por sua região
'''

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

plt.tight_layout()
plt.savefig('{}/{}'.format(plot_destiny,'regiao_etnia_escolaridade.png'), format='png')

df.to_json('{}/{}'.format(json_destiny,'regiao_etnia_escolaridade.json', orient='split'))
df.to_csv('{}/{}'.format(csv_destiny,'regiao_pessoas_etnia_escolaridade.csv', orient='split'))


#plt.bar(df['Região'].tolist(), df['Média Região'].tolist())
#plt.xticks(rotation=30, ha='right')
#plt.xlabel('Nível Superiror - Raça / Maior Microregião')
#plt.title('Maiores Microregiores por Escolaridade e Raça')
#plt.yticks(df['Média Região'].tolist()) 
#plt.tight_layout()
#plt.show()