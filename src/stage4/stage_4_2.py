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
    
    required_keys = {"digitos", "invertido", "palindromo"}
    if set(data.keys()) != required_keys:
        raise ValueError("Estructura inválida")
    
    for key in data.keys():
        if key not in ["digitos", "invertido", "palindromo"]:
            raise ValueError(f"No esta {key}")
        
        if key == "digitos" or key == "invertido":
            if not isinstance(data[key], int):
                raise ValueError(f"{data[key]} no es un int")
            
        if key == "palindromo":
            if not isinstance(data[key], bool):
                raise ValueError(f"{data[key]} no es un bool")


def formatear_analisis(data: dict) -> str:
    """
    Recibe un análisis validado y lo convierte en texto legible.
    """
    string = "Análisis del número: \n"
    for key in data.keys():
        if key == "palindromo":
            flag = "No"
            if data[key]:
                flag = "Si"
            string += f"- ¿Es palíndromo?: {flag} \n"
            break
        string += f"- {key}: {data[key]} \n"

    return string



def procesar_numero(x: int) -> str:
    """
    Ejecuta el flujo completo:
    número → análisis → validación → formateo
    """

    diccionario = analizar_numero(x)

    validar_analisis(diccionario)

    return formatear_analisis(diccionario)


def main() -> None:
    try:
        x = int(input("Digite un número: "))
        salida = procesar_numero(x)
        print(salida)
    except ValueError as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()