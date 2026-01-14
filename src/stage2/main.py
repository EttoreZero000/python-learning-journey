"""
*Pide un número y muestra si es positivo, negativo o cero.

*Pide un número y muestra si es par o impar.

*Pide una edad y muestra si es mayor de edad (>=18).

*Pide una contraseña y compara si coincide con "1234".

*Pide dos números y muestra cuál es el mayor.

*Pide una letra y determina si es vocal o consonante.

*Pide un año y determina si es bisiesto (simplificado: divisible entre 4).

*Pide la calificación (0–100) y muestra si aprueba (>=70).

*Pide un número del 1 al 7 y muestra el día de la semana.

*Pide un número y muestra si está en el rango [10, 20].
"""

def esPositivo():
    numero = int(input("Digite un numero: "))

    if numero > 0:
        print("Es positivo")
    elif numero == 0:
        print("Es cero")
    else:
        print("Es negativo")

def esPar():
    numero = int(input("Digite un numero: "))

    if numero == 0:
        raise ValueError("No se permite el numero cero")

    if numero%2 == 0:
        print("Es par")
        return
    print("Es impar")
    return

def esMayor():
    year = int(input("What years old?: "))

    if year<18:
        print("You are underage")
        return
    print("You are of legal age")

def yourPassword():
    password = input("What its your password?: ")

    if password == "1234":
        print("Welcome your account")
        return
    print("Not it's your password!")
    return

def numberComparation():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    if num2 == num1:
        raise ValueError("The numbers is equals")

    if num1 > num2:
        print(f"This is largest number: {num1}")
        return
    print(f"This is largest number: {num2}")

def isVocal():
    a = input("Enter a char: ").lower()

    if len(a) > 1:
        raise ValueError("It's a one letter")

    if a in "aeiou":
        print("It's a vocal")
        return
    print("It's a consonant")

def isLeap():
    year = int(input("Enter a year: "))

    if year % 4 == 0:
        print("It's a leap")
        return
    print("It's not a leap")
    
def isApproved():
    note = int(input("What is your note (0-100): "))

    if note>100 or note<0:
        raise ValueError("It's outside range")

    if note >= 70:
        print("Your have approved!!")
        return
    print("Your not have approved")
    
def numberToDay():
    number = int(input("Enter a digit (1-7)"))
    listDay = ["Monday","Tuesday", "Wendnesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if number>7 or number<1:
        raise ValueError("It's outside range")
    
    print(listDay[number-1])
    
def range1020():
    number = int(input("Enter a digit: "))

    if number>20 or number<10:
        raise ValueError("It's outside range")
    
    print("It's on range")
    return

def main():
    print("Iniciando stage 2")
    try:
        range1020()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()