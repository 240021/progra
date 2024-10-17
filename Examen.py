#Alejandro Dominguez Castellanos Matricula 240021
#Examen 1
#Realice un programa que resuelva lo siguiente
#En un grupo de 15 alumnos de UPBC, se busca nombrar a un jefe de grupo
#mediante el voto de cada uno de ellos, todo esto en presencia de su maestro asesor
#se decidio una votacion.
#los 3 candidatos son 1 hugo, 2 paco y 3 luis
#el maestro asesor les solicito que el primer lugar sea el jefe de grupo y el segundo lugar sera el tesorero.
#a) quien serael jefede grupo y con cuantos votos y porcentaje
#b) quien sera el tesorero y con cuantos votos y porcentaje
#c) al 3er lugar le daremos las gracias

i=1
j=0
jpor=0
p=0
ppor=0
l=0
lpor=0

while i<16:

    print("escoje 1 para juan, 2 para paco y 3 para luis")
    Alumno=int(input(f"votacion del {i} alumno: "))
    if Alumno==1:
     j=j+1
    elif Alumno==2:
     p=p+1
    elif Alumno==3:
     l=l+1
    else:
     print("debes de votar por un alumno")
     i=i-1
    i=i+1
print("")        
print(f"Votos juan: {j}, Votos paco: {p}, Votos luis: {l}")

jpor=(j*100/15)
ppor=(p*100/15)
lpor=(l*100/15)
("")
print(f"porcentaje juan: {jpor:.2f}, porcentaje paco: {ppor:.2f}, porcentaje luis: {lpor:.2f}")

("")
if j>p and j>l and p>l:
 print(f"Juan es el nuevo jefe de grupo, paco el tesorero y le damos las gracias a luis")
elif p>j and p>l and j>l:
 print("paco es el nuevo jefe de grupo, juan es el tesorero y le damos las gracias a luis")
elif l>j and l>p and p>j:
 print("luis es el nuevo jefe de grupo, paco es el tesorero y le damos las gracias a juan")
if j>p and j>l and l>p:
 print("Juan es el nuevo jefe de grupo, paco es el tesorero y le damos las gracias a paco")
elif p>j and p>l and l>j:
 print("paco es el nuevo jefe de grupo, luis es el tesorero y le damos las gracias a juan")
elif l>j and l>p and j>p:
 print("luis es el nuevo jefe de grupo, juan es el tesorero y le damos las gracias a paco")
elif j==p==l:
 print("empate vuelvan a votar")
else:
 print("no hay un ganador vuelvan a votar")


     

    