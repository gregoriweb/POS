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

        

    def ligar(self):

        print("Carro Ligado ....")

        

    def desligar(self):

        print("Carro desligando ....")

         

    def frear(self):

        print("Carro Freiando ....")    

        

    def travarPortas(self):

        print("Carro travando as portas ....")

    

    def acelerar(self):

        print("Carro acelerando ....")




lista = []



for x in range(2):

    a = Automovel()

    a.ano_fabricacao = int(input("Informe o ano de Fabricação: "))

    a.chassi = input("Informe o Chassi: ")

    a.cor = input("Informe a Cor: ")

    a.marca = input("Informe a Marca: ")

    a.modelo = input("Informe o modelo: ")

    a.numero_portas = int(input("Informe o numero de Portas: "))

    a.placa = input("Informe a Placa: ")

    a.potencia = input("Informe a potência: ")

    lista.append(a)



for a in lista:

    a.imprimir(a)

    a.ligar()

    a.frear()

    a.acelerar()

    a.desligar()

    a.travarPortas()

    print(" ****************  ")