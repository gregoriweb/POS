'''
5) Escreva a classe ConversaoDeUnidadesDeArea com métodos estáticos para conversão das unidades de área segundo a lista abaixo.

     a) 1 metro quadrado = 10.76 pés quadrados

     b) 1 pé quadrado = 929 centímetros quadrados

    c) 1 milha quadrada = 640 acres

    d) 1 acre = 43.560 pés quadrados
'''

class ConversaoDeUnidadesDeArea:

    def metro_quadrado_pes(medida_metro):
        medida_pes = medida_metro * 10.76
        return medida_pes

    def pe_quadrado_cm(medida_pes):
        medida_cm = medida_pes * 929
        return medida_cm
    
    def pe_quadrado_m(medida_pes):
        medida_m = medida_pes * 0.0929
        return medida_m

    def milha_quadrada_acre(medida_milha):
        medida_acre = medida_milha * 640
        return medida_acre

    def acre_milha_quadrada(medida_acres):
        medida_milha = medida_acres / 640
        return medida_milha
    
    def acre_pes_quadrado(medida_acre):
        medida_pes = medida_acre * 43560
        return medida_pes

    def pe_quadrado_acre(medida_pes):
        medida_acre = medida_pes / 43560
        return medida_acre


# Teste Objeto:
# ---------------- ACRES
print("Acres para milhas:")
print(ConversaoDeUnidadesDeArea.acre_milha_quadrada(10))

print("Acres para pes:")
print(ConversaoDeUnidadesDeArea.acre_pes_quadrado(10))

print("Acres para metros:")
print(ConversaoDeUnidadesDeArea.pe_quadrado_m( ConversaoDeUnidadesDeArea.acre_pes_quadrado(10) ) )

# ---------------- MILHAS
print("Milhas para Acres:")
print( ConversaoDeUnidadesDeArea.milha_quadrada_acre(10) )

print("Milhas para Pes:")
print( ConversaoDeUnidadesDeArea.acre_pes_quadrado(ConversaoDeUnidadesDeArea.milha_quadrada_acre(0.13)) )

print("Milhas para Metros:")
print( ConversaoDeUnidadesDeArea.pe_quadrado_m( ConversaoDeUnidadesDeArea.acre_pes_quadrado(ConversaoDeUnidadesDeArea.milha_quadrada_acre(0.13))) )


# ---------------- PES
print("Pes para Acres:")
print( ConversaoDeUnidadesDeArea.pe_quadrado_acre(10)  )

print("Pes para Milhas:")
print(ConversaoDeUnidadesDeArea.acre_milha_quadrada(ConversaoDeUnidadesDeArea.pe_quadrado_acre(10)) )

print("Pes para Metros:")
print( ConversaoDeUnidadesDeArea.pe_quadrado_m(10) )


# ---------------- METROS
print("Metros para Acres:")
print( ConversaoDeUnidadesDeArea.pe_quadrado_acre(ConversaoDeUnidadesDeArea.metro_quadrado_pes(10) ) )

print("Metros para Pes:")
print( ConversaoDeUnidadesDeArea.metro_quadrado_pes(10) )

print("Metros para Milhas:")
print( ConversaoDeUnidadesDeArea.acre_milha_quadrada(ConversaoDeUnidadesDeArea.pe_quadrado_acre(ConversaoDeUnidadesDeArea.metro_quadrado_pes(10))) )