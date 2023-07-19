from algoritmo.Estado import Estado

class Nodo:
    costo: float
    def __init__(self, costo: float, estado: Estado):
        self.costo = costo