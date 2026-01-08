"""
Programa principal de stardew_manager va a organizar tu granja y amistades del pueblo pelicano

Version: 1.0.0
Nombre: stardew_manager

"""

"imports"

from models.crop import cultivos

try:
    cultivos_1 = cultivos("Chirivia", 20, 4, 35)
    cultivos_1.imprimir()
except ValueError as e:
    print(e)