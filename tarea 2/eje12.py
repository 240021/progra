# Dominguez Castellanos Alejandro matricula: 240021

nupa = int(input("Introduce el número de payasos vendidos: "))
numu = int(input("Introduce el número de muñecas vendidas: "))

pesopayaso = 112  # en gramos
pesomuneca = 75   # en gramos

ptotal = (nupa * pesopayaso) + (numu * pesomuneca)

costoenvio = ((ptotal + 599) // 600) * 120

print(f"El peso total del paquete es {ptotal} gramos.")
print(f"El costo de envío es {costoenvio} pesos.")