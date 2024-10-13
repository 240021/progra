#Alejandro Dominguez Castellanos Matricuela 240021

C=0
while C<3:  
    n=float(input("Ingrece PIN de 4 digitos: "))
    if n != 1425:
        C+=1
        if C==3:
            print("Llamando a la policia")
            break
        else:
            print("Intente de nuevo")   
    else:
        print("Login Correcto")
        break