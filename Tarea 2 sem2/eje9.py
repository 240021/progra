#Alejandro Dominguez Castellanos Matricuela 240021
#calculadora
print("calculadoras")
print ("Ingrese el numero de la operacion que desea realizar")
n=int(input("1 suma, 2 resta, 3 division, 4 multiplicacion: "))
if n==1:
    n1=float(input("Ingrese el primer numero "))
    n2=float(input("Ingrese el segundo numero "))
    r=n1+n2
    print(f"El resultado es: {r}")
elif n==2:
    n1=float(input("Ingrese el primer numero "))
    n2=float(input("Ingrese el segundo numero "))
    r=n1-n2
    print(f"El resultado es: {r}")
elif n==3:
    n1=float(input("Ingrese el primer numero "))
    n2=float(input("Ingrese el segundo numero "))
    if n2==0:
     print("No se puede dividir entre cero")
    else:
     r=n1/n2
     print(f"El resultado es {r}")
elif n==4:
    n1=float(input("Ingrese el primer numero "))
    n2=float(input("Ingrese el segundo numero "))
    r=n1*n2
    print(f"El resultado es: {r}")
else:
    print("Opcion invalida")