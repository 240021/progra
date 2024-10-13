#Alejandro Dominguez Castellanos Matricuela 240021
#un elefante se columpiaba

E=1
print(f" {E} elefante se columpiaba")
while E<10:  
    n=int(input("Cuantos elefantes se colimpiaran: "))
    if n == E+1:
        E+=1
        print(f" {E} elefante se columpiaba")
    else:
        print("Error")
print("Son todos los elefantes :)")