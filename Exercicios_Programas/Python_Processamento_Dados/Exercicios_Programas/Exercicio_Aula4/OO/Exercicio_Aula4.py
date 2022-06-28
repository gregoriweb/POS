'''
    Com base no arquivo em material de aula faça:
    a) Gerar um gráfico com  os 10 municípios mineiros com maior expectativa de vida.
    b) Gerar um gráfico com  os 10 municípios mineiros com menor expectativa de vida.
    c) Gerar um grafico com o municipio com maior expectativa.
    d) Gerar um grafico com o municipio com menor expectativa.
'''
from FonteDados import FonteDados
#import OO.DestinoDados

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
        municipios = {}

        for i in fd.dataset:
            mun = Municipio()
            mun.municipio = i[0]
            mun.expectativa = i[1]
            municipios[mun.municipio] = mun.expectativa 
        return municipios

    def ev_municipios_top10 (self,municipios):
        return

me = MunicipioExpectativa()
me.ev_municipios()




#    def vitoriasMandante(self):
#        for i in self.lista_jogos:
#            if (i.time_mandante == self.time_analisado and i.time_vencedor == self.time_analisado):
#                self.VitoriasMandante.append(i)
#                self.QtdVitoriasMandante += 1
#                self.lista_jogos_mandante.append(i.linha_dados)
#        return self.QtdVitoriasMandante
#
#    def vitoriasVisitante(self):
#        for i in self.lista_jogos:
#            if (i.time_visitante == self.time_analisado and i.time_vencedor == self.time_analisado):
#                self.VitoriasVisitante.append(i)
#                self.QtdVitoriasVisitante += 1
#                self.lista_jogos_visitante.append(i.linha_dados)
#        return self.QtdVitoriasVisitante