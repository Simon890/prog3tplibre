from .algoritmo import Estado
from .algoritmo import Accion

class Nodo:
    costo: float
    estado: Estado.Estado
    padre: "Nodo"
    accion: Accion.Accion
    
    def __init__(self, costo: float, estado: Estado.Estado, padre : "Nodo", accion: Accion.Accion):
        self.costo = costo
        self.estado = estado
        self.padre = padre
        self.accion = accion
    
    def __str__(self):
        return (f"Nodo >> Costo: {self.costo} Estado: {self.estado} \n\n Padre: {self.padre.__str__()}")