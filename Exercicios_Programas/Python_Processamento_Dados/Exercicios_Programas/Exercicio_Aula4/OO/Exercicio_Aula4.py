'''
    Com base no arquivo em material de aula faça:
    a) Gerar um gráfico com  os 10 municípios mineiros com maior expectativa de vida.
    b) Gerar um gráfico com  os 10 municípios mineiros com menor expectativa de vida.
    c) Gerar um grafico com o municipio com maior expectativa.
    d) Gerar um grafico com o municipio com menor expectativa.
'''
import FonteDados
import OO.DestinoDados


class MunicipoExpectativa():

    def __init__(self):
        self.municipios = {}

    def expectativa_municipios (self, arquivo="MunicipiosExpectativa.txt"):
        fd = FonteDados()
        fd.vetorArquivo(arquivo)
        municipio={}
        
        for i in fd.dataset:
            cb = CampeonatoBrasileiro()
            cb.rodada           = i[0]
            cb.data_jogo        = i[1]
            cb.horario          = i[2]
            cb.dia_jogo         = i[3]
            cb.time_mandante    = i[4]
            cb.time_visitante   = i[5]
            cb.time_vencedor    = i[6]
            cb.campo            = i[7]
            cb.placar_mandante  = i[8]
            cb.placar_visitante = i[9]
            cb.estado_mandante  = i[10]
            cb.estado_visitante = i[11]
            cb.estado_vencedor  = i[12]
            cb.ano_campeonato   = i[1].split("/")[2]
            cb.linha_dados = i
            lista_jogos.append(cb)
        return lista_jogos

    def vitoriasMandante(self):
        for i in self.lista_jogos:
            if (i.time_mandante == self.time_analisado and i.time_vencedor == self.time_analisado):
                self.VitoriasMandante.append(i)
                self.QtdVitoriasMandante += 1
                self.lista_jogos_mandante.append(i.linha_dados)
        return self.QtdVitoriasMandante

    def vitoriasVisitante(self):
        for i in self.lista_jogos:
            if (i.time_visitante == self.time_analisado and i.time_vencedor == self.time_analisado):
                self.VitoriasVisitante.append(i)
                self.QtdVitoriasVisitante += 1
                self.lista_jogos_visitante.append(i.linha_dados)
        return self.QtdVitoriasVisitante