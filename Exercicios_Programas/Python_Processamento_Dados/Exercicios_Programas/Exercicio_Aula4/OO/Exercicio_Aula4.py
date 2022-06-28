'''
    Com base no arquivo em material de aula faça:
    a) Gerar um gráfico com  os 10 municípios mineiros com maior expectativa de vida.
    b) Gerar um gráfico com  os 10 municípios mineiros com menor expectativa de vida.
    c) Gerar um grafico com o municipio com maior expectativa.
    d) Gerar um grafico com o municipio com menor expectativa.
    https://note.nkmk.me/en/python-dict-list-sort/#:~:text=To%20sort%20a%20list%20of,the%20result%20of%20that%20function.
'''

from FonteDados import FonteDados


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

        print (type(lista_municipios))

        return lista_municipios

    def ev_municipios_maiores(self, lista_municipios, itens): 
        lista_municipios.sort(key=lambda expectativa: expectativa[1], reverse=True)
        return lista_municipios[:itens]

    def ev_municipios_menores(self, lista_municipios, itens): 
        lista_municipios.sort(key=lambda expectativa: expectativa[1], reverse=False)
        return lista_municipios[:itens]


# Teste:
me = MunicipioExpectativa()
for i in me.ev_municipios_x_maiores(me.ev_municipios(), 10):
    print (i)
for i in me.ev_municipios_x_menores(me.ev_municipios(), 10):
    print (i)