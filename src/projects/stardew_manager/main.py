"""
Programa principal de stardew_manager va a organizar tu granja y amistades del pueblo pelicano

Version: 1.0.0
Nombre: stardew_manager

"""

"imports"

from models.crop import Crop

try:
    cultivos_1 = Crop("Chirivia", 20, 4, 35)
except ValueError as e:
    print(e)

