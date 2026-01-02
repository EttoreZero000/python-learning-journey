"""
1-1-2026
Archivo: main.py
Autor: Ettore Zero

Descripción:
Punto de inicio para realizar el reto de 365 dias del 2026
"""

def signo(x):

    """
    Determinar si un numero es positivo, negativo o cero

    Args:
        x (int): Numero entero

    Returns:
        string: Es positivo, es negativo o es cero
    """

    if x>0:
        return "Es positivo"
    elif x<0:
        return "Es negativo"
    else:
        return "Es cero"


x = int(input("Digite un numero: "))

print(signo(x))