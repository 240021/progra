#Alejandro Dominguez Castellanos Matricula 240021
#vocales
v=str(input("Ingrese una vocal (a,e,i,o,u) ").lower())
if v=="a" or v=="e" or v=="i":
      print(f"La vocal {v} es abierta ")
elif v=="o" or v=="u":
       print(f"La vocal {v} es cerrada ")
else:
      print("Ingrese una vocal: a-e-i-o-u")