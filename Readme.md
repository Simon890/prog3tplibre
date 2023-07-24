# Trabajo Práctico Programación 3 (Libre)

## Profesores: 
* Mauro Lucci
* Valentina Bini
* Damián Ariel Marotte

## Alumno:
* Simón Revello

### Enunciado: Resolver el 8-puzzle utilizando los algoritmos A* y Tabú. Además, verificar que el estado inicial posea solución

--- 
### Pasos para ejecutar el programa
1. En el archivo index.py se puede establecer el estado inicial en la variable ESTADO
2. Para determinar el tipo de algoritmo a ejecutar, pasar el nombre del mismo por parámetros en la consola.
#### Tabú:
```
python index.py tabu
```
#### A*:
```
python index.py aestrella
```

## Explicación de la estructura del código:
### Nodo.py
#### Almacena el estado, la acción aplicada, el costo de acción y el nodo padre
### Accion.py
#### Es una enumeración de acciones posibles (ARRIBA, ABAJO, IZQUIERDA, DERECHA)
### Problema.py
#### Representa el problema a solucionar. Posee un estado inicial, y varios métodos:
* test_objetivo() -> Dado un estado, retorna True si es un estado final
* acciones() -> Dado un nodo, retorna una lista de las acciones posibles que se pueden realizar en el estado de ese nodo
* cost() -> siempre retorna 1
* resultado() -> Dado un estado y una acción retorna uno nuevo, resultado de haber aplicado esa acción al estado anterior
* _encontrar_cero() -> Dado un estado, retorna una tupla indicando la posición en donde está el 0 (vacío)
* _check_paridad() -> Verifica que el estado inicial tenga solución
### Solucion.py
#### La solución obtenida. Acepta como parámetro el nodo final. Método:
* mostrarJugada() -> Muestra por consola todos los estados con las acciones aplicadas
### Frontera.py
#### Cola de prioridad en donde se guardan los nodos. Se utiliza para el algoritmo A*. Métodos:
* encolar() -> Agrega un nodo en la lista
* desencolar() -> Retorna el nodo con el menor valor
### Algoritmo.py
#### Clase abstracta que representa un algoritmo de búsqueda. Métodos:
* [abstracto] resolver() -> Cada clase que extienda de Algoritmo debe implementar este método
* _heuristica() -> Dado un estado, retorna su valor heurístico
### AEstrella.py
#### Clase que extiende de la clase Algoritmo e implementa el algoritmo A*
### Tabu.py
#### Clase que extiende de la clase Algoritmo e implementa el algoritmo Tabú
### Estado.py
#### Define un tipo de dato personalizado que representa un estado
### Fallo.py
#### Excepción que se lanza cuando no se encuentra una solución