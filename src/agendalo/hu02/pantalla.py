from agendalo.clinica import ERROR_CMP_REPETIDO
from agendalo.medico import DIAS, ESPECIALIDADES, Medico
from agendalo.validaciones import (
    validar_cmp,
    validar_dias,
    validar_especialidad,
    validar_hora,
    validar_nombre,
)


def pantalla_registrar_medico(clinica):
    """Pide los datos del médico, uno por uno, y lo registra en la clínica."""
    print("===== REGISTRAR MÉDICO =====")

    while True:
        try:
            cmp = validar_cmp(input("CMP: "))
            if clinica.buscar_medico(cmp) is None:
                break
            print(ERROR_CMP_REPETIDO)
        except ValueError as error:
            print(error)

    while True:
        try:
            nombres = validar_nombre(input("Nombres: "))
            break
        except ValueError as error:
            print(error)

    while True:
        try:
            apellidos = validar_nombre(input("Apellidos: "))
            break
        except ValueError as error:
            print(error)

    print("Especialidad:")
    for numero in ESPECIALIDADES:
        print(f"  {numero}. {ESPECIALIDADES[numero]}")

    while True:
        try:
            especialidad = validar_especialidad(input("Elija el número de la especialidad: "))
            break
        except ValueError as error:
            print(error)

    print("Días de atención:")
    for letra in DIAS:
        print(f"  {letra}. {DIAS[letra]}")

    while True:
        try:
            dias = validar_dias(input("Escriba las letras de los días, separadas por espacios: "))
            break
        except ValueError as error:
            print(error)

    while True:
        try:
            hora_inicio = validar_hora(input("Hora de inicio (HH:MM): "))
            break
        except ValueError as error:
            print(error)

    while True:
        try:
            hora_fin = validar_hora(input("Hora de fin (HH:MM): "), hora_inicio)
            break
        except ValueError as error:
            print(error)

    medico = Medico(cmp, nombres, apellidos, especialidad, dias, hora_inicio, hora_fin)
    clinica.registrar_medico(medico)
    print(f">> Médico registrado: {medico.describir()}")
    print(f"   CMP: {medico.cmp}")
    print("   Días de atención:")
    for letra in medico.dias:
        print(f"     - {DIAS[letra]}")
    print(f"   Horario: de {medico.hora_inicio.strftime('%H:%M')} a {medico.hora_fin.strftime('%H:%M')}")
    input("Presione Enter para volver al menú.")
