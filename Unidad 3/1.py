# Dominguez Castellanos Alejandro
palabras = []
for i in range(5):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)
palabras.sort()
print("\nLas palabras ordenadas alfabéticamente son:")
for palabra in palabras:
    print(palabra)