from OO.FonteDados import *
from OO.CampeonatoBrasileiro import *
from OO.CampeonatoBrasileiroEstatisticas import *
from OO.DestinoDados import *


cbe = CampeonatoBrasileiroEstatisticas()
print ("Entre 2003 e 2020 " + cbe.time_analisado + " teve " + str(cbe.vitoriasMandante()) + " vitórias como mandante.")
print ("Entre 2003 e 2020 " + cbe.time_analisado + " teve " + str(cbe.vitoriasVisitante()) + " vitórias como visitante.")


dd = DestinoDados(cbe.lista_jogos_mandante,"../","vitorias_mandante.txt")
dd.populaArquivo()
print("O arquivo " + dd.endereco_arquivo + " foi gerado com as informações dos jogos vencidos como mandante")

dd = DestinoDados(cbe.lista_jogos_visitante,"../","vitorias_visitante.txt")
dd.populaArquivo()
print("O arquivo " + dd.endereco_arquivo + " foi gerado com as informações dos jogos vencidos como visitante")

