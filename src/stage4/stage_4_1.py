from src.fundamentals.numeros import invertir_numero_refactorizada
from src.fundamentals.numeros import cantidad_digitos_refactorizada
from src.fundamentals.numeros import palindromo_numero_refactorizada

def analizar_numero(x: int) -> dict:
    """
    Analiza un número entero positivo y devuelve información estructurada.

    Args:
        x (int): Número entero positivo

    Returns:
        dict con las claves:
            - digitos (int)
            - invertido (int)
            - palindromo (bool)

    Raises:
        ValueError: si x <= 0
    """

    if x<=0:
        raise ValueError("x no puede ser 0 ni negativo")

    return {
        "digitos" : cantidad_digitos_refactorizada(x), 
        "invertido" : invertir_numero_refactorizada(x), 
        "palindromo" : palindromo_numero_refactorizada(x)
        }



def main() -> None:

    try:
        x=int(input("Digite un numero: "))
        print(analizar_numero(x))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()