'''
3. Crie uma classe Elevador para armazenar as informações de um elevador de prédio. 
A classe deve armazenar o andar atual (térreo = 0), 
total de andares no prédio (desconsiderando o térreo), 
capacidade do elevador e quantas pessoas estão presentes nele. 
A classe deve também disponibilizar os seguintes métodos:

Inicializar: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
Entrar: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
Sair: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
Subir: para subir um andar (não deve subir se já estiver no último andar);
Descer: para descer um andar (não deve descer se já estiver no térreo);
Obs.: Encapsular todos os atributosdd da classe (criar os métodos set e get).
'''

from OO.Elevador import Elevador

e = Elevador()
e.setAndar_atual(10)
e.setCapacidade_elevador(8)
e.setQuantidade_pessoas(5)
e.setTotal_andares(10)

print("Capacidade do Elevador " + str(e.getCapacidade_elevador()))
print("Andar Atual " + str(e.getAndar_atual()))
print("Qtde de Pessoas no Elevador " + str(e.getQuantidade_pessoas()))
print("Total Andares " + str(e.getTotal_andares()))


#teste Descida
while e.getAndar_atual() > 0:
    e.Descer()
    print ("Descendo: "+ str(e.getAndar_atual()))



#teste Subida
while e.getAndar_atual() < e.getTotal_andares():
    e.Subir()
    print ("Subindo: "+ str(e.getAndar_atual()))

#teste Saida
while e.getQuantidade_pessoas() > 0:
    e.Sair()
    print ("Saindo: "+ str(e.getQuantidade_pessoas()))

#teste Entrada
while e.getQuantidade_pessoas() < e.getCapacidade_elevador():
    e.Entrar()
    print ("Entrando: "+ str(e.getQuantidade_pessoas()))

