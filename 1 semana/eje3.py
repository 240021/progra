#Alejandro Dominguez Castellanos, matricula: 240021
print("area y perimetro de un triangulo rectangulo")
b=float(input("ingrese la medida de la base del triangulo: "))
a=float(input("ingrese la medida de la altura: "))
h=float(input("ingrese la medida de la hipotenusa: "))

Area=(b*a)/2
Perimetro=b+a+h

print(f"El triangulo tiene un area de {Area:.2f} y un perimetro de {Perimetro:.2f}")