from collections.abc import Generator
import time


class TorresDeHanoi:

    def __init__(self, num_discos: int):
        if num_discos <= 0:
            raise ValueError("El número de discos debe ser mayor a 0.")
        self.num_discos = num_discos
        # Representación real: A tiene los discos de mayor a menor [n, ..., 1]
        self.torres: dict[str, list[int]] = {
            "A": list(range(num_discos, 0, -1)),
            "B": [],
            "C": [],
        }
        self.pasos = 0

    def _mover_disco(self, origen: str, destino: str) -> None:
        """Ejecuta y valida que el movimiento cumpla las reglas del juego."""
        if not self.torres[origen]:
            raise RuntimeError(f"Error lógico: La torre {origen} está vacía.")

        disco = self.torres[origen][-1]
        if self.torres[destino] and self.torres[destino][-1] < disco:
            raise RuntimeError(
                f"Movimiento ilegal: Disco {disco} sobre {self.torres[destino][-1]}"
            )

        self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.pasos += 1

    def resolver(
        self,
        n: int | None = None,
        origen: str = "A",
        auxiliar: str = "B",
        destino: str = "C",
    ) -> Generator[tuple[int, str, str], None, None]:
        """Generador recursivo que actualiza el estado interno paso a paso."""
        if n is None:
            n = self.num_discos

        if n > 0:
            yield from self.resolver(n - 1, origen, destino, auxiliar)
            self._mover_disco(origen, destino)
            yield (self.pasos, origen, destino)
            yield from self.resolver(n - 1, auxiliar, origen, destino)

    def mostrar_estado(self) -> None:
        """Renderiza las torres en consola de forma visual."""
        altura = self.num_discos
        print()
        for nivel in range(altura - 1, -1, -1):
            fila = []
            for nombre in ("A", "B", "C"):
                torre = self.torres[nombre]
                if nivel < len(torre):
                    disco = torre[nivel]
                    # Dibuja el disco centrado según su tamaño
                    bloque = "=" * (disco * 2 - 1)
                    fila.append(bloque.center(altura * 2 + 1))
                else:
                    fila.append("|".center(altura * 2 + 1))
            print("  ".join(fila))

        base = "-" * (altura * 2 + 1)
        print(f"{base}  {base}  {base}")
        etiquetas = [t.center(altura * 2 + 1) for t in ("A", "B", "C")]
        print("  ".join(etiquetas) + "\n")


def ejecutar() -> None:
    try:
        entrada = input("Ingrese el número de discos (recomendado 1-10): ")
        n = int(entrada)
        if n > 20:
            print(
                f"Advertencia: {n} discos requieren {2**n - 1:,} pasos. Operación cancelada."
            )
            return

        juego = TorresDeHanoi(n)
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return

    ver_visual = n <= 5  # Solo dibuja en consola si hay 5 o menos discos
    print(f"\nMovimientos teóricos necesarios: {2**n - 1}")

    if ver_visual:
        print("Estado inicial:")
        juego.mostrar_estado()

    inicio = time.perf_counter()

    for paso, origen, destino in juego.resolver():
        print(f"Paso {paso:02d}: {origen} --> {destino}")
        if ver_visual:
            juego.mostrar_estado()

    duracion = (time.perf_counter() - inicio) * 1000
    print(f"Completado en {juego.pasos} pasos ({duracion:.3f} ms).")


if __name__ == "__main__":
    ejecutar()