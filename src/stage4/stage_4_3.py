from src.stage4.stage_4_1 import analizar_numero

def validar_analisis(data: dict) -> None:
    """
    Valida que el diccionario de análisis tenga la estructura correcta.

    Args:
        data (dict): Resultado de analizar_numero

    Raises:
        ValueError: si la estructura es inválida
    """


    if not isinstance(data, dict):
        raise TypeError("Esto no es un diccionario")
    
    required_keys = {
        "digitos" : int,
        "invertido": int,
        "palindromo": bool
    }

    for key, type in required_keys.items():
        if key not in data:
            raise KeyError(f"Falta la clave {key}")
        
        if not isinstance(data[key], type):
            raise TypeError(f"No coincide {key}")
        
    if len(data) != len(required_keys):
        raise ValueError(f"No coincide el size aceptado")


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
    except TypeError as e:
        print(f"Error de tipo: {e}")
    except KeyError as e:
        print(f"Error de key: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except:
        print("Error inesperado")



if __name__ == "__main__":
    main()