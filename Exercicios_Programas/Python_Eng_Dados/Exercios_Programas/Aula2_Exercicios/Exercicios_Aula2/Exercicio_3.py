'''
3) Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura.

   a) Crie  um método para imprimir os dados de uma pessoa.
'''

class Pessoa:

    def __init__(self):
        self.nome = "Joao"
        self.idade = "32"
        self.altura = 1.70

    def mostra_pessoa(self):
        print("Nome da Pessoa: " + self.nome)
        print("Idade da Pessoa: " + self.idade)
        print("altura da Pessoa: " + str( self.altura) )


# Teste do Objeto:
pessoa = Pessoa()
pessoa.mostra_pessoa()
