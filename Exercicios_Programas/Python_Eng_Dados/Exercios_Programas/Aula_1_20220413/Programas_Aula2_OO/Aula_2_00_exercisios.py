from classes.Automovel import Automovel


carros = {}

for i in range (2):
    carros[i] = Automovel()
    carros[i].ano_fabricacao = input("Insira o ano de fabricação do carro " + str(i) + ": " )
    carros[i].modelo = input("Insira a modelo do carro " + str(i) + ": " )
    carros[i].marca = input("Insira a marca do carro " + str(i) + ": " )
    carros[i].numero_portas = input("Insira a numero_portas do carro " + str(i) + ":" )
    carros[i].placa = input("Insira a placa do carro " + str(i) + ":" )
    carros[i].cor = input("Insira a cor do carro " + str(i) + ":" )
    carros[i].chassi = input("Insira a chassi do carro " + str(i) + ":" )

for i in carros:
    print (carros[i].ano_fabricacao)
 



