from datetime import date, datetime, time, timedelta

from agendalo.clinica import ERROR_PACIENTE_NO_ENCONTRADO
from agendalo.hu02.datos_ejemplo import crear_medico_ejemplo
from agendalo.paciente import Paciente
from agendalo.validaciones import validar_dni, validar_fecha


def proximo_martes():
    """Devuelve la fecha del próximo martes, para que las citas de ejemplo nunca queden en el pasado."""
    fecha = date.today() + timedelta(days=1)
    while fecha.weekday() != 1:
        fecha = fecha + timedelta(days=1)

    return fecha


def cargar_datos_ejemplo(clinica):
    """Registra una médica, dos pacientes y cuatro citas de ejemplo, sin mostrar nada en pantalla."""
    carmen = crear_medico_ejemplo("072345", "Carmen", "Ruiz Paz", "1", "L M X J V", "14:00", "19:00")
    clinica.registrar_medico(carmen)

    ana_maria = Paciente("45678912", "Ana María", "Quispe Rojas", "987654321", date(1990, 3, 14))
    clinica.registrar_paciente(ana_maria)

    jorge = Paciente("41234567", "Jorge", "Salas Medina", "912345678", date(1985, 8, 2))
    clinica.registrar_paciente(jorge)

    luis = clinica.buscar_medico("054321")
    ana_rios = clinica.buscar_medico("061234")
    martes = proximo_martes()

    clinica.reservar_cita(ana_maria, luis, datetime.combine(martes, time(9, 0)))
    clinica.reservar_cita(jorge, luis, datetime.combine(martes, time(10, 0)))

    cita_cancelada = clinica.reservar_cita(jorge, ana_rios, datetime.combine(martes, time(14, 0)))
    clinica.cancelar_cita(cita_cancelada)

    clinica.reservar_cita(ana_maria, ana_rios, datetime.combine(martes, time(15, 0)))


def mostrar_citas(clinica):
    """Muestra todas las citas con su código, paciente y estado."""
    for cita in clinica.citas:
        print(f"- {cita.codigo}: {cita.describir()} — {cita.paciente.nombre_completo()} ({cita.estado})")


def mostrar_pruebas(clinica):
    """Muestra los datos de ejemplo, una reserva válida y un caso rechazado por cada regla de HU03."""
    print("===== HU03 RESERVAR CITA: DATOS DE EJEMPLO =====")
    print("Pacientes de ejemplo registrados:")
    for paciente in clinica.pacientes:
        print(f"- {paciente.describir()}")

    print("Citas de ejemplo:")
    mostrar_citas(clinica)

    ana_maria = clinica.buscar_paciente("45678912")
    jorge = clinica.buscar_paciente("41234567")
    luis = clinica.buscar_medico("054321")
    carmen = clinica.buscar_medico("072345")
    martes = proximo_martes()

    print("----- Reserva válida -----")
    cita = clinica.reservar_cita(jorge, carmen, datetime.combine(martes, time(16, 0)))
    print(f">> Cita reservada. Código: {cita.codigo}")
    print(f"   {cita.describir()}")

    print("----- Casos rechazados -----")

    print("DNI con 4 dígitos:")
    try:
        validar_dni("4567")
    except ValueError as error:
        print(error)

    print("DNI no registrado (99999999):")
    if clinica.buscar_paciente("99999999") is None:
        print(ERROR_PACIENTE_NO_ENCONTRADO)

    print("Fecha 2026-11-25:")
    try:
        validar_fecha("2026-11-25")
    except ValueError as error:
        print(error)

    print("Fecha 01/01/2020:")
    try:
        clinica.reservar_cita(ana_maria, luis, datetime(2020, 1, 1, 9, 0))
    except ValueError as error:
        print(error)

    print("Dr. Luis un sábado:")
    sabado = martes + timedelta(days=4)
    try:
        clinica.reservar_cita(ana_maria, luis, datetime.combine(sabado, time(9, 0)))
    except ValueError as error:
        print(error)

    print("Dr. Luis a las 15:00:")
    try:
        clinica.reservar_cita(ana_maria, luis, datetime.combine(martes, time(15, 0)))
    except ValueError as error:
        print(error)

    print("Dr. Luis a las 09:00, ya ocupado por C0001:")
    try:
        clinica.reservar_cita(jorge, luis, datetime.combine(martes, time(9, 0)))
    except ValueError as error:
        print(error)

    print("Ana María con la Dra. Carmen a las 15:00, pero ya tiene C0004 a esa hora:")
    try:
        clinica.reservar_cita(ana_maria, carmen, datetime.combine(martes, time(15, 0)))
    except ValueError as error:
        print(error)
