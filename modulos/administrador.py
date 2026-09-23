from .persona import Persona

class Administrador(Persona):
    def __init__(self, id_persona: int, nombre: str, apellido: str, cedula: str, correo: str, telefono: str, estado: str, id_administrador: int):
        super().__init__(id_persona, nombre, apellido, cedula, correo, telefono, estado)
        self.id_administrador = id_administrador

    def get_administrador() -> int:
        pass

    def set_administrador(id_administrador: int) -> None:
        pass