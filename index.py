from src.algoritmo.Tabu import Tabu
from src.algoritmo.Problema import Problema
from src.algoritmo.AEstrella import AEstrella
import sys

ESTADO = [
    [1, 5, 8], 
    [7, 0, 6], 
    [2, 4, 3]
]


algoritmo = sys.argv[1] if len(sys.argv) == 2 else "aestrella"
p = Problema(ESTADO)
algo = None

if algoritmo == "tabu":
    print("ALGORITMO TABÚ\n")
    algo = Tabu(p)
elif algoritmo == "aestrella":
    print("ALGORITMO A ESTRELLA\n")
    algo = AEstrella(p)

solucion = algo.resolver()
solucion.mostrarJugada()