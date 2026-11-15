from agendalo.persona import Persona

ESPECIALIDADES = {
    "1": "Medicina general",
    "2": "Cardiología",
    "3": "Pediatría",
}

DIAS = {
    "L": "Lunes",
    "M": "Martes",
    "X": "Miércoles",
    "J": "Jueves",
    "V": "Viernes",
    "S": "Sábado",
}


class Medico(Persona):
    """Un médico de la clínica, con su especialidad y su horario de atención."""

    def __init__(self, cmp, nombres, apellidos, especialidad, dias, hora_inicio, hora_fin):
        super().__init__(nombres, apellidos)
        self.cmp = cmp
        self.especialidad = especialidad
        self.dias = dias
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def describir(self):
        """Devuelve, por ejemplo: Dr. Luis Fernández Soto — Cardiología."""
        return f"Dr. {self.nombre_completo()} — {self.especialidad}"
