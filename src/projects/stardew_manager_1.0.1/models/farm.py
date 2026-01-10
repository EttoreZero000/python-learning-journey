from typing import List
from .crop import Crop

class Farm:
    """
    Representa la granja del jugador.
    Maneja el dinero, día actual y cultivos plantados.
    """

    def __init__(self, starting_money: int = 400):
        if starting_money < 0:
            raise ValueError("El dinero inicial no puede ser negativo")

        self.money = starting_money
        self.day = 1
        self._plants: List[dict] = []

    def plant(self, crop: Crop, quantity: int = 1):
        if quantity <= 0:
            raise ValueError("La cantidad debe ser positiva")

        total_cost = crop.seed_cost * quantity

        if self.money < total_cost:
            raise ValueError("Dinero insuficiente para plantar")

        self.money -= total_cost

        for _ in range(quantity):
            self._plants.append({
                "crop": crop,
                "day_planted": self.day,
            })

    def advance_day(self):

        self.day += 1




    def harvest_ready(self) -> List[Crop]:
        """
        Devuelve una lista de cultivos listos para cosechar.
        NO los elimina todavía.
        """
        ready = []
        for data in self._plants:
            crop = data["crop"]
            if self.day - data["day_planted"] >= crop.grow_days:
                ready.append(crop)
        return ready

    def harvest(self):
        """
        Cosecha todos los cultivos listos y los elimina de la granja.
        Suma el dinero correspondiente.
        """
        ready = []
        remaining = []

        for data in self._plants:
            crop = data["crop"]
            if self.day - data["day_planted"] >= crop.grow_days:
                ready.append(crop)
            else:
                remaining.append(data)

        self._plants = remaining

        for crop in ready:
            self.money += crop.sell_price

        return len(ready)
