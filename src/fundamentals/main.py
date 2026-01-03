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

def sumar_n(x: int) -> int | str:
    """
    Calcula la suma de los números desde 1 hasta n.

    Args:
        x (int): Número entero positivo.

    Returns:
        int | str: La suma total si x es positivo,
                   o un mensaje de error en caso contrario.
    """
    if x <= 0:
        return "Error: el número tiene que ser positivo"

    total = 0
    while x > 0:
        total += x
        x -= 1

    return total

def cantidad_digitos(x: int) -> int | str:
    """
    Reto 4:
    Calcula la cantidad de digitos de un numero

    Args:
        x (int): Numero entero positivo

    Returns:
        int | str: Cantidad de digitos en un numero x positivo
                    o un mensaje de error en caso contrario
    """
    if x <= 0:
        return "Tiene que ser positivo."
    n=1

    while True:
        if x/(10**n) < 1:
            return n
        n+=1

def num_mayor(x: int, y: int, z: int) -> int | str:
    """
    Reto 5:
    Dice el numero mayor, y si hay duplicados dice que "hay duplicados de x numero"

    Args:
        x, y, z (int): Numeros enteros positivos

    Returns:
        int | str: Dice cual numero es mayor,
                    si hay duplicados lo dice

    """
    if x>=y and x>=z:
        if x==y or x==z:
            return ("El mayor es "+ str(x) + " y hay duplicado")
        else:
            return x
    return(num_mayor(y,z,x))

def invertir_numero(x: int) -> int | str:
    """
    Reto 6:

    Args:
        x (int): Numero entero positivo

    Returns:
        int | str: Devuelve el numero invertido,
                    si es negativo dice error
    """
    if x <= 0:
        return "No puede ser un negativo"

    resultado = 0
    n=cantidad_digitos(x) - 1
    for i in range(n, -1, -1):
        resultado += (x % 10) * 10** i
        x //= 10
    return resultado
    
def sumar_pares(x: int) -> int | str:
    """
    Reto 7:

    Args:
        x (int): Numero entero positivo

    Returns:
        int | str: Devuelve la suma de todos los pares positivos
                    si es un numero negativo o cero error.
    """
    if x<=0:
        return "Error: no se puede 0 o negativos"

    temp=0
    for i in range(2,x+1,2):
        temp+=i
    return temp

def pares_basica(x: int) -> int | str:
    """
    Reto 8:

    Args:
        x (int): Numero entero positivo
    
    Returns:
        int | str: Devuelve la cantidad de pares que hay de 1 a x
                    si es un numero negativo o cero da error
    """

    if x<=0:
        return "Error: el numero es 0 o negativo"

    n,pares=0,0


    while True:
        n += 1
        x -= 1

        if n == 2:
            n = 0
            pares += 1
        
        if x == 0:
            return pares
        
def es_primo(x: int) -> str:
    """
    Reto 9:

    Args:
        x (int): Nuero entero positivo
    
    Returns:
        str: Devuelve "No es primo" o "Es primo",
                si es negativo o 0, se devuelve un error
    """

    if x<=0:
        return "Error: el numero es 0 o negativo"

    n=int(x**(0.5))

    for i in range (2, n+1):
        if x%i == 0:
            return "No es primo"
    return "Es primo"

def sumar_numeros(x: int) -> int | str:
    """
    Reto 10:

    Args:
        x (int): Numero entero positivo
    
    Returns:
        str: Devuelve la suma de todos los digitos individuales
            si es negativo o un 0, devuelve un error
    """

    if x <= 0:
        return "No puede ser un negativo"

    resultado = 0
    n=cantidad_digitos(x) - 1
    for i in range(n, -1, -1):
        resultado += (x % 10)
        x //= 10
    return resultado

def palindromo_numero(x: int) -> str:
    """
    Reto 11

    Args:
        x (int): Entero positivo

    Returns:
        str: Devuelve si es un palindromo o no lo es
    """
    if x == invertir_numero(x): return "Es palindromo"

    return "No es palindromo"

def cantidad_digitos_refactorizada(x: int) -> int:
    """
    Reto 12:
    Calcula la cantidad de digitos de un numero

    Args:
        x (int): Numero entero positivo

    Returns:
        int: Cantidad de digitos en un numero x positivo
                    o un mensaje de error en caso contrario
    
    Raises:
    ValueError: Si x <= 0
    """
    if x <= 0:
        raise ValueError("x debe de ser un numero entero positivo")
    
    if x <= 0:
        raise ValueError("x debe ser un entero positivo")

    contador = 0
    while x > 0:
        contador += 1
        x //= 10

    return contador

def invertir_numero_refactorizada(x: int) -> int:

    if x<=0:
        raise ValueError("x no puede ser 0 o negativo")
    
    resultado = 0
    n=cantidad_digitos_refactorizada(x) - 1
    for i in range(n, -1, -1):
        resultado += (x % 10) * 10** i
        x //= 10
    return resultado

def main() -> None:
    """
    Función principal del programa.
    """
    print("Hola, si hay conexion con docker")
    try:
        x = int(input("Digite un número: "))
        print(invertir_numero_refactorizada(x))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
