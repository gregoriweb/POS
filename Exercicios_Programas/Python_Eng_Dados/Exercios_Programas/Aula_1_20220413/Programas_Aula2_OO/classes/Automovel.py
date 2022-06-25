class Automovel:
    ano_fabricacao = None
    modelo = None
    marca = None
    potencia = None
    numero_portas = None
    placa = None
    cor = None
    chassi = None
    
    
    
    def imprimir(self, a):
        print("Marca: " + a.marca)
        print("Modelo: " + a.modelo)
        print("Cor: " + a.cor)
        print("Ano Fabricacao: " + str(a.ano_fabricacao))
        print("Chassi : " + a.chassi)
        print("Placa: " + a.placa)