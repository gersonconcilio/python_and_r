def carga(weight):
    if weight <= 10:
        print(f"\nO valor será: R$50,00")
    elif weight >= 11 and weight <= 20:
        print(f"\nO valor será: R$80,00")
    elif weight > 20:
        print(f"\nTransporte Nao Aceito!!!!")

carga(float(input("\nDigite o peso da carga: ")))