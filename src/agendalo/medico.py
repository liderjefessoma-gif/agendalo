from datetime import datetime, timedelta

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

LETRAS_DE_LA_SEMANA = ["L", "M", "X", "J", "V", "S", "D"]


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

    def horario_en_texto(self):
        """Devuelve, por ejemplo: 08:00 a 13:00."""
        return f"{self.hora_inicio.strftime('%H:%M')} a {self.hora_fin.strftime('%H:%M')}"

    def horarios_del_dia(self, fecha):
        """Devuelve las horas de sus bloques de 30 minutos en esa fecha, o una lista vacía si no atiende ese día."""
        letra_del_dia = LETRAS_DE_LA_SEMANA[fecha.weekday()]
        if letra_del_dia not in self.dias:
            return []

        horarios = []
        bloque = datetime.combine(fecha, self.hora_inicio)
        fin = datetime.combine(fecha, self.hora_fin)
        while bloque < fin:
            horarios.append(bloque.time())
            bloque = bloque + timedelta(minutes=30)

        return horarios
