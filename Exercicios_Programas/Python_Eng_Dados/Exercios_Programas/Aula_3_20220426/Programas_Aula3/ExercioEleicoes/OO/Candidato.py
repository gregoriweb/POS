class Candidato():
    nome = None
    legenda = None
    numero = None
    cargoEletivo = None
    votos = None

    def __init__(self):
        self.nome = ""
        self.legenda = ""
        self.numero = 0
        self.cargo = ""

    def obtemNome(self):
        return self.nome
    
    def adicionaNome(self, nome):
        self.nome = nome

    def obtemLegenda(self):
        return self.legenda
    
    def adicionaLegenda(self, legenda):
        self.legenda = legenda

    def obtemNumero(self):
        return self.numero
    
    def adicionaNumero(self, numero):
        self.numero = numero

    def obtemCargoEletivo(self,cargoEletivo):
        return self.cargoEletivo
    
    def adicionaCargoEletivo(self, cargoEletivo):
        self.cargoEletivo = cargoEletivo

    def adicionaVoto(self, numeroCandidato):
        self.votos += 1