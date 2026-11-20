from datetime import date, datetime

from agendalo.cita import CANCELADA, RESERVADA, Cita

ERROR_CMP_REPETIDO = ">> Error: el CMP ya está registrado. Ingrese otro CMP."
ERROR_DNI_REPETIDO = ">> Error: el DNI ya está registrado. Ingrese otro DNI."
ERROR_PACIENTE_NO_ENCONTRADO = ">> Error: paciente no encontrado. Verifique el DNI."
ERROR_CITA_NO_ENCONTRADA = ">> Error: cita no encontrada."
ERROR_FECHA_PASADA = ">> Error: la fecha ya pasó."
ERROR_DIA_SIN_ATENCION = ">> Error: el médico no atiende ese día."
ERROR_SIN_HORARIOS_LIBRES = ">> Error: el médico no tiene horarios libres ese día. Elija otra fecha."
ERROR_HORARIO_OCUPADO = ">> Error: horario ocupado. Elija uno de los horarios libres."
ERROR_PACIENTE_OCUPADO = ">> Error: el paciente ya tiene una cita a esa hora."
ERROR_REPROGRAMAR_NO_RESERVADA = '>> Error: solo se reprograman citas en estado "Reservada".'
ERROR_CANCELAR_NO_RESERVADA = '>> Error: solo se cancelan citas en estado "Reservada".'


class Clinica:
    """Guarda en memoria los médicos, los pacientes y las citas."""

    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.citas = []

    def registrar_medico(self, medico):
        """Agrega el médico a la lista, si su CMP todavía está libre."""
        if self.buscar_medico(medico.cmp) is not None:
            raise ValueError(ERROR_CMP_REPETIDO)

        self.medicos.append(medico)

    def buscar_medico(self, cmp):
        """Devuelve el médico con ese CMP, o None si nadie lo tiene."""
        for medico in self.medicos:
            if medico.cmp == cmp:
                return medico

        return None

    def registrar_paciente(self, paciente):
        """Agrega el paciente a la lista, si su DNI todavía está libre."""
        if self.buscar_paciente(paciente.dni) is not None:
            raise ValueError(ERROR_DNI_REPETIDO)

        self.pacientes.append(paciente)

    def buscar_paciente(self, dni):
        """Devuelve el paciente con ese DNI, o None si nadie lo tiene."""
        for paciente in self.pacientes:
            if paciente.dni == dni:
                return paciente

        return None

    def buscar_cita(self, codigo):
        """Devuelve la cita con ese código, o None si no existe."""
        for cita in self.citas:
            if cita.codigo == codigo:
                return cita

        return None

    def medico_ocupado(self, medico, fecha_hora, cita_a_ignorar=None):
        """Dice si el médico ya tiene una cita reservada en esa fecha y hora."""
        for cita in self.citas:
            if cita is cita_a_ignorar:
                continue
            if cita.estado == RESERVADA and cita.medico is medico and cita.fecha_hora == fecha_hora:
                return True

        return False

    def paciente_ocupado(self, paciente, fecha_hora, cita_a_ignorar=None):
        """Dice si el paciente ya tiene una cita reservada en esa fecha y hora."""
        for cita in self.citas:
            if cita is cita_a_ignorar:
                continue
            if cita.estado == RESERVADA and cita.paciente is paciente and cita.fecha_hora == fecha_hora:
                return True

        return False

    def horarios_libres(self, medico, fecha, cita_a_ignorar=None):
        """Devuelve las horas del médico en esa fecha que todavía no pasaron y no tienen cita."""
        ahora = datetime.now()
        libres = []
        for hora in medico.horarios_del_dia(fecha):
            fecha_hora = datetime.combine(fecha, hora)
            if fecha_hora > ahora and not self.medico_ocupado(medico, fecha_hora, cita_a_ignorar):
                libres.append(hora)

        return libres

    def validar_fecha_de_cita(self, medico, fecha):
        """Revisa que la fecha no haya pasado y que el médico atienda ese día."""
        if fecha < date.today():
            raise ValueError(ERROR_FECHA_PASADA)

        if len(medico.horarios_del_dia(fecha)) == 0:
            raise ValueError(ERROR_DIA_SIN_ATENCION)

    def validar_disponibilidad(self, paciente, medico, fecha_hora, cita_a_ignorar=None):
        """Revisa todas las reglas para reservar o reprogramar una cita. Lanza ValueError si alguna falla."""
        if fecha_hora <= datetime.now():
            raise ValueError(ERROR_FECHA_PASADA)

        horarios = medico.horarios_del_dia(fecha_hora.date())
        if len(horarios) == 0:
            raise ValueError(ERROR_DIA_SIN_ATENCION)

        if fecha_hora.time() not in horarios:
            raise ValueError(f">> Error: la hora está fuera del horario del médico ({medico.horario_en_texto()}).")

        if self.medico_ocupado(medico, fecha_hora, cita_a_ignorar):
            raise ValueError(ERROR_HORARIO_OCUPADO)

        if self.paciente_ocupado(paciente, fecha_hora, cita_a_ignorar):
            raise ValueError(ERROR_PACIENTE_OCUPADO)

    def reservar_cita(self, paciente, medico, fecha_hora):
        """Crea una cita reservada con un código nuevo y la devuelve."""
        self.validar_disponibilidad(paciente, medico, fecha_hora)

        numero = len(self.citas) + 1
        codigo = "C" + str(numero).zfill(4)
        cita = Cita(codigo, paciente, medico, fecha_hora)
        self.citas.append(cita)
        return cita

    def reprogramar_cita(self, cita, nueva_fecha_hora):
        """Cambia la fecha y hora de una cita reservada, con las mismas reglas de una reserva."""
        if cita.estado != RESERVADA:
            raise ValueError(ERROR_REPROGRAMAR_NO_RESERVADA)

        self.validar_disponibilidad(cita.paciente, cita.medico, nueva_fecha_hora, cita)
        cita.fecha_hora = nueva_fecha_hora

    def cancelar_cita(self, cita):
        """Marca la cita como cancelada. No la borra y su horario queda libre."""
        if cita.estado != RESERVADA:
            raise ValueError(ERROR_CANCELAR_NO_RESERVADA)

        cita.estado = CANCELADA
