class lote:
    def __init__(self, name: str, length: int, days: int):
        self.name = name
        self.length = length   # cantidad
        self.days = days       # días restantes

    def lessDay(self):
        self.days -= 1

    def __repr__(self):
        return f"<Lote {self.name} x{self.length}, días restantes: {self.days}>"

class lotes:
    def __init__(self):
        self.list = []        # lotes creciendo
        self.list_ready = []  # lotes listos

    def create(self, lote: lote):
        """ Agrega un nuevo lote en crecimiento """
        self.list.append(lote)

    def lessDays(self):
        """ Resta 1 día a todos los lotes en crecimiento """
        for lote in self.list:
            lote.lessDay()

    def checkReady(self):
        """ Mueve los lotes con días <= 0 a la lista de listos """
        to_move = []
        for lote in self.list:
            if lote.days <= 0:
                to_move.append(lote)

        for lote in to_move:
            self.list.remove(lote)
            self.list_ready.append(lote)

    def passDay(self):
        """ Pasa un día entero: resta días y actualiza listos """
        self.lessDays()
        self.checkReady()

    def harvest(self, index: int):
        """ Cosecha un lote listo y lo elimina de list_ready """
        if 0 <= index < len(self.list_ready):
            lote = self.list_ready.pop(index)
            return lote
        else:
            raise IndexError("Índice fuera de rango")

    def viewGrowing(self):
        """ Devuelve lista de lotes creciendo """
        return self.list

    def viewReady(self):
        """ Devuelve lista de lotes listos """
        return self.list_ready
