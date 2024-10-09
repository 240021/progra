#Alejandro Dominguez Castellanos Matricuela 240021
#Contador de digitos

n=int(input("Ingresa un número entero positivo: "))
conta=0
while n > 0:
    n //= 10  
    conta= conta+1  
print(f"El número tiene {conta} dígitos.")