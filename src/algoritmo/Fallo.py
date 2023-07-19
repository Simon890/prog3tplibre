class Fallo(Exception):
    def __init__(self):
        super().__init__(message="No se encontró una solución")