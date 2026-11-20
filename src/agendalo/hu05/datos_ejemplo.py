from datetime import datetime, time

from agendalo.clinica import ERROR_CITA_NO_ENCONTRADA
from agendalo.hu03.datos_ejemplo import mostrar_citas, proximo_martes


def cargar_datos_ejemplo(clinica):
    """HU05 usa las citas de ejemplo de HU03, así que no registra nada nuevo."""
    return


def mostrar_pruebas(clinica):
    """Muestra una cancelación válida, que el horario queda libre y un caso rechazado por cada regla de HU05."""
    print("===== HU05 CANCELAR CITA: DATOS DE EJEMPLO =====")

    print("----- Cancelación válida -----")
    cita = clinica.buscar_cita("C0001")
    clinica.cancelar_cita(cita)
    print(f">> Cita {cita.codigo} cancelada. El horario quedó libre.")

    print("El horario de C0001 se puede reservar otra vez:")
    jorge = clinica.buscar_paciente("41234567")
    nueva = clinica.reservar_cita(jorge, cita.medico, datetime.combine(proximo_martes(), time(9, 0)))
    print(f">> Cita reservada. Código: {nueva.codigo}")
    print(f"   {nueva.describir()}")

    print("----- Casos rechazados -----")

    print("Código C9999:")
    if clinica.buscar_cita("C9999") is None:
        print(ERROR_CITA_NO_ENCONTRADA)

    print("C0001 otra vez, que ya está Cancelada:")
    try:
        clinica.cancelar_cita(cita)
    except ValueError as error:
        print(error)

    print("Citas después de cancelar:")
    mostrar_citas(clinica)
