class NoExisteBarbero(Exception):
    def __init__ (self, id_barbero: str):
        self.id_barbero = id_barbero
        super().__init__(f"No existe barbero con id: {id_barbero}")

class YaExisteBarberoConEseID(Exception):
    def __init__ (self, id_barbero: str):
        self.id_barbero = id_barbero
        super().__init__(f"Ya existe un barbero con id: {id_barbero}")

class ContrasenaIncorrecta(Exception):
    def __init__(self):
        super().__init__("La contraseña es incorrecta")

class ContrasenaNoCoinciden(Exception):
    def __init__(self):
        super().__init__("La contraseña nueva no es igual a la confirmacion")


class ContrasenaNoSeActualizo(Exception):
    def __init__(self):
        super().__init__("No se logro actualizar la contrasena")

class BarberoNoSeElimino(Exception):
    def __init__(self, id_barbero: str):
        self.id_barbero = id_barbero
        super().__init__(f"No se logro eliminar el Barbero con id: {id_barbero}")

class BarberoNoSeActualizo(Exception):
    def __init__(self, id_barbero: str):
        self.id_barbero = id_barbero
        super().__init__(f"No se logro actualizar el Barbero con id: {id_barbero}")

class BarberoNoSeCreo(Exception):
    def __init__(self):
        super().__init__(f"No se logro crear el Barbero")