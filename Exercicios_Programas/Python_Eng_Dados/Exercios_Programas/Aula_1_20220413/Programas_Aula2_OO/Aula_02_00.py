from classes.Automovel import Automovel


a = Automovel()
a.ano_fabricacao = 2022
a.chassi = "HUHUHD202928A"
a.cor = "Preto"
a.marca = "Fiat"
a.modelo = "Palio"
a.numero_portas = 4
a.placa = "XPYO1234"
a.potencia = "80 CV"


a1 = Automovel()
a1.ano_fabricacao = 2000
a1.chassi = "HUHUHUHKBBB"
a1.cor = "Vermelho"
a1.marca = "Audi"
a1.modelo = "Q3"
a1.numero_portas = 4
a1.placa = "GYGY777"
a1.potencia = "250 CV"

a.imprimir(a)
a.imprimir(a1)