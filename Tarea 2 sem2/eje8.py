#Alejandro Dominguez Castellanos Matricula 240021

print("Ingrese las medidas del triangulo para saber su tipo")
lado1=float(input("Ingrese la medida del primer lado "))
lado2=float(input("Ingrese la medida del segundo lado "))
lado3=float(input("Ingrese la medida del tercer lado "))
if lado1==lado2 and lado1==lado3:
    print("Es un triangulo equilatero")
elif lado1!=lado2 and lado3!=lado2 and lado3!=lado1:
    print("Es un triangulo escaleno")
else:
    print("Es un triangulo isosceles")