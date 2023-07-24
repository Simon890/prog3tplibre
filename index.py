from src.algoritmo.Tabu import Tabu
from src.algoritmo.Problema import Problema
from src.algoritmo.AEstrella import AEstrella
import sys

try:
    
    ESTADO = [
        [1, 2, 3], 
        [5, 6, 0], 
        [7, 8, 4]
    ]

    p = Problema(ESTADO)
    algoritmo = sys.argv[1] if len(sys.argv) == 2 else "aestrella"
    algo = None

    if algoritmo == "tabu":
        print("ALGORITMO TABÚ\n")
        algo = Tabu(p)
    elif algoritmo == "aestrella":
        print("ALGORITMO A ESTRELLA\n")
        algo = AEstrella(p)

    solucion = algo.resolver()
    solucion.mostrarJugada()
except Exception as ex:
    print("Ha ocurrido un error:", str(ex))