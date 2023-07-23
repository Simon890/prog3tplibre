from src.algoritmo.Tabu import Tabu
from src.algoritmo.Frontera import Frontera
from src.Nodo import Nodo
from src.algoritmo.Problema import Problema
from src.algoritmo.AEstrella import AEstrella
from src.algoritmo.Accion import Accion

# f = Frontera()
# # f.encolar(Nodo(), 3)
# # f.encolar(Nodo(), 5)
# # f.encolar(Nodo(), 1)
# # print(p.test_objetivo([[1, 3, 2], [4, 5, 6], [7, 8, 0]]))
# print(p.acciones(Nodo(0, [[1, 3, 2], [4, 5, 6], [7, 0, 8]], None)))
# # print(f.desencolar(), f.desencolar(), f.desencolar(), f.desencolar())

# p = Problema([[1, 5, 8], [7, 0, 6], [2, 4, 3]])
p = Problema([[1, 2, 3], [5, 6, 0], [7, 8, 4]])

# algo = AEstrella(p)
# solucion = algo.resolver()
# solucion.mostrarJugada()
algo = Tabu(p)
solucion = algo.resolver()
solucion.mostrarJugada()