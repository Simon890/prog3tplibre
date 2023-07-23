
from abc import abstractmethod

from .Problema import Problema

from .Estado import Estado

class Algoritmo:
    
    problema: Problema
    
    def __init__(self, problema: Problema):
        self.problema = problema
    
    @abstractmethod
    def resolver(self):
        pass
    
    def _heuristica(self, estado: Estado):
        costo = 0
        for i, fila in enumerate(self.problema.ESTADO_FINAL):
            for j, val in enumerate(fila):
                if val != estado[i][j]: costo += 1
        return costo