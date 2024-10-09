#Alejandro Dominguez Castellanos Matricuela 240021
#Factorial de un numero

n=int(input("Ingresa el numero al cual deseas saber su factoria: "))
S=1
for n in range(n,1,-1):
 S=S*(n)
print(f"El resultado es {S}")