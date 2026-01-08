class cultivos:
    def __init__(self, name: str, costo: int, days: int, sell: int):

        if costo < 0 or days < 0 or sell < 0:
            raise ValueError("No se puende valores negativos")

        self.name = name
        self.costo = costo
        self.days = days
        self.sell = sell

    def imprimir(self):
        print(f"Nombre: {self.name}, \nCosto: {self.costo} \nDias: {self.days} \nVenta: {self.sell} \nGanancia: {self.sell - self.costo}")