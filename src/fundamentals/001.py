"""
Fecha: 2026-01-01
Archivo: main.py
Autor: Ettore Zero

Descripción:
Punto de inicio para realizar el reto de 365 días del 2026.
"""

def signo(x: int) -> str:
    """
    Determina si un número es positivo, negativo o cero.

    Args:
        x (int): Número entero.

    Returns:
        str: Indica el signo del número.
    """
    if x > 0:
        return "Es positivo"
    elif x < 0:
        return "Es negativo"
    return "Es cero"


def main() -> None:
    """
    Función principal del programa.
    """
    x = int(input("Digite un número: "))
    print(signo(x))


if __name__ == "__main__":
    main()
