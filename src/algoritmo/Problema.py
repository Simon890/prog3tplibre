from .Estado import Estado
from ..Nodo import Nodo

class Problema:
    """
    Representa el problema a solucionar.
    """
    
    ESTADO_FINAL: Estado = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    estado_inicial: Estado
    
    def __init__(self, estado_inicial: Estado):
        """
        estado_inicial: Estado desde donde se inicia el problema
        """
        self.estado_inicial = estado_inicial
    
    def test_objetivo(self, estado: Estado):
        """
        Dado un estado, retorna True si corresponde con el estado objetivo
        """
        for i, fila in enumerate(self.ESTADO_FINAL):
            for j, nro in enumerate(fila):
                if nro != estado[i][j]: return False
        return True

    def acciones(self, nodo: Nodo):
        pass
    
    def costo(self, accion):
        pass