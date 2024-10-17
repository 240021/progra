#Alejandro Dominguez Castellanos Matricula
i=0
par=0
impar=0
cero=0
while i<10:
    i=i+1
    n=int(input("Ingresa un numero entero: "))
    if n==0:
     cero=cero+1
    elif n % 2 == 0:
     par=par+1
    else:
      impar=impar+1
print(f"exiten pares {par}, impares {impar}, ceros {cero}")