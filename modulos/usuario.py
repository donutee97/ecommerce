from .persona import Persona

class Usuario:
    def __init__(self, id_usuario: int, usuario: str, contrasena: str, persona: Persona):
        self.id_usuario = id_usuario
        self.usuario = usuario
        self.contrasena = contrasena
        self.persona = persona  # Relación 1 a 1 con Persona

    def get_account() -> str:
        pass

    def set_account(account: str) -> None:
        pass