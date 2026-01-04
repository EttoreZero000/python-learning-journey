def cantidad_digitos_refactorizada(x: int) -> int:
    """
    Cuenta la cantidad de digitos de un numero

    Args:
        x (int): Numero entero positivo

    Returns:
        int: Devuelve la cantidad de digitos del numero

    raise:
        ValueError si x<=0
    """

    if x <= 0:
        raise ValueError("x no tiene que ser 0 o negativo")
    
    contador = 0

    while x > 0:
        contador += 1

        x //= 10
    
    return contador

def invertir_numero_refactorizada(x: int) -> int:
    """
    Invierte el numero

    Args:
        x (int): Numero entero positivo

    Returns:
        int: Retorna el numero invertido

    raise:
        ValueError si x<=0
    """
    if x<=0:
        raise ValueError("x no puede ser 0 o negativo")
    
    resultado=0
    while x > 0:
        resultado = resultado * 10 + (x % 10)
        x //= 10

    return resultado

def palindromo_numero_refactorizada(x: int) -> int:
    """
    Palindromo de un numero

    Args:
        x (int): Numero entero positivo

    Return:
        bool: Si es palindromo True
                si no es palindromo False

    raise:
        ValueError si x<=0
    """

    if x<=0:
        raise ValueError("x no puede ser 0 ni negativo")
    
    return x == invertir_numero_refactorizada(x)


def main():
    """
    Funcion principal del programa
    """

    try:
        x = int(input("Digite un numero: "))
        print(palindromo_numero_refactorizada(x))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()