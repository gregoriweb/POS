'''
5) Escreva a classe ConversaoDeUnidadesDeArea com métodos estáticos para conversão das unidades de área segundo a lista abaixo.

     a) 1 metro quadrado = 10.76 pés quadrados

     b) 1 pé quadrado = 929 centímetros quadrados

    c) 1 milha quadrada = 640 acres

    d) 1 acre = 43.560 pés quadrados
'''

class ConversaoDeUnidadesDeArea:

    @staticmethod
    def metro_quadrado(medida):
        metro_unidade = "m²"
        metros = 10.76 * ConversaoDeUnidadesDeArea.pe_quadrado(medida)
        return str ( medida * metros  ) + metro_unidade
    
    @staticmethod
    def pe_quadrado(medida):
        unidade_quadrado = "ft²"
        pe_quadrado = 929 * (ConversaoDeUnidadesDeArea.metro_quadrado(medida) / 100)
        return str (medida * pe_quadrado) + unidade_quadrado

    @staticmethod
    def milha_quadrada(medida):
        unidade_pe = "mi²"
        milha_quadrada = 640 * ConversaoDeUnidadesDeArea.acres(medida)
        return str (medida * milha_quadrada) + unidade_pe
    
    @staticmethod
    def acre(medida):
        unidade_acre = "ac"
        acre = 43560 * ConversaoDeUnidadesDeArea.pe_quadrado(medida)
        return str(medida * acre) + unidade_acre

medida_original = input("Digite o valor que será convertido (apenas numero): ")

unidade_original = input(
'''
Selecione a unidade de medida original:

1) Acres
2) Milhas
3) Pes
4) Metros

''')

unidade_destino = input(
'''
Selecione a unidade de medida de destino:

1) Acres
2) Milhas
3) Pes
4) Metros

''')


if (unidade_destino == 1):
    unidade_original = "ac"
    valor_convertido = ConversaoDeUnidadesDeArea.acre(medida_original)

if (unidade_destino == 2):
    unidade_original = "mi²"
    valor_convertido = ConversaoDeUnidadesDeArea.valorConvertido.milha_quadrada(medida_original)

if (unidade_destino == 3):
    unidade_original = "ft²"
    valor_convertido = ConversaoDeUnidadesDeArea.valorConvertido.pe_quadrado(medida_original)

if (unidade_destino == 4):
    unidade_original = "m²"
    valor_convertido = ConversaoDeUnidadesDeArea.valorConvertido.metro_quadrado(medida_original)


print(ConversaoDeUnidadesDeArea.acre(10))


#print ("asdf "+unidade_original)
#print (valor_convertido)



#print ("O valor convertido é: " + valor_convertido )
