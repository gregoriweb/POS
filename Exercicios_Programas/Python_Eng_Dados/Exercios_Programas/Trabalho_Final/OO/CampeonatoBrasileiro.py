'''
Created on 16 de nov. de 2021

@author: nelsonjunior
'''

from datetime import date

class CampeonatoBrasileiro:
    rodada = None 
    data_jogo = None 
    horario = None 
    dia_jogo = None 
    time_mandante = None 
    time_visitante = None 
    time_vencedor = None 
    campo = None 
    placar_mandante = None 
    placar_visitante = None 
    estado_mandante = None 
    estado_visitante = None
    estado_vencedor = None 
    ano_campeonato = None 
    
    def __init__(self):
        self.data_jogo = ""
        self.campo = ""
        self.hora = ""
        self.time_mandante = ""
        self.time_visitante = ""
        self.time_vencedor = "" 
        self.campo = "" 
        self.placar_mandante = "" 
        self.placar_visitante = "" 
        self.estado_mandante = "" 
        self.estado_visitante = ""
        self.estado_vencedor = "" 
        self.ano_campeonato = ""