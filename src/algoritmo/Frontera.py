from typing import List, Tuple
from ..Nodo import Nodo

class Frontera:
    """
    Frontera en donde se guardan los nodos.
    Es una cola de prioridad
    """
    nodos: List[Tuple[Nodo, float]] = []
    
    def encolar(self, nodo: Nodo, costo: float) -> None:
        """Guarda nodos en la lista"""
        self.nodos.append((nodo, costo))
        
    def desencolar(self) -> Nodo:
        """Retorna el nodo con menor costo"""
        if len(self.nodos) == 0: raise Exception("No hay nodos para desencolar")
        mejor : Nodo | None = self.nodos[0]
        for nodo in self.nodos:
            if nodo[1] < mejor[1]:
                mejor = nodo
        self.nodos.remove(mejor)
        return mejor
    
    def vacia(self) -> bool:
        return len(self.nodos) == 0
