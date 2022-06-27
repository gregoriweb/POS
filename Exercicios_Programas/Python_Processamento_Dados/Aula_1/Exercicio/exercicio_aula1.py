'''
1) Crie uma matriz NumPy vazia e uma completa.
2) Crie uma matriz Numpy preenchida com todos os zeros
3) Crie uma matriz Numpy preenchida com todos os um
4) Verifique se um array Numpy contém uma linha especificada
5) Encontre o número de ocorrências de uma sequência em uma matriz NumPy
6) Encontre o valor mais frequente em uma matriz NumPy
7) Combinando Array NumPy unidimensional e bidimensional
8) Como construir um array de todas as combinações de dois arrays NumPy?
9) Como comparar dois arrays NumPy?
10) Crie um exemplo de grafico com a biblioteca Numpy
'''
from dis import code_info
import numpy as np

#1) Crie uma matriz NumPy vazia e uma completa.
matriz_vazia = np.array([])
matriz_completa = np.array([4,3,7,-9,1])


'''
2) Crie uma matriz Numpy preenchida com todos os zeros
'''
matriz_zeros = (np.zeros(10))

'''
3) Crie uma matriz Numpy preenchida com todos os um
'''
matriz_ones = (np.ones(10))

'''
4) Verifique se um array Numpy contém uma linha especificada
'''
#encontra 100 em matriz_ones
np.isin(matriz_ones, 100).any

'''
5) Encontre o número de ocorrências de uma sequência em uma matriz NumPy
'''
print(len(np.isin(matriz_ones, 1)))

#unique, counts = np.unique(np.isin(matriz_ones, 1), return_counts=True)
#print (unique[np.argmax(counts)])

#matriz_teste = [1,2,2,3,3,3,4,4,4,4]
#matriz_teste_2 = [1,1,1,1,2,2,2,3,3,4]
#u, c = np.unique(matriz_teste_2, return_counts=True)
#print (u[c.argmax()])


'''
6) Encontre o valor mais frequente em uma matriz NumPy
'''
matriz_teste = [1,2,2,3,3,3,4,4,4,4]
matriz_teste_2 = [1,1,1,1,2,2,2,3,3,4]
u, c = np.unique(matriz_teste_2, return_counts=True)
print ( u[c.argmax()])


'''
7) Combinando Array NumPy unidimensional e bidimensional
'''
#matriz_teste = np.array([1,2,2,3,3,3,4,4,4,4])
#matriz_teste_2 = np.array([[1,1,1,1,2][2,2,3,3,4]])
#np.nditer([matriz_teste, matriz_teste_2])


'''
8) Como construir um array de todas as combinações de dois arrays NumPy?
'''

'''
9) Como comparar dois arrays NumPy?
'''

'''
10) Crie um exemplo de grafico com a biblioteca Numpy
'''