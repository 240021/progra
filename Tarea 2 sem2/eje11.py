#Alejandro Dominguez Castellanos Matricuela 240021
print("PONDUKA STATE UNIVERSITY")
print("Escoja la opcion que corresponda")
n=int(input("1.alumno veterano  2.alumno regular: "))
if n==1:
    re=int(input("Ingrese las materias reprobadas "))
    pa= 30*re
    print(f"Su pago sera de {pa} dolares")
elif n==2:
    re=int(input("Ingrese las materias reprobadas "))
    pa= 50*re
    print(f"Su pago sera de {pa} dolares")
else:
    print("Opcion invalida. Intente de nuevo")