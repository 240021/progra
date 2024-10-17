#Alejandro Dominguez Castellanos Matricuela 240021
caliente=0
frio=100000000000000
suma=0
i=0
while i<7:
 i=i+1
 n=int(input(f"Ingresa la temperatura del día {i}:  "))
 suma=suma+n
 
 if n>caliente:
   caliente=n
 if n<frio:
    frio=n
   
promedio=suma/7
print(f"El clima más calinete en la semana fue de: {caliente}")
print(f"El clima más frio en la semana fue de: {frio} ")
print(f"El clima promedio de la semana es: {promedio}")