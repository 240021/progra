#Alejandro Dominguez Castellanos Matricuela 240021
#Invertir un numero de 3 digitos
In=int(input("ingresa un numero de 3 digitos: "))

if In<1 or In>999:
    print("El dato ingresado debe estar en un rango de 1 a 999")
else:
    uni=In%10
    dec=(In//10)%10
    cen=In//100
    Newn=uni*100+dec*10+cen
    print(f"El numero invertido es {Newn}")
