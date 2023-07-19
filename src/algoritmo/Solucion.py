from ..Nodo import Nodo
from typing import List
class Solucion:
    nodo: Nodo = None
    def __init__(self, nodo: Nodo):
        self.nodo = nodo
        
    def mostrarJugada(self):
        nodos: List[Nodo] = [self.nodo]
        padre = self.nodo.padre
        while padre:
            nodos.append(padre)
            padre = padre.padre
        nodos.reverse()
        for nodo in nodos:
            for nro, fila in enumerate(nodo.estado):
                for val in fila:
                    print(f"[{' ' if val == 0 else val}]", end="")
                if nro == 1 and nodo.accion:
                    print(f" Acción: {nodo.accion.value}")
                else:
                    print("")
            print("")