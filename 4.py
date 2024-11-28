# Dominguez Castellanos Alejandro 240021
letras = []
for i in range(5):
    letra = input(f"Ingrese la letra {i+1}: ")
    letras.append(letra)
letra_buscar = input("Ingrese la letra que desea buscar: ")
contador = letras.count(letra_buscar)
print(f"\nLa letra '{letra_buscar}' aparece {contador} veces en el arreglo.")