def hanoi(n: int, origen: str, auxiliar: str, destino: str, pasos: int = 0) -> int:
    if n == 1:
        pasos += 1
        print(f"{pasos}: {origen} --> {destino}")
        return pasos

    pasos = hanoi(n - 1, origen, destino, auxiliar, pasos)
    pasos += 1
    print(f"{pasos}: {origen} --> {destino}")
    return hanoi(n - 1, auxiliar, origen, destino, pasos)


n = int(input("Ingrese el número de discos: "))
if n > 0:
    total = hanoi(n, "A", "B", "C")
    print(f"Total de pasos: {total}")