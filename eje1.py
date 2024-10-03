#Alejandro Dominguez Castellanos Matricula: 240021
print("Encontrar el numero mayor entre 3 numeros")
n1=int(input("ingrese el primer numero: "))
n2=int(input("ingrese el segundo numero: "))
n3=int(input("ingrese el tercer numero: "))

if n1>n2 and n1>n3:
    max=n1
elif n2>n3:
    max=n2
else:
    max=n3
print(f"el numero mayor es {max}")

    