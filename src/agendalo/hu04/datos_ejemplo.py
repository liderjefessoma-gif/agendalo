from datetime import datetime, time

from agendalo.clinica import ERROR_CITA_NO_ENCONTRADA
from agendalo.hu03.datos_ejemplo import mostrar_citas, proximo_martes


def cargar_datos_ejemplo(clinica):
    """HU04 usa las citas de ejemplo de HU03, así que no registra nada nuevo."""
    return


def mostrar_pruebas(clinica):
    """Muestra una reprogramación válida y un caso rechazado por cada regla de HU04."""
    print("===== HU04 REPROGRAMAR CITA: DATOS DE EJEMPLO =====")
    martes = proximo_martes()

    print("----- Reprogramación válida -----")
    cita = clinica.buscar_cita("C0002")
    fecha_anterior = cita.fecha_hora.strftime("%d/%m/%Y %H:%M")
    clinica.reprogramar_cita(cita, datetime.combine(martes, time(11, 0)))
    print(f"C0002 de {fecha_anterior} a {cita.fecha_hora.strftime('%d/%m/%Y %H:%M')}:")
    print(f">> Cita {cita.codigo} reprogramada.")

    print("----- Casos rechazados -----")

    print("Código C9999:")
    if clinica.buscar_cita("C9999") is None:
        print(ERROR_CITA_NO_ENCONTRADA)

    print("C0003, que está Cancelada:")
    try:
        clinica.reprogramar_cita(clinica.buscar_cita("C0003"), datetime.combine(martes, time(16, 30)))
    except ValueError as error:
        print(error)

    print("C0001 a las 11:00, ya ocupado por C0002:")
    try:
        clinica.reprogramar_cita(clinica.buscar_cita("C0001"), datetime.combine(martes, time(11, 0)))
    except ValueError as error:
        print(error)

    print("Citas después de reprogramar:")
    mostrar_citas(clinica)
