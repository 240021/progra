# Dominguez Castellanos Alejandro
numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
valor_maximo = max(numeros)
valor_minimo = min(numeros)
print(f"\nEl valor máximo es: {valor_maximo}")
print(f"El valor mínimo es: {valor_minimo}")