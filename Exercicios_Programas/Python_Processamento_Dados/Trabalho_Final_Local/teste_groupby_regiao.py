from pathlib import Path
from matplotlib import pyplot as plt
import pandas as pd

file_path = '{}/{}'.format(Path(__file__).parent,'IBGE_Escolar.csv')
data = open(file_path, 'r', encoding='utf-8')


#1)

dt_file = pd.read_csv(data, sep = ';', decimal=',', encoding='utf-8')
df_file = pd.DataFrame(dt_file,  columns=[                                      
                                    'Nome das Grandes Regiões',
                                    'Nome da Microregião',
                                    'Superior completo - Amarela',
                                    'Superior completo - Branca',
                                    'Superior completo - Indígena',
                                    'Superior completo - Parda',
                                    'Superior completo - Preta'])

df_file = df_file[df_file['Nome das Grandes Regiões'].str.strip()=='Sul']
#df_filedf=df_file.groupby('Nome das Grandes Regiões').sum().aggregate('max')
df=df_file.mean()


print(df_file)
print(df)

df=df.rename_axis('Escolaridade').reset_index()
df.insert(1, 'Macroregiao Maior N. Pess.', list(df_file.groupby('Nome da Microregião').sum().idxmax(0)), True)
df.rename( columns={0:'N. de Pessoas'}, inplace=True )
df=df.sort_values(by=['N. de Pessoas'])
#df.to_json('{}/{}'.format(Path(__file__).parent,'pessoas_etnia_escolaridade.json', orient='split'))
#df.to_csv('{}/{}'.format(Path(__file__).parent,'pessoas_etnia_escolaridade.csv', orient='split'))

#plt.bar(df['Escolaridade'].tolist(), df['N. de Pessoas'].tolist())
#plt.xticks(rotation=30, ha='right')
#plt.xlabel('Nível Superiror - Raça / Maior Microregião')
#plt.title('Maiores Microregiores por Escolaridade e Raça')
#plt.yticks(df['N. de Pessoas'].tolist(),df['Macroregiao Maior N. Pess.'].tolist()) 
#plt.tight_layout()
#plt.show()