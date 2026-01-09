from models.farm import Farm

class SimulationEngine:
    def __init__(self, farm: Farm):
        self.farm = farm

    def advance_days(self, n: int):
        if n<=0:
            raise ValueError("No se puede dias negativos")

        for _ in range(n):
            self.farm.day+=1