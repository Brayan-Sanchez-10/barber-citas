class NoExisteServicio(Exception):
    def __init__(self, id_servicio: int):
        self.id_servicio = id_servicio
        super().__init__(f"No existe Servicio con id: {self.id_servicio}")

class ServicioNoSeCreo(Exception):
    def __init__ (self):
        super().__init__(f"No se logro crear el Servicio")

class ServicioNoSeActualizo(Exception):
    def __init__(self, id_servicio: int):
        super().__init__(f"No se logro actualizar el Servicio con id: {self.id_servicio}")

class ServicioNoSeElimino(Exception):
    def __init__(self, id_servicio: int):
        super().__init__(f"No se logro eliminar el Servicio con id: {self.id_servicio}")