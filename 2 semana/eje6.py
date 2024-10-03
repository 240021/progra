#Alejandro Dominguez Castellanos, Matricula: 240021
#precio de frutas 
kilo=float(input("Cuantos kilos de manzana quieres comprar? "))
precio=46.60*kilo

if kilo>0 and kilo<=2:
 print(f"El total a pagar es {precio:.2f}")
elif kilo<=5:
   descuento=(precio*.10)
   cd=precio-descuento
   print(f"El costo con el 10% de descuento es {cd:.2f}")
elif kilo<=10:
   descuento=(precio*.15)
   cd=precio-descuento
   print(f"El costo con el 15% de descuento es {cd:.2f}")
else:
   descuento=(precio*.20)
   cd=precio-descuento
   print(f"El costo con el 20% de descuento es {cd:.2f}")
     
  