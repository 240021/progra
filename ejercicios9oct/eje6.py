#Alejandro Dominguez Castellanos Matricuela

num=int(input("Ingresa los numeros que deseas sumar, para cerrar ingrese un numero negativo: "))
suma=0
while True: 
    if num<0:
        break
    suma=suma+num
    num=int(input("ingrese otro numero"))
print(f"la suma es: {suma}")