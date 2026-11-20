from agendalo.cita import RESERVADA
from agendalo.clinica import ERROR_CITA_NO_ENCONTRADA, ERROR_REPROGRAMAR_NO_RESERVADA
from agendalo.hu03.pantalla import pedir_fecha_y_hora
from agendalo.validaciones import validar_confirmacion


def pantalla_reprogramar_cita(clinica):
    """Pide el código de una cita reservada, una nueva fecha y hora, y la reprograma si el usuario confirma."""
    print("===== REPROGRAMAR CITA =====")

    while True:
        codigo = input("Código de cita (0 para volver): ").strip().upper()
        if codigo == "0":
            return
        cita = clinica.buscar_cita(codigo)
        if cita is None:
            print(ERROR_CITA_NO_ENCONTRADA)
        elif cita.estado != RESERVADA:
            print(ERROR_REPROGRAMAR_NO_RESERVADA)
        else:
            break

    print(f">> Cita actual: {cita.describir()}")
    print(f"   Paciente: {cita.paciente.nombre_completo()}")

    nueva_fecha_hora = pedir_fecha_y_hora(
        clinica,
        cita.paciente,
        cita.medico,
        "Nueva fecha (DD/MM/AAAA): ",
        "Nueva hora (HH:MM): ",
        cita,
    )

    fecha_anterior = cita.fecha_hora.strftime("%d/%m/%Y %H:%M")
    fecha_nueva = nueva_fecha_hora.strftime("%d/%m/%Y %H:%M")
    while True:
        try:
            confirma = validar_confirmacion(input(f"Cambiar de {fecha_anterior} a {fecha_nueva}. ¿Confirmar? (S/N): "))
            break
        except ValueError as error:
            print(error)

    if confirma:
        clinica.reprogramar_cita(cita, nueva_fecha_hora)
        print(f">> Cita {cita.codigo} reprogramada.")
    else:
        print(">> No se hicieron cambios.")

    input("Presione Enter para volver al menú.")
