"""
Pide al usuario su nombre y salúdale.

Pide dos números y muéstralos en una sola línea separados por coma.

Pide la edad del usuario y muestra: "Tienes X años".

Pide un nombre y un color favorito, muestra una frase combinando ambos.

Pide un número y muestra: "El número ingresado fue: X".
"""

def stage1_1():
    name = input("Escriba tu nombre: ")

    print(f"Hola, {name}")

def stage1_2():
    numero1 = input("Digite un numero: ")
    numero2 = input("Digite un numero: ")

    print(numero1, numero2, sep=',')

def stage1_3():
    years = input("Digite cuantos años tienes: ")

    print(f"Tienes {years} años")

def stage1_4():
    name = input("Escriba tu nombre: ")
    color = input("Escriba tu color favorito: ")

    print(f"Tu nombre es {name} y tu color favorito es {color}")

def stage1_5():
    numero = input("Digite un numero")

    print(f"El número ingresado fue: {numero}")

def main():
    stage1_3()

if __name__ == "__main__":
    main()