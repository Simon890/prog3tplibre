class Fallo(Exception):
    def __init__(self):
        super().__init__("No se encontró una solución")