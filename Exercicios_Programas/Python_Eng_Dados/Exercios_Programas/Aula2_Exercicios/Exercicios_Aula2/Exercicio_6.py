'''
6) Escreva um construtor para a classe Data que receba os valores correspondentes ao dia, mês e ano, e inicialize os campos da classe, verificando antes se a data é válida.
'''

class Data:
    def __init__(self, dia = int() , mes = int() , ano = int()):

        self.ano = None
        self.mes = None
        self.dia = None

        if (ano > 0 and ano <= 2999):
            self.ano = ano
            if (mes > 0 and mes <= 12):
                if (mes == 2):
                    if (ano%4==0 and dia > 0 and dia <= 29):
                        self.mes=mes
                        self.dia=dia
                    elif(dia > 0 and dia <= 28):
                        self.mes=mes
                        self.dia=dia
                elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
                    if (dia > 0 and dia <= 31):
                        self.mes=mes
                        self.dia=dia
                elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                    if (dia > 0 and dia <= 30):
                        self.mes=mes
                        self.dia=dia

        if (self.ano == None or self.mes == None or self.dia == None):
            self.datavalida = False
        else:
            self.datavalida = True
    


dia = int( input("Digite o dia: ") )
mes = int( input("Digite o mes: ") )
ano = int( input("Digite o ano: ") )

data = Data(dia,mes,ano)

if (data.datavalida):
    print (str(data.dia) + "/" + str(data.mes) + "/" + str(data.ano) )
else:
    print("Data Inválida")