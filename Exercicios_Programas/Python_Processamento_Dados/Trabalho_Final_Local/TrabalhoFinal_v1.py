from pathlib import Path
from turtle import position
from matplotlib import pyplot as plt
import pandas as pd

file_path = '{}/{}'.format(Path(__file__).parent,'IBGE_Escolar.csv')
data = open(file_path, 'r', encoding='utf-8')

dt1 = pd.read_csv(data, sep = ';', decimal=',',  index_col=['Nome da Microregião'], encoding='utf-8')

df1 = pd.DataFrame(dt1, columns=[   'Superior completo - Amarela',
                                    'Superior completo - Branca',
                                    'Superior completo - Indígena',
                                    'Superior completo - Parda',
                                    'Superior completo - Preta'])

df2 = pd.DataFrame(dt1, columns=[   'incompleto - Amarela',
                                    'Incompleto - Branca',
                                    ' incompleto - Indígena',
                                    'incompleto - Parda',
                                    'Incompleto - Preta',
                                    'Superior completo - Amarela',
                                    'Superior completo - Branca',
                                    'Superior completo - Indígena',
                                    'Superior completo - Parda',
                                    'Superior completo - Preta'])

#print(df2[' incompleto - Indígena'].max())

grouped = df1.groupby('Nome da Microregião').sum().max()
#print (list(grouped.to_dict().values()))

grouped_keys = df1.groupby('Nome da Microregião').sum().idxmax(0)
#print(grouped_keys.to_list())

x_desc = [' / '.join(z) for z in zip(list(grouped.to_dict().keys()), grouped_keys.to_list())]
x_desc_2 = [' / '.join(z) for z in zip(x_desc, list(map(str,map(int,grouped.to_dict().values()))))]

print(list(map(int,grouped.to_dict().values())))

plt.bar(x_desc_2, list(map(int,grouped.to_dict().values())))
plt.xticks(rotation=30, ha='right')
plt.xlabel('Nível Superiror - Raça / Maior Microregião')
plt.title('Maiores Microregiores por Escolaridade e Raça')
plt.yticks([])
plt.tight_layout()
#plt.show()