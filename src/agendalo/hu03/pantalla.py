from datetime import datetime

from agendalo.clinica import ERROR_PACIENTE_NO_ENCONTRADO, ERROR_SIN_HORARIOS_LIBRES
from agendalo.validaciones import validar_dni, validar_fecha, validar_hora

ERROR_OPCION_LISTA = ">> Error: opción no válida. Elija un número de la lista."


def pedir_fecha_y_hora(clinica, paciente, medico, texto_fecha, texto_hora, cita_a_ignorar=None):
    """Pide una fecha, muestra los horarios libres del médico y pide una hora libre. Devuelve la fecha y hora."""
    while True:
        try:
            fecha = validar_fecha(input(texto_fecha))
            clinica.validar_fecha_de_cita(medico, fecha)
            libres = clinica.horarios_libres(medico, fecha, cita_a_ignorar)
            if len(libres) > 0:
                break
            print(ERROR_SIN_HORARIOS_LIBRES)
        except ValueError as error:
            print(error)

    texto_libres = ""
    for hora in libres:
        texto_libres = texto_libres + hora.strftime("%H:%M") + "  "
    print("Horarios libres: " + texto_libres.strip())

    while True:
        try:
            hora = validar_hora(input(texto_hora))
            fecha_hora = datetime.combine(fecha, hora)
            clinica.validar_disponibilidad(paciente, medico, fecha_hora, cita_a_ignorar)
            return fecha_hora
        except ValueError as error:
            print(error)


def pantalla_reservar_cita(clinica):
    """Pide el paciente, el médico, la fecha y la hora, y reserva la cita."""
    print("===== RESERVAR CITA =====")

    while True:
        try:
            texto = input("DNI del paciente (0 para volver): ").strip()
            if texto == "0":
                return
            dni = validar_dni(texto)
            paciente = clinica.buscar_paciente(dni)
            if paciente is not None:
                break
            print(ERROR_PACIENTE_NO_ENCONTRADO)
        except ValueError as error:
            print(error)

    print(f">> Paciente: {paciente.describir()}")

    print("Médicos:")
    numero = 1
    for medico in clinica.medicos:
        print(f"  {numero}. {medico.describir()} — {medico.horario_en_texto()}")
        numero = numero + 1

    while True:
        texto = input("Elija el número del médico: ").strip()
        if texto.isdigit() and int(texto) >= 1 and int(texto) <= len(clinica.medicos):
            medico = clinica.medicos[int(texto) - 1]
            break
        print(ERROR_OPCION_LISTA)

    fecha_hora = pedir_fecha_y_hora(clinica, paciente, medico, "Fecha (DD/MM/AAAA): ", "Hora (HH:MM): ")

    cita = clinica.reservar_cita(paciente, medico, fecha_hora)
    print(f">> Cita reservada. Código: {cita.codigo}")
    print(f"   {cita.describir()}")
    input("Presione Enter para volver al menú.")
