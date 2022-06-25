from OO.CampeonatoBrasileiro import CampeonatoBrasileiro
from OO.FonteDados import FonteDados

class CampeonatoBrasileiroEstatisticas(CampeonatoBrasileiro):

    def __init__(self, time_analisado="São Paulo", lista_jogos=[]) -> None:
        super().__init__()
        
        if ( len(lista_jogos) > 0 ):
            self.lista_jogos = lista_jogos
        else:
            self.lista_jogos = self.jogos()
        
        self.lista_jogos_mandante = []
        self.lista_jogos_visitante = []

        self.time_analisado = time_analisado
        self.QtdVitoriasMandante = 0
        self.QtdVitoriasVisitante = 0
        self.QtdDerrotasMandante = 0
        self.QtdDerrotasVisitante = 0
        self.VitoriasMandante = []
        self.VitoriasVisitante = []
        self.DerrotasMandante = []
        self.DerrotasVisitante = []

    def jogos (self, arquivo="Jogos.txt"):
        fd = FonteDados()
        fd.vetorArquivo(arquivo)
        lista_jogos=[]
        
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