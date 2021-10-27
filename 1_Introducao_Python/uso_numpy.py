import numpy as np 

#MATRIZ UNIDIMENSIONAL
print(f"\n-----------------Array Unidimensional-----------------\n")
vet = np.array([12, 13, 14, 15, 16])
print(vet)
print(vet.dtype)
print(f"\n-----------------Array Unidimensional-----------------")


#CRIA UM ARRAY DE TIPO ESPECÍFICO
print(f"\n-----------------Array de Tipo Especifico-----------------\n")
vet_float = np.array([2, 3, 4, 5], dtype = np.float64)
print(vet_float)
print(type(vet_float))

vet_int = np.array([5, 6, 7], dtype = np.int32)
print(vet_int)
print(type(vet_int))
print(f"\n-----------------Array de Tipo Especifico-----------------")


#MUDAR O TIPO DO ARRAY
print(f"\n-----------------Mudando tipo do Array-----------------\n")
vet_float = np.array([3.22, 1.22, 3.22, 4.33])
print(vet_float)

vet_novo = vet_float.astype(np.int32)
print(vet_novo)
print(f"\n-----------------Mudando tipo do Array-----------------\n")


#ARRAY SEM REPETICOES E MOSTRANDO EM PARTES
print(f"\n-----------------Array sem Repeticoes & Mostrado em Partes-----------------\n")
array = np.array([12, 14, 13, 14, 13, 1, 14, 15, 16, 15, 2, 3, 4, 5, 6, 7, 8])
print(array)
array = np.unique(array)
print(array)

print(f"\n{array[1]}")
print(f"\n{array[:2]}")
print(f"\n{array[1:]}")
print(f"\n{array[-3:]}")
print(f"\n-----------------Array sem Repeticoes & Mostrado em Partes-----------------\n")


#MATRIZ BIDIMENSIONAL E Mostrando em Partes
print(f"\n-----------------Array Bidimensional e Mostrando em Partes-----------------\n")
mat = np.array([[4, 5], [6, 1], [7, 4]])
print(mat)

print(f"\n{mat[0 : 1, 0 : ]}")
print(f"\n{mat[ 1 : 2, 0 : ]}")
print(f"\n{mat[2 : 3, 0 : ]}")
print(f"\n{mat[0 : , 0 : 1]}")
print(f"\n{mat[0 : , 1 : 2]}")
print(f"\n-----------------Array Bidimensional e Mostrando em Partes-----------------")


#ARRAY JÁ INICIALIZADOS
print(f"\n-----------------Array Já Inicializado-----------------\n")
print(f"Inicializando Array Vazio: ")
vazio = np.empty([3, 3], dtype = int)
print(vazio)
print(f"------------\n")

print(f"Inicializando Array com Zeros: ")
zeros = np.zeros([3, 3])
print(zeros)
print(f"------------\n")

print(f"Inicializando Array com Uns: ")
uns = np.ones([3, 3])
print(uns)
print(f"------------\n")

print(f"Inicializando Array com Diagona Principal com Uns: ")
diag = np.eye(3)
print(diag)
print(f"------------")
print(f"\n-----------------Array Já Inicializado-----------------\n")


#NUMEROS ALEATORIOS 
print(f"\n-----------------Valores Aleatorios-----------------\n")
print(f"Valores Aleatorios Entre 0 e 1: ")
alea = np.random.random((5))
print(alea)
print(f"------------\n")

print(f"Valores Aleatorios Distribuicao Normal: ")
alea2 = np.random.randn((5))
print(alea2)
print(f"------------\n")

print(f"Matriz 3 x 4 com Aleatorios: ")
alea3 = np.random.random((3, 4))
print(alea3)
print(f"------------\n")

#ESSE GERADOR É INTERESSANTE!!!!!!!!!!!!!!!!
print(f"Gerando com Semente: ")
gnr = np.random.default_rng(1)
print(gnr)
ale5 = gnr.random(3)
print(ale5)
print(f"------------\n")

print(f"Gerando Inteiros: ")
ale6 = gnr.integers(10, size = (3, 4))
print(ale6)
print(f"------------\n")

print(f"Gerando Valores Inteiros 2: ")
v = np.random.randn(3, 4)
print(v)

x = (v > 0)
print(x)

z = np.where(x > 0, 1, -1)
print(z)
print(f"------------")
print(f"\n-----------------Valores Aleatorios-----------------\n")