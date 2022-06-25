'''
4) Crie uma classe Televisao e uma classe ControleRemoto que pode controlar o volume e trocar os canais da televisão.

    O controle de volume permite: 
    
     a)  aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;

     b) aumentar e diminuir o número do canal em uma unidade

     c) trocar para um canal indicado;
     
     d) consultar o valor do volume de som e o canal selecionado.
'''


class Televisao:

    def __init__(self):
        self.canal = 12
        self.volume = 10

class ControleRemoto:

    def __init__(self,televisao = Televisao()):
        print("TV LIGADA")
        self.motra_valores()

    def diminui_canal(self):
        print("CANAL")
        if televisao.canal > 1:
            televisao.canal -= 1
        self.motra_valores()

    def aumenta_canal(self):
        print("CANAL")
        if televisao.canal < 99:
            televisao.canal += 1
        self.motra_valores()


    def diminui_volume(self):
        print("VOLUME")
        if televisao.volume > 1:
            televisao.volume -= 1
        self.motra_valores()

    def aumenta_volume(self):
        print("VOLUME")
        if televisao.volume < 99:
            televisao.volume += 1
        self.motra_valores()

    def define_canal(self):
        canal = input("DIGITE O CANAL: ")
        if televisao.canal < 99:
            televisao.canal = int(canal)
        self.motra_valores()

    def motra_valores(self):
        print("Canal:" + str(televisao.canal))
        print("Volume:" + str(televisao.volume))


# Teste Objeto:

televisao = Televisao()
controle = ControleRemoto(televisao)


while (True):
    comando = input('''
            1) Mostrar Valores de Canal e Volume
            2) Digitar canal
            3) Canal +
            4) Canal -
            5) Volume +
            6) Volume -
        ''')
    

    if (comando == "1" ):
        controle.motra_valores()

    if (comando == "2" ):
        controle.define_canal()

    if (comando == "3" ):
        controle.aumenta_canal()

    if (comando == "4" ):
        controle.diminui_canal()

    if (comando == "5" ):
        controle.aumenta_volume()
        
    if (comando == "6" ):
        controle.diminui_volume()







