class Persona:
    def __init__(self, id_persona: int, nombre: str, apellido: str, cedula: str, correo: str, telefono: str, estado: str):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono
        self.estado = estado

    def crear_persona(self) -> None:
        pass

    def actualizar_persona(self) -> None:
        pass

    def eliminar_persona(self) -> None:
        pass