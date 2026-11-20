from agendalo.persona import Persona


class Paciente(Persona):
    """Un paciente de la clínica, con su DNI y sus datos de contacto."""

    def __init__(self, dni, nombres, apellidos, telefono, fecha_nacimiento):
        super().__init__(nombres, apellidos)
        self.dni = dni
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento

    def describir(self):
        """Devuelve, por ejemplo: Ana María Quispe Rojas (DNI 45678912)."""
        return f"{self.nombre_completo()} (DNI {self.dni})"
