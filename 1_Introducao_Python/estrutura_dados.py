#TIPOS DE LISTAS E COMO SAO FEITAS
print(f"\n---------------Listas---------------\n")
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, "4", True]
lst3 = [12, [1, 2, 3, 4, 5], "a"]
lst4 = list(range(0, 10))

print(lst1)
print(lst2)
print(lst3)
print(lst4)
print(lst4[0])
print(f"O tamano da lst4 eh: {len(lst4)}")
for i in range(0, len(lst4)):
    print(lst4[i])
print(f"\n---------------Listas---------------\n")


#DICIONARIOS ------ CHAVE E VALOR ASSOCIADOS
print(f"\n---------------Dicionarios---------------\n")
dic1 = {"Lapis": 5.5, "Borracha": 7.0, "Caneta": 6.5}

print(dic1.keys())
print(dic1.values())
print("Calculadora" in dic1)
print(dic1)

del dic1["Borracha"]
print(dic1)
dic1["Calculadora"] = 17.5
print(dic1)
print(f"\n---------------Dicionarios---------------\n")


#SETS  ------ NAO ORDENADOS E NAO REPETIDOS
print(f"\n---------------Sets---------------\n")
animais = {"gato", "cachorro"}
print(animais)

print("gato" in animais)
animais.add("lebre")
print(animais)
print(len(animais))
print(f"\n---------------Sets---------------\n")


#TUPLAS ------ LISTAS QUE NÃO PODEM SER ALTERADAS
print(f"\n---------------Tupla---------------\n")
tupla = (1, 2, 3, 4, 5, 6)

print(tupla)
print(f"\n---------------Tupla---------------\n")

#DICIONARIO DE TUPLAS -------------------
print(f"\n---------------Dicionario de Tupla---------------\n")
dic2 = {(0, 1): 1, (1, 2): 2, (2, 3): 3, (3, 4): 4}
print(dic2)
print(f"\n---------------Dicionario de Tupla---------------\n")