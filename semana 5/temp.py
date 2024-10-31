#Alejandro Dominguez Castellanos #240021
def Grados():
    print("Selecciona la conversion deseada?")
    op=int(input("1.convertir C a F, 2. convertir a F a C: "))

    if op ==1:
        Ce=float(input("Ingrese los centigrados a convertir: "))
        fa=Ce*(9/5)+32
        print(f"Los {Ce} centigrados son {fa:.2f} Fahrenheit")
    elif op==2:
        Gf=float(input("Ingrese los fahrenheit a convertir: "))
        Gc=(Gf-32)*(5/9)
        print(f"Las {Gf} fahrenheit son {Gc:.2f} centigrados")
    else:
        print("Opcion no valida")
Grados()