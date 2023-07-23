from .Estado import Estado
from ..Nodo import Nodo
from .Frontera import Frontera
from .Fallo import Fallo
from .Solucion import Solucion
from typing import List, Tuple
from .Algoritmo import Algoritmo

class AEstrella(Algoritmo):
    
    alcanzados: List[Tuple[Estado, Nodo]]
    
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
    

    def _checkAlcanzados(self, nodo: Nodo):
        for alcanzado in self.alcanzados:
            if nodo.estado == alcanzado[0]: return True
        return False

    def _encontrarAlcanzado(self, nodo: Nodo):
        for alcanzado in self.alcanzados:
            if nodo.estado == alcanzado[0]: return alcanzado[1]