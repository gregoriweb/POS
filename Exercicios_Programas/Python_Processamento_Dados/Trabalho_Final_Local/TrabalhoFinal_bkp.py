from pathlib import Path
from turtle import position
from matplotlib import pyplot as plt
import pandas as pd


#Código IBGE do Município;Nome das Grandes Regiões;Nome da Microregião;incompleto - Amarela;Incompleto - Branca; 
#incompleto - Indígena;incompleto - Parda;Incompleto - Preta;Superior completo - Amarela;Superior completo - Branca;
#Superior completo - Indígena;Superior completo - Parda;Superior completo - Preta

#Código IBGE do Município;
# Nome das Grandes Regiões;
# Nome da Microregião;
# incompleto - Amarela;
# Incompleto - Branca;
#  incompleto - Indígena;
# incompleto - Parda;
# Incompleto - Preta;
# Superior completo - Amarela;
# Superior completo - Branca;
# Superior completo - Indígena;
# Superior completo - Parda;
# Superior completo - Preta


# print (Path(__file__).parent)
# 
# print('{}/{}'.format(Path(__file__).parent,'IBGE_Escolar.csv'))

# with open('{}/{}'.format(Path(__file__).parent,'IBGE_Escolar.csv'), 'r', encoding='utf-8') as filehandle:
#     for line in filehandle:
#         print(line)


#Nome da Microregião;incompleto - Amarela;Incompleto - Branca; 
#incompleto - Indígena;incompleto - Parda;Incompleto - Preta;Superior completo - Amarela;Superior completo - Branca;
#Superior completo - Indígena;Superior completo - Parda;Superior completo - Preta


# incompleto - Amarela;Incompleto - Branca; 
# ,'incompleto - Indígena','incompleto - Parda','Incompleto - Preta','Superior completo - Amarela','Superior completo - Branca','Superior completo - Indígena','Superior completo - Parda','Superior completo - Preta'


file_path = '{}/{}'.format(Path(__file__).parent,'IBGE_Escolar.csv')
data = open(file_path, 'r', encoding='utf-8')


#        print (data)
#
#        #dt = pd.read_csv(data, sep = ';', decimal=',', index_col='Nome da Microregião')
#        dt = pd.read_csv(data, sep = ';', decimal=',', index_col='Nome da Microregião')
#        #df = pd.DataFrame(dt.nlargest(1,'Nome da Microregião'), columns=['incompleto - Amarela','Incompleto - Branca','incompleto - Indígena','incompleto - Parda','Incompleto - Preta','Superior completo - Amarela','Superior completo - Branca','Superior completo - Indígena','Superior completo - Parda','Superior completo - Preta'])
#
#
#        df = pd.DataFrame(dt, columns=['incompleto - Amarela','Incompleto - Branca','incompleto - Indígena','incompleto - Parda','Incompleto - Preta','Superior completo - Amarela','Superior completo - Branca','Superior completo - Indígena','Superior completo - Parda','Superior completo - Preta'])
#        df.groupby('Nome da Microregião').sum()
#        print (df)


dt1 = pd.read_csv(data, sep = ';', decimal=',',  index_col=['Nome da Microregião'], encoding='utf-8')
df1 = pd.DataFrame(dt1, columns=['incompleto - Amarela','Incompleto - Branca',' incompleto - Indígena','incompleto - Parda','Incompleto - Preta','Superior completo - Amarela','Superior completo - Branca','Superior completo - Indígena','Superior completo - Parda','Superior completo - Preta'])


print(df1[' incompleto - Indígena'].max())

#df1 = pd.DataFrame(dt1, columns=['incompleto - Amarela'])
#df1 = df1.groupby('Nome da Microregião').sum().max()
#df1 = df1.groupby('Nome da Microregião').sum().max()


#df_fim = df1.groupby('Nome da Microregião')['incompleto - Amarela'].sum().max()
#df_fim2 = df1.groupby('Nome da Microregião').sum().max()

grouped = df1.groupby('Nome da Microregião').sum().max()
print (list(grouped.to_dict().values()))

grouped_keys = df1.groupby('Nome da Microregião').sum().idxmax(0)
print(grouped_keys.to_list())



C = [' / '.join(z) for z in zip(list(grouped.to_dict().keys()), grouped_keys.to_list())]
C2 = [' / '.join(z) for z in zip(C, list(map(str,map(int,grouped.to_dict().values()))))]

print (C)
#print(df1.groupby('Nome da Microregião').sum().idxmax(0))
#print(df1.groupby('Nome da Microregião').sum().max())

#list(df_fim)

#df1.groupby('Nome da Microregião').sum().max().plot(kind='bar')

#plots = df1.groupby('Nome da Microregião').sum().max()


print(C)
print(list(map(int,grouped.to_dict().values())))



print("-------------------------")

plt.bar(C2, list(map(int,grouped.to_dict().values())))
#plt.plot(C, list(grouped.to_dict().values()))
plt.xticks(rotation=30, ha='right')
#plt.xticks(C2, rotation=30, ha='right')
plt.xlabel('Nível Superiror - Raça / Maior Microregião')
plt.title('Maiores Microregiores por Escolaridade e Raça')
#plt.yticks(list(map(int,grouped.to_dict().values())), C2, rotation=45)
plt.yticks([])
plt.tight_layout()
#plt.bar_label()
#df1.plot(x=0, y=1, kind = 'bar')
plt.show()


#plt.barh(list(df_fim.keys()), df_fim.values())

#plt.gca().invert_yaxis()
#plt.savefig(nome_arquivo, format='png')
#plt.show()
#plt.close()


#df1 = pd.DataFrame(dt1, columns=['Nome da Microregião'])
#print(df1.max().to_frame().T)
#df1=df1.groupby('Nome da Microregião').max()
#print(df1.idxmax(0))
#print (df1)

#df.pivot_table()

# print (df.groupby('Nome da Microregião').sum())


# pd.pivot_table(df, values='D', index=['A', 'B'],
#                     columns=['C'], aggfunc=np.sum)


#df = pd.DataFrame(dt, columns=['Nome da Microregião'])
#df = pd.DataFrame(dt.nlargest(1,['incompleto - Amarela','Incompleto - Branca','incompleto - Indígena','incompleto - Parda','Incompleto - Preta','Superior completo - Amarela','Superior completo - Branca','Superior completo - Indígena','Superior completo - Parda','Superior completo - Preta']), columns=['Nome da Microregião'])
#print(df.max())

#print (dt.nlargest(10, 'Código IBGE do Município'))

#print ("")
#print (dt.nlargest(5, 'Mortalidade infantil'))

#
#df = pd.DataFrame(dt.nlargest(5, 'Mortalidade infantil'), columns=['Município','Mortalidade infantil'])
#df.plot(x='Município', y='Mortalidade infantil', kind = 'bar')
#plt.show()
#
#df = pd.DataFrame(dt.nlargest(5, 'Esperança de vida ao nascer'), columns=['Município','Esperança de vida ao nascer'])
#df.plot(x='Município', y='Esperança de vida ao nascer', kind = 'bar')
#plt.show()