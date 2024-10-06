#Alejandro Dominguez Castellanos Matricuela 240021
#Crear un programa que pida al usuario su edad y le indique a qué grupo etario pertenece
edad=int(input("ingresa tu edad "))
if edad <=6:
    print("Usted esta en su infancia")
elif edad <=12:
    print("Usted esta en su ninez")
elif edad <=20:
    print("Usted esta en su adolescencia")
elif edad <=25:
    print("Usted esta en su juventud")
elif edad <=60:
    print("Usted esta en su adultez")
else:
    print("Usted esta en su etapa ancianidad")