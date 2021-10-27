def amplitude(lista):
    print(f"\nLista Criada: {lista}")
    print(f"\nA amplitude eh: {max(lista) - min(lista)}")

valor=1
lst = []
while valor != 0:
    valor = int(input("\nDigite o valor: "))
    print(f"\nValores Inseridos!!") if valor <=0 else lst.append(valor)

amplitude(lst)