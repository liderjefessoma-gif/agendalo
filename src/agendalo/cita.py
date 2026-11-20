RESERVADA = "Reservada"
CANCELADA = "Cancelada"
ATENDIDA = "Atendida"


class Cita:
    """Una cita de un paciente con un médico, en una fecha y hora."""

    def __init__(self, codigo, paciente, medico, fecha_hora):
        self.codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora
        self.estado = RESERVADA

    def describir(self):
        """Devuelve, por ejemplo: 25/11/2026 09:30 — Dr. Luis Fernández Soto."""
        fecha_y_hora = self.fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"{fecha_y_hora} — Dr. {self.medico.nombre_completo()}"
