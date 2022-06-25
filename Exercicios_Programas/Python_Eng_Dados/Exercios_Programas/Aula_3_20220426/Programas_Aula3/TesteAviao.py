from OO.Aviao import Aviao


aviao = Aviao()
aviao.modelo = input("Favor informe o modelo do Avião: ")
aviao.capacidade = input("Favor informe a capacidade de passageiros Avião: ")
aviao.altitude = int(input("Favor informe a altitude Avião: "))
aviao.velocidade = int(input("Favor informe a velocidade do Avião: "))



print("Avião Modelo : " + aviao.modelo)
print("Capacidade : " + str(aviao.capacidade) + " passageiros.")
print("Altitude : " + str(aviao.altitude) + " pés.")
print("Velocidade : " + str(aviao.velocidade) + " km.")


velocidade = int(input("Informe a velocidade do Avião: "))
aviao.aumentar_velocidade(velocidade)
print("Altitude: " + str(aviao.obter_altitude()) + " pés." )
print("Velocidade: " + str(aviao.obter_velocidade()) + " km." )
