#Alejandro Dominguez Castellanos 240021
def factorial():
    facto=1
    n=int(input("Ingrese el numero que desea para realizar su factorial: "))
    for i in range (1,n+1) :
        facto*=i
    print(f"La factorial es: {facto}")
factorial()