#FUNCOES PADROES/SEM BIBLIOTECA
print(f"\nValor Absoluto de -200 eh: {abs(-200)}")
lst = [1, 2, 30, 30, 45]
print(f"\nLista: {lst}")
print(f"\nMaior Valor da Lista: {max(lst)}")
print(f"\nMenor Valor da Lista: {min(lst)}")
print(f"\nSoma dos Valores da Lista: {sum(lst)}")
print(f"\nO arredondamento do valor 2.34567 em duas casas eh: {round(2.34567, 2)}")


#FUNCOES CONTIDADAS NO PACOTE STATISTICS
from statistics import *
print(f"\nMedia da Lista: {mean(lst)}")
print(f"\nMediana da Lista: {median(lst)}")
print(f"\nModa da Lista: {mode(lst)}")
print(f"\nDesvio Padrão da Lista: {stdev(lst)}")
print(f"\nVariancia da Lista: {variance(lst)}")


#FUNCAO VALORES ALEATORIOS NUMPY
from numpy import *
a = random.random((3, 3))
print(f"\nValores a: \n{a}")
print(type(a))