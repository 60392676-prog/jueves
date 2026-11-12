pasos =  0

def hanoi(n, origen, auxiliar, destino):
    global pasos
    if n == 1:
        print(pasos+1, ":",origen, "-->", destino)
        pasos += 1
    else:
        hanoi(n-1, origen, destino,auxiliar)
        print(pasos+1,":", origen, "-->", destino)
        pasos += 1
        hanoi(n-1, auxiliar, origen, destino)

n = int(input("Ingrese el numero de discos: "))
hanoi(n,"A","B","C")
print("Total de pasos: ", pasos)