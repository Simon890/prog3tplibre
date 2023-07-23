from ..Nodo import Nodo
from .Algoritmo import Algoritmo
from .Solucion import Solucion
from .Fallo import Fallo


class Tabu(Algoritmo):
    
    IT_MAX = 1000
    TABU_MAX = 50
    
    def resolver(self):
        actual = Nodo(0, self.problema.estado_inicial, None, None)
        tabu = [actual.estado]
        for _ in range(self.IT_MAX):
            acciones = self.problema.acciones(actual)
            acciones_cand = []

            for accion in acciones:
                nuevo_estado = self.problema.resultado(actual.estado, accion)
                if nuevo_estado not in tabu:
                    acciones_cand.append((accion, self._heuristica(nuevo_estado)))
            if len(acciones_cand) == 0: print(len(acciones_cand))
            if not acciones_cand:
                acciones_cand = [(accion, self._heuristica(self.problema.resultado(actual.estado, accion))) for accion in acciones]
            
            acciones_cand.sort(key=lambda x: x[1])
            mejor_accion = acciones_cand[0][0]
            nuevo_estado = self.problema.resultado(actual.estado, mejor_accion)
            nuevo_nodo = Nodo(self.problema.costo(actual.estado, mejor_accion), nuevo_estado, actual, mejor_accion)
            tabu.append(nuevo_nodo.estado)
            
            if len(tabu) > self.TABU_MAX:
                tabu.pop(0)
            actual = nuevo_nodo
            
            if self.problema.test_objetivo(actual.estado):
                return Solucion(actual)
        raise Fallo()