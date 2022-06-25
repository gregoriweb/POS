arquivo = open("notas.txt", "r")
linha1 = arquivo.readline()

print("Aluno:")
print(linha1)


linha2 = arquivo.readline()

print("Nota Av1:")
print(linha2)

linha3 = arquivo.readline()

print("Nota Av2:")
print(linha3)

arquivo.close()