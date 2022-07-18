from pathlib import Path
from matplotlib import pyplot as plt
import pandas as pd

file_path = '{}/{}'.format(Path(__file__).parent,'IBGE_Escolar.csv')
data = open(file_path, 'r', encoding='utf-8')

dt_file = pd.read_csv(data, sep = ';', decimal=',', encoding='utf-8')
#print (dt_file) 
df_file = pd.DataFrame(dt_file,  columns=[                                      #,index =['Nome da Microregião'],
                                    'Nome da Microregião',
                                    'Superior completo - Amarela',
                                    'Superior completo - Branca',
                                    'Superior completo - Indígena',
                                    'Superior completo - Parda',
                                    'Superior completo - Preta'])

#print (df_file)

# group_df_file=df_file.set_index('Nome da Microregião')

df_max_sum=df_file.groupby('Nome da Microregião').sum().aggregate('max')

df_idmax=df_file.groupby('Nome da Microregião').sum().idxmax(0)

#print(df_idmax)

#print(df_max_sum)

#df_max_sum.insert(1, 'Maior N. Habitantes', df_max_sum, True)

#print(df_max_sum.rename_axis('Escolaridade').reset_index()) # transforma o indice em coluna rename_axis antes renomea a coluna para 'Escolaridade'


df_new = df_max_sum.rename_axis('Escolaridade').reset_index()

df_new.insert(1, 'Macroregiao Maior N. Pess.', list(df_file.groupby('Nome da Microregião').sum().idxmax(0)), True)
df_new.rename( columns={0:'N. de Pessoas'}, inplace=True )

df_new = df_new.sort_values(by=['N. de Pessoas'])

# group_df_file = df_file.groupby(['Nome da Microregião']).sum().idxmax(0)
# 
df_new.to_json('{}/{}'.format(Path(__file__).parent,'teste_json.json', orient='split'))

#df_new.plot('Escolaridade','N. de Pessoas',kind='bar')



plt.bar(df_new['Escolaridade'].tolist(), df_new['N. de Pessoas'].tolist())
plt.xticks(rotation=30, ha='right')
plt.xlabel('Nível Superiror - Raça / Maior Microregião')
plt.title('Maiores Microregiores por Escolaridade e Raça')
plt.yticks(df_new['N. de Pessoas'].tolist(),df_new['Macroregiao Maior N. Pess.'].tolist()) 
#plt.yticks()
plt.tight_layout()
#plt.show()



#df_new['Macroregiao Maior N. Pess.'].tolist(), y=df_new['N. de Pessoas'].tolist(), kind='bar' 
plt.show()

#df = pd.DataFrame([['Jay',16,'BBA'],
#                   ['Jack',19,'BTech'],
#                   ['Mark',18,'BSc']],
#                  columns = ['Name','Age','Course'])
#
#js = df.to_json(orient = 'columns')

#print(js)

#group_df_file.to_json('{}/{}'.format(Path(__file__).parent,'teste_json.json'))