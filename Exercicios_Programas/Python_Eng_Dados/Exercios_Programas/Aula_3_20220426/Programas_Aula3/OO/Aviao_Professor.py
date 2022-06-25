class Aviao():
    velocidade = None
    altitude = None
    modelo = None
    capacidade = None
    
    def __init__(self):
        self.altitude = 0
        self.velocidade = 0
        self.modelo = ""
        self.capacidade = 0
        
    def obter_velocidade(self):
        return self.velocidade
        
    def aumentar_velocidade(self, velocidade):
        self.velocidade += velocidade
        
    def obter_altitude(self):
        return self.altitude

