"""
Programa main que llamara a todas las clases o funciones

Version de Python: 3.12

Hector Leiva Gamboa
Inicio: Sabado 10 de enero
Termina:
"""

from src.todo import ToDo
from datetime import datetime

dia = datetime(2027, 12, 10, 9, 30)

nota = ToDo("Test", "Test123", dia)

print(nota.Nombre)
print(nota.Nota)
print(nota.Fecha)