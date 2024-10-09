#Alejandro Dominguez Castellanos Matricula 240021
#tabla de multiplicar 

N=int(input("Ingrese la tabla que desea ver: "))
c=0
R=0
for c in range(1,11):
 R=N*c
 print(f"{N} x {c} = {R}") 