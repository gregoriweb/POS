from FonteDados import FonteDados
import matplotlib.pyplot as plt

class Municipio():

    def __init__(self):
        self.municipio = ""
        self.expectativa = 0.00


class MunicipioExpectativa():

    def __init__(self):
        self.municipios = {}

    def ev_municipios_maiores(self, lista_municipios, itens):
        municipios = {}
        lista_municipios.sort(key=lambda expectativa: expectativa[1], reverse=True)
        for i in lista_municipios[:itens]:
            mun = Municipio()
            mun.municipio = i[0]
            mun.expectativa = i[1]
            municipios[i[0]] = float(i[1])
        
        return municipios
        

    def ev_municipios_menores(self, lista_municipios, itens):
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