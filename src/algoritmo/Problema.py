from .Estado import Estado
from ..Nodo import Nodo
from typing import Tuple, List
from .Accion import Accion
from copy import deepcopy
from random import randint
import itertools

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
        if not self._check_paridad(): raise Exception("El problema no posee paridad")
    
    def test_objetivo(self, estado: Estado):
        """
        Dado un estado, retorna True si corresponde con el estado objetivo
        """
        for i, fila in enumerate(self.ESTADO_FINAL):
            for j, nro in enumerate(fila):
                if nro != estado[i][j]: return False
        return True

    def acciones(self, nodo: Nodo) -> List[Accion]:
        """
        Retorna una lista de acciones posibles que se pueden realizar en un estado particular
        """
        p_cero = self._encontrar_cero(nodo.estado)
        
        #Si el cero está en el centro:
        if p_cero == (1, 1): return [Accion.ARRIBA, Accion.ABAJO, Accion.IZQ, Accion.DER]
        
        #Si el cero está en las esquinas:
        if p_cero == (0, 0): return [Accion.ABAJO, Accion.DER]
        if p_cero == (2, 0): return [Accion.ARRIBA, Accion.DER]
        if p_cero == (2, 2): return [Accion.ARRIBA, Accion.IZQ]
        if p_cero == (0, 2): return [Accion.ABAJO, Accion.IZQ]
        
        #Si el cero está en las aristas:
        if p_cero == (1, 0): return [Accion.ARRIBA, Accion.ABAJO, Accion.DER]
        if p_cero == (0, 1): return [Accion.ABAJO, Accion.IZQ, Accion.DER]
        if p_cero == (1, 2): return [Accion.ARRIBA, Accion.ABAJO, Accion.IZQ]
        if p_cero == (2, 1): return [Accion.ARRIBA, Accion.IZQ, Accion.DER]
    
    def costo(self, estado: Estado, accion: Accion):
        return 1 #El costo siempre es uno para cualquier acción

    def resultado(self, estado: Estado, accion: Accion) -> Estado:
        """
        Retorna un nuevo estado resultado de haber aplicado una acción a un estado anterior.
        """
        p_cero = self._encontrar_cero(estado)
        nuevo_estado : Estado = deepcopy(estado)
        if accion == Accion.DER:
            val = nuevo_estado[p_cero[0]][p_cero[1] + 1]
            nuevo_estado[p_cero[0]][p_cero[1]] = val
            nuevo_estado[p_cero[0]][p_cero[1] + 1] = 0
            return nuevo_estado
        if accion == Accion.IZQ:
            val = nuevo_estado[p_cero[0]][p_cero[1] - 1]
            nuevo_estado[p_cero[0]][p_cero[1]] = val
            nuevo_estado[p_cero[0]][p_cero[1] - 1] = 0
            return nuevo_estado
        if accion == Accion.ABAJO:
            val = nuevo_estado[p_cero[0] + 1][p_cero[1]]
            nuevo_estado[p_cero[0]][p_cero[1]] = val
            nuevo_estado[p_cero[0] + 1][p_cero[1]] = 0
            return nuevo_estado
        if accion == Accion.ARRIBA:
            val = nuevo_estado[p_cero[0] - 1][p_cero[1]]
            nuevo_estado[p_cero[0]][p_cero[1]] = val
            nuevo_estado[p_cero[0] - 1][p_cero[1]] = 0
            return nuevo_estado

    def _encontrar_cero(self, estado: Estado) -> Tuple[int, int]:
        """
        Retorna una tupla indicando la posición del número cero (vacío)
        """
        for i, fila in enumerate(estado):
            for j, nro in enumerate(fila):
                if nro == 0: return (i, j)
        raise Exception("No hay un cero en el estado")
    
    def _check_paridad(self):
        """
        Verifica que el estado inicial cumpla con la condición de paridad.
        (Tiene cantidad par de inversiones)
        """
        inicial = list(itertools.chain(*self.estado_inicial))
        inver_inicial = 0
        for i in range(len(inicial)):
            for j in range(i + 1, len(inicial)):
                if inicial[i] > inicial[j] and inicial[i] != 0 and inicial[j] != 0:
                    inver_inicial += 1
        return inver_inicial % 2 == 0