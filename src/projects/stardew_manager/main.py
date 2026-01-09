"""
Programa principal de stardew_manager va a organizar tu granja y amistades del pueblo pelicano

Version: 1.0.0
Nombre: stardew_manager

"""

"imports"

from models.crop import Crop
from models.farm import Farm
from services.simulation import SimulationEngine

try:
    chirivia = Crop("Chirivia", 20, 4, 35)
    granja = Farm()

    granja.plant(chirivia, 20)

    simulador = SimulationEngine(granja)

    simulador.advance_days(5)

    lista = granja.harvest_ready()

    print(granja.money)

    print(granja.harvest())

    print(granja.money)


    print(granja.day)

    simulador.advance_days(1)

    print(granja.day)



except ValueError as e:
    print(f"Error: {e}")

