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
Obs.: Encapsular todos os atributos da classe (criar os métodos set e get).
'''

class Elevador():

    def _init_(self):
        self.__andar_atual = 0
        self.__total_andares = 0
        self.__capacidade_elevador = 0
        self.__quantidade_pessoas = 0

    def setAndar_atual(self, andar_atual):
        self.__andar_atual = andar_atual

    def getAndar_atual(self):
        return int(self.__andar_atual)

    def setTotal_andares(self, total_andares):
        self.__total_andares = total_andares

    def getTotal_andares(self):
        return self.__total_andares

    def setCapacidade_elevador(self, capacidade_elevador):
        self.__capacidade_elevador = capacidade_elevador

    def getCapacidade_elevador(self):
        return self.__capacidade_elevador

    def setQuantidade_pessoas(self, quantidade_pessoas):
        self.__quantidade_pessoas = quantidade_pessoas

    def getQuantidade_pessoas(self):
        return self.__quantidade_pessoas

# Entrar, Sair,Subir , Descer

    def Entrar (self):
        if self.getQuantidade_pessoas() < self.getCapacidade_elevador():
            self.setQuantidade_pessoas(self.getQuantidade_pessoas()+1)
        else:
            return

    def Sair (self):
        if self.getQuantidade_pessoas() > 0:
            self.setQuantidade_pessoas(self.getQuantidade_pessoas()-1)
        else:
            return
    
    def Subir (self):
        if self.getAndar_atual() < self.getTotal_andares():
            self.setAndar_atual(self.getAndar_atual()+1)
        else:
            return

    def Descer (self):
        if self.getAndar_atual() > 0:
            self.setAndar_atual(self.getAndar_atual()-1)
        else:
            return
    