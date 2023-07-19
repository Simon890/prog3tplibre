from .Problema import Problema
from .Estado import Estado
from ..Nodo import Nodo
from .Frontera import Frontera
from .Fallo import Fallo
from .Solucion import Solucion
from typing import List, Tuple

class AEstrella:
    problema: Problema
    alcanzados: List[Tuple[Estado, Nodo]]
    
    def __init__(self, problema: Problema):
        self.problema = problema
    
    def resolver(self):
        raiz = Nodo(0, self.problema.estado_inicial, None, None)
        frontera = Frontera()
        frontera.encolar(raiz, raiz.costo + self._heuristica(raiz.estado))
        self.alcanzados = [[raiz.estado, raiz]]
        
        while True:
            if frontera.vacia(): raise Fallo()
            
            nodo = frontera.desencolar()
            
            if self.problema.test_objetivo(nodo.estado): return Solucion(nodo)
            for accion in self.problema.acciones(nodo):
                hijo = Nodo(self.problema.costo(nodo.estado, accion), self.problema.resultado(nodo.estado, accion), nodo, accion)
                if not self._checkAlcanzados(hijo) or hijo.costo < self._encontrarAlcanzado(hijo).costo:
                    self.alcanzados.append([hijo.estado, hijo])
                    frontera.encolar(hijo, hijo.costo + self._heuristica(hijo.estado))
    
    def _heuristica(self, estado: Estado):
        costo = 0
        for i, fila in enumerate(self.problema.ESTADO_FINAL):
            for j, val in enumerate(fila):
                if val != estado[i][j]: costo += 1
        return costo

    def _checkAlcanzados(self, nodo: Nodo):
        for alcanzado in self.alcanzados:
            if nodo.estado == alcanzado[0]: return True
        return False

    def _encontrarAlcanzado(self, nodo: Nodo):
        for alcanzado in self.alcanzados:
            if nodo.estado == alcanzado[0]: return alcanzado[1]