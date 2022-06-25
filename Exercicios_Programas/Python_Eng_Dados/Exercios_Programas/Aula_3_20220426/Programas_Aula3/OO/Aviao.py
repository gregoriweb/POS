class Aviao():
    velocidade = None
    altitude = None
    modelo = None
    capacidade = None

    def __init__(self):
        self.velocidade = 0
        self.altitude = 0
        self.modelo = ''
        self.capacidade = 0

    def obter_velocidade(self):
        return self.velocidade

    def aumentar_velocidade(self, velocidade):
        self.velocidade += velocidade

    def obter_altitude(self):
        return self.altitude

    def obter_autitude(self):
        return self.altitude