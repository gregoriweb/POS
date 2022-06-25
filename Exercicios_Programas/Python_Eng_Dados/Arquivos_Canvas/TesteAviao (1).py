'''
Created on 26 de abr. de 2022

@author: nelsonjunior
'''
from OO.Aviao import Aviao

lista = []
opcao = 0

while(True):
    print("")
    opcao = int(input("Cadastrado de Avião \n" + "1) Incluir " + "\n" 
                      + "2) Aumentar Velocidade" +  "\n" 
                      + "3) Obter Velocidade" +  "\n" + "4) Obter Altitude" 
                  +  "\n" + "5) Listar Aviões" +   "\n" + "6) Finalizar" "\n"))

    if(opcao > 6 or opcao < 1):
        print("Opcao Invalida ! ")
        continue
    
    if(opcao == 6):
        break
    
    if (opcao == 1):
        aviao = Aviao()
        aviao.modelo = input("Favor informe o modelo do Avião: ")
        aviao.capacidade = input("Favor informe a capacidade de passageiros Avião: ")
        aviao.altitude = int(input("Favor informe a altitude Avião: "))
        aviao.velocidade = int(input("Favor informe a velocidade do Avião: "))
        lista.append(aviao)
    
    if(opcao == 2):
        cont = 0
        for dados in lista:
            cont += 1
            print(str(cont) +  ") Avião Modelo : " + dados.modelo)
        
        aviao_selecionado = int(input("Escolha qual aviao deseja aumentar a velocidade: "))
        aviao_selecionado = aviao_selecionado - 1
        velocidade = int(input("Favor informe a velocidade que deseja aumentar do " + lista[aviao_selecionado].modelo))
        aviao = lista[aviao_selecionado]
        aviao.aumentar_velocidade(velocidade)
        lista[aviao_selecionado] = aviao
        
    if(opcao == 3):
        cont = 0
        for dados in lista:
            cont += 1
            print(str(cont) +  "Avião Modelo : " + dados.modelo)
        
        aviao_selecionado = int(input("Escolha qual aviao deseja obter a velocidade: "))
        aviao_selecionado = aviao_selecionado - 1
        aviao = lista[aviao_selecionado]
        print("Velocidade : " + str(aviao.obter_velocidade()) + " km.")
        
        
    if(opcao == 4):
        cont = 0
        for dados in lista:
            cont += 1
            print(str(cont) +  "Avião Modelo : " + dados.modelo)
        
        aviao_selecionado = int(input("Escolha qual aviao deseja obter a Altitude: "))
        aviao_selecionado = aviao_selecionado - 1
        aviao = lista[aviao_selecionado]
        print("Altitude : " + str(aviao.obter_altitude()) + " pés.")

    if(opcao == 5):
        for dados in lista:
            print("Avião Modelo : " + dados.modelo)
            print("Capacidade : " + str(dados.capacidade) + " passageiros.")
            print("Altitude : " + str(dados.altitude) + " pés.")
            print("Velocidade : " + str(dados.velocidade) + " km.")
            print(" ######")
