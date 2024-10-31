#Alejandro Dominguez Castellanos #240021
def convertir(m):
    h = m // 60
    mi = m % 60
    return h, mi

m = int(input("Ingrese los minutos a convertir a horas y minutos: "))
h, mi = convertir(m)
print(f"{m} min son {h} h y {mi} min.")