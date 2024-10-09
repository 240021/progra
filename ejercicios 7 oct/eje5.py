#Alejandro Dominguez Castellanos Matricula 240021
#Secuencia de fibonacci

N=int(input("Ingresa una numero: "))
A=0
B=1
R=0
for N in range(0,N):
 print(f"{A}", end=" ")
 R=(A+B)
 A=B
 B=R
print("Fin") 
 
 