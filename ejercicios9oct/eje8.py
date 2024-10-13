#Alejandro Dominguez Castellanos Matricuela 240021
#monto
S=0
while True:  
    n=float(input("Cual es el precio del producto: "))
    if n == 0:
        break
    elif n<0:
        print("Error, ingrece un nuevo monto: ")
    else:
        S += n
if S>1000:
    S = S -(S*.1)
    print(f"Su descuento es de: {S}")
else:
    print(f"Su total a pagar {S}")