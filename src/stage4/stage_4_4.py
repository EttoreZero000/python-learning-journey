from src.stage4.stage_4_1 import analizar_numero
from src.stage4.stage_4_2 import validar_analisis

def test_analizar_numero_basico():
    resultado = analizar_numero(121)

    assert resultado["digitos"] == 3
    assert resultado["invertido"] == 121
    assert resultado["palindromo"] is True

def test_analizar_numero_no_palindromo():
    resultado = analizar_numero(123)

    assert resultado["digitos"] == 3
    assert resultado["invertido"] == 321
    assert resultado["palindromo"] is False

def test_analizar_numero_un_digito():
    resultado = analizar_numero(7)

    assert resultado["digitos"] == 1
    assert resultado["invertido"] == 7
    assert resultado["palindromo"] is True

def test_validar_analisis_falla():
    data = {
        "digitos": "tres",
        "invertido": 321,
        "palindromo": False
    }

    try:
        validar_analisis(data)
        assert False, "Debió lanzar una excepción"
    except ValueError:
        pass


def run_tests():
    test_analizar_numero_basico()
    test_analizar_numero_no_palindromo()
    test_analizar_numero_un_digito()
    test_validar_analisis_falla()
    print("Todos los tests pasaron")

if __name__ == "__main__":
    run_tests()
