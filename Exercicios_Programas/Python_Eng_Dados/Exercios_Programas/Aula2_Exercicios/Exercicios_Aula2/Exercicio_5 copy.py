'''
5) Escreva a classe ConversaoDeUnidadesDeArea com métodos estáticos para conversão das unidades de área segundo a lista abaixo.

     a) 1 metro quadrado = 10.76 pés quadrados

     b) 1 pé quadrado = 929 centímetros quadrados

    c) 1 milha quadrada = 640 acres

    d) 1 acre = 43.560 pés quadrados
'''

class ConversaoDeUnidadesDeArea:
    
    
    ref_metro = 1
    ref_pe_quadrado = 929 * 0.0001
    ref_metro_quadrado = 10.76 * ref_pe_quadrado
    ref_acre = 43560 * ref_pe_quadrado
    ref_milha_quadrada = 640 * ref_acre

    def metro_quadrado(medida):
        metro_unidade = "m²"
        pes_quadrados = medida * (929 * 0.0001)
        metros_quadrados = 10.76 * pes_quadrados
        return metros_quadrados
    
    def pe_quadrado(medida):
        pes = medida * (929 * 0.0001)
        return pes

    def milha_quadrada(medida):
        unidade_pe = "mi²"
        pe_quadrado = medida * (929 * 0.0001)
        acre = 43560 * pe_quadrado
        milha_quadrada = 60 * acre
        return milha_quadrada
    
    def acre(medida):
        unidade_acre = "ac"
        pe_quadrado = medida * (929 * 0.0001)
        acre = 43560 * pe_quadrado
        return acre



    def metro_quadrado_2(medida):
        metro_unidade = "m²"
        metros = medida * ConversaoDeUnidadesDeArea.ref_metro_quadrado
        return metros
    
    def pe_quadrado_2(medida):
        pes = medida * ConversaoDeUnidadesDeArea.ref_pe_quadrado
        return pes

    def milha_quadrada_2(medida):
        unidade_pe = "mi²"
        milha_quadrada = medida * ConversaoDeUnidadesDeArea.ref_milha_quadrada
        return milha_quadrada
    
    def acre_2(medida):
        unidade_acre = "ac"
        acre = medida * ConversaoDeUnidadesDeArea.ref_acre
        return acre




medida_original = int(input("Digite o valor que será convertido (apenas numero): "))

unidade_original = int(input(
'''
Selecione a unidade de medida original:

1) Acres
2) Milhas
3) Pes
4) Metros

'''))

unidade_destino = int(input(
'''
Selecione a unidade de medida de destino:

1) Acres
2) Milhas
3) Pes
4) Metros

'''))

if (unidade_original == 1):
    unidade_original = "ac"
    valor_original = ConversaoDeUnidadesDeArea.acre(medida_original)

if (unidade_original == 2):
    unidade_original = "mi²"
    valor_original = ConversaoDeUnidadesDeArea.milha_quadrada(medida_original)

if (unidade_original == 3):
    unidade_original = "ft²"
    valor_original = ConversaoDeUnidadesDeArea.pe_quadrado(medida_original)

if (unidade_original == 4):
    unidade_original = "m²"
    valor_original = ConversaoDeUnidadesDeArea.metro_quadrado(medida_original)



# if (unidade_destino == 1):
#     unidade_original = "ac"
#     valor_convertido = ConversaoDeUnidadesDeArea.acre(valor_original)
# 
# if (unidade_destino == 2):
#     unidade_original = "mi²"
#     valor_convertido = ConversaoDeUnidadesDeArea.milha_quadrada(valor_original)
# 
# if (unidade_destino == 3):
#     unidade_original = "ft²"
#     valor_convertido = ConversaoDeUnidadesDeArea.pe_quadrado(valor_original)
# 
# if (unidade_destino == 4):
#     unidade_original = "m²"
#     valor_convertido = ConversaoDeUnidadesDeArea.metro_quadrado(valor_original)


if (unidade_destino == 1):
    unidade_original = "ac"
    valor_convertido = ConversaoDeUnidadesDeArea.acre(medida_original)

if (unidade_destino == 2):
    unidade_original = "mi²"
    valor_convertido = ConversaoDeUnidadesDeArea.milha_quadrada(medida_original)

if (unidade_destino == 3):
    unidade_original = "ft²"
    valor_convertido = ConversaoDeUnidadesDeArea.pe_quadrado(medida_original)

if (unidade_destino == 4):
    unidade_original = "m²"
    valor_convertido = ConversaoDeUnidadesDeArea.metro_quadrado(medida_original)

print ("unidade_original: "+ str(unidade_original))
print ("unidade_destino: "+ str(unidade_destino))
print()
print ("valor_original: "+ str(valor_original))
print()
print ("medida_original: "+ str(medida_original))
print ("valor_convertido_unidade: "+ str(unidade_original))
print()
print ("valor_convertido: "+ str(valor_convertido))
print ("valor_convertido_unidade: "+ str(unidade_original))





print( ConversaoDeUnidadesDeArea.acre(10) )