def validar_analisis(data: dict) -> None:
    if not isinstance(data, dict):
        raise TypeError("El análisis debe ser un diccionario")

    required_keys = {
        "digitos": int,
        "invertido": int,
        "palindromo": bool
    }

    for key, expected_type in required_keys.items():
        if key not in data:
            raise KeyError(f"Falta la clave '{key}'")

        if not isinstance(data[key], expected_type):
            raise TypeError(
                f"La clave '{key}' debe ser {expected_type.__name__}"
            )

    if len(data) != len(required_keys):
        raise ValueError("El diccionario tiene claves extra")
