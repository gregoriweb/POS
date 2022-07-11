'''
    Com base no arquivo em material de aula faça:
    a) Gerar um gráfico com  os 10 municípios mineiros com maior expectativa de vida.
    b) Gerar um gráfico com  os 10 municípios mineiros com menor expectativa de vida.
    c) Gerar um grafico com o municipio com maior expectativa.
    d) Gerar um grafico com o municipio com menor expectativa.
    https://note.nkmk.me/en/python-dict-list-sort/#:~:text=To%20sort%20a%20list%20of,the%20result%20of%20that%20function.
'''

from FonteDados import FonteDados
import matplotlib.pyplot as plt

class Municipio():

    def __init__(self):
        self.municipio = ""
        self.expectativa = 0.00


class MunicipioExpectativa():

    def __init__(self):
        self.municipios = {}

    def ev_municipios (self, arquivo="MunicipiosExpectativa.txt"):

        fd = FonteDados()
        fd.vetorArquivo(arquivo)
        lista_municipios = fd.dataset

        municipios = []

        for i in lista_municipios:
            mun = Municipio()
            mun.municipio = i[0]
            mun.expectativa = i[1]
            municipios.append(mun)

        return lista_municipios

    def ev_municipios_2 (self, arquivo="MunicipiosExpectativa.txt"):

        fd = FonteDados()
        fd.vetorArquivo(arquivo)
        lista_municipios = fd.dataset

        municipios = []

        for i in lista_municipios:
            mun = Municipio()
            mun.municipio = i[0]
            mun.expectativa = i[1]
            municipios.append(mun)

        return municipios

#    def ev_municipios_maiores(self, lista_municipios, itens): 
#        lista_municipios.sort(key=lambda expectativa: expectativa[1], reverse=True)
#        return lista_municipios[:itens]
#
#    def ev_municipios_menores(self, lista_municipios, itens): 
#        lista_municipios.sort(key=lambda expectativa: expectativa[1], reverse=False)
#        return lista_municipios[:itens]

    def ev_municipios_maiores_2(self, lista_municipios, itens):
        municipios = {}
        lista_municipios.sort(key=lambda expectativa: expectativa[1], reverse=True)
        for i in lista_municipios[:itens]:
            mun = Municipio()
            mun.municipio = i[0]
            mun.expectativa = i[1]
            municipios[i[0]] = float(i[1])
        
        return municipios
        

    def ev_municipios_menores_2(self, lista_municipios, itens):
        municipios = {}
        lista_municipios.sort(key=lambda expectativa: expectativa[1], reverse=False)
        for i in lista_municipios[:itens]:
            mun = Municipio()
            mun.municipio = i[0]
            mun.expectativa = i[1]
            municipios[i[0]] = float(i[1])
        
        return municipios




me = MunicipioExpectativa()

print (list(me.ev_municipios_maiores_2(me.ev_municipios(), 10)))
print (list(me.ev_municipios_maiores_2(me.ev_municipios(), 10).values()))

print (list(me.ev_municipios_menores_2(me.ev_municipios(), 10)))
print (list(me.ev_municipios_menores_2(me.ev_municipios(), 10).values()))

#plt.barh(list(me.ev_municipios_maiores_2(me.ev_municipios(), 10).keys()), list(me.ev_municipios_maiores_2(me.ev_municipios(), 10).values()))
plt.barh(list(me.ev_municipios_maiores_2(me.ev_municipios(), 10).keys()), list(me.ev_municipios_maiores_2(me.ev_municipios(), 10).values()))
plt.show()

plt.barh(list(me.ev_municipios_menores_2(me.ev_municipios(), 10)), list(me.ev_municipios_menores_2(me.ev_municipios(), 10).values()))
plt.show()

plt.barh(list(me.ev_municipios_maiores_2(me.ev_municipios(), 1).keys()), list(me.ev_municipios_maiores_2(me.ev_municipios(), 1).values()))
plt.show()

plt.barh(list(me.ev_municipios_menores_2(me.ev_municipios(), 1)), list(me.ev_municipios_menores_2(me.ev_municipios(), 1).values()))
plt.show()

plt.close()