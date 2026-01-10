class Crop:
    """
    Representa un tipo de cultivo.
    """

    def __init__(self, name: str, seed_cost: int, grow_days: int, sell_price: int):
        if seed_cost <= 0 or grow_days <= 0 or sell_price <= 0:
            raise ValueError("Los valores del cultivo deben ser positivos")

        self.name = name
        self.seed_cost = seed_cost
        self.grow_days = grow_days
        self.sell_price = sell_price
        self.dias_plantado = 0
        self.is_ready = False
