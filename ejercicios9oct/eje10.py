#Alejandro Dominguez Castellanos Matricuela 240021
#po,neg,cer
i=0
po=0
ne=0
ce=0
while i<10:  
    n=float(input("Ingrece un numero: "))
    if n<0:
        ne+=1
        i+=1
    elif n>0:
        po+=1
        i+=1
    elif n==0:
        ce+=1
        i+=1
print(f"Hay {po} positivos, {ne} negativos y {ce} ceros")