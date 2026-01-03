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

def es_par(x: int) -> str:
    """
    Determinar si un numero es par o impar

    Args:
        x (int): Numero entero.

    Returns:
        str: Indica si es par o no
    """

    if x<=0:
        return "Error: el numero tiene que ser positivo"

    if x%2 == 0:
        return "Es par"
    return "Es impar"

def sumar_n(x: int) -> str:
    """
    if x<=0:
        return x
    return x + (sumar_n(x-1))
    """
    if x<=0:
        return "Error: el numero tiene que ser positivo"
    i=0
    while x>0:
        i+=x
        x-=1
    return i


def main() -> None:
    """
    Función principal del programa.
    """
    print("Hola conexion")
    x = int(input("Digite un número: "))
    print(sumar_n(x))


if __name__ == "__main__":
    main()
