# Dominguez Castellanos Alejandro 240021
numeros = []
for i in range(6):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
if numeros == sorted(numeros):
    print("\nEl arreglo está ordenado de menor a mayor.")
else:
    print("\nEl arreglo NO está ordenado de menor a mayor.")