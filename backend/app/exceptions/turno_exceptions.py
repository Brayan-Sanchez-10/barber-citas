class NoExisteTurno(Exception):
    def __init__(self, id_turno : int):
        self.id_turno = id_turno
        super().__init__(f"No existe Turno con id: {self.id_turno}")

class TurnoNoSeCreo(Exception):
    def __init__(self):
        super().__init__(f"No se logro crear el Turno")

class TurnoNoSeEdito(Exception):
    def __init__(self, id_turno: int):
        self.id_turno = id_turno
        super().__init__(f"No se le logro editar el Turno con id: {self.id_turno}")

class TurnoNoSeModificoEstado(Exception):
    def __init__(self, id_turno: int):
        self.id_turno = id_turno
        super().__init__(f"No se logro Modificar el estado del turno con id: {self.id_turno}")
