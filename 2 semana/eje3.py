#Alejandro Dominguez Castellanos Matricula: 240021
#calcular la diferencia entre dos numeros enteros positivos
print("Diferencia entre dos numeros enteros")
n1=int(input("Ingresa el primer numero entero:  "))
n2=int(input("Ingresa el segundo numero entero:  "))
 
if n1<0 or n2<0:
 print("solamente ingrese numeros positivos")
elif n1>n2:
 resultado=n1-n2
 print(f"La diferencia es de {resultado}")
else:
 resultado=n2-n1
 print(f"La diferencia es de: {resultado}")
