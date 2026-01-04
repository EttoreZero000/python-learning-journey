from src.stage4.stage_4_1 import analizar_numero

def validar_analisis(data: dict) -> None:
    """
    Valida que el diccionario de análisis tenga la estructura correcta.

    Args:
        data (dict): Resultado de analizar_numero

    Raises:
        ValueError: si la estructura es inválida
    """

    if type(data) != dict:
        raise ValueError("Esto no es un diccionario")

def formatear_analisis(data: dict) -> str:
    """
    Recibe un análisis validado y lo convierte en texto legible.
    """
    string = ""
    for key in data.keys():
        string += f"{key}: {data[key]} \n"

    print(string)



def procesar_numero(x: int) -> str:
    """
    Ejecuta el flujo completo:
    número → análisis → validación → formateo
    """

    diccionario = analizar_numero(x)

    validar_analisis(diccionario)

    formatear_analisis(diccionario)


def main() -> None:
    try:
        x = int(input("Digite un número: "))
        salida = procesar_numero(x)
        print(salida)
    except ValueError as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()