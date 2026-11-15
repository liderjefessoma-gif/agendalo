from datetime import time

from agendalo.medico import Medico
from agendalo.validaciones import (
    validar_cmp,
    validar_dias,
    validar_especialidad,
    validar_hora,
    validar_nombre,
)


def crear_medico_ejemplo(cmp, nombres, apellidos, especialidad, dias, hora_inicio, hora_fin):
    """Valida los datos de un médico de ejemplo y devuelve el médico creado."""
    cmp_valido = validar_cmp(cmp)
    nombres_validos = validar_nombre(nombres)
    apellidos_validos = validar_nombre(apellidos)
    especialidad_valida = validar_especialidad(especialidad)
    dias_validos = validar_dias(dias)
    hora_inicio_valida = validar_hora(hora_inicio)
    hora_fin_valida = validar_hora(hora_fin, hora_inicio_valida)

    return Medico(
        cmp_valido,
        nombres_validos,
        apellidos_validos,
        especialidad_valida,
        dias_validos,
        hora_inicio_valida,
        hora_fin_valida,
    )


def cargar_datos_ejemplo(clinica):
    """Registra los médicos de ejemplo en la clínica, sin mostrar nada en pantalla."""
    luis = crear_medico_ejemplo("054321", "Luis", "Fernández Soto", "2", "L M X J V", "08:00", "13:00")
    clinica.registrar_medico(luis)

    ana = crear_medico_ejemplo("061234", "Ana", "Ríos Paredes", "3", "M J S", "14:00", "18:30")
    clinica.registrar_medico(ana)


def mostrar_pruebas(clinica):
    """Muestra los médicos de ejemplo registrados y un caso rechazado por cada validación de HU02."""
    print("===== HU02 REGISTRAR MÉDICO: DATOS DE EJEMPLO =====")
    print("Médicos de ejemplo registrados:")
    for medico in clinica.medicos:
        print(f"- {medico.describir()} (CMP {medico.cmp})")

    print("----- Casos rechazados -----")

    print("CMP con 5 dígitos:")
    try:
        validar_cmp("12345")
    except ValueError as error:
        print(error)

    print("CMP ya registrado:")
    try:
        carla = crear_medico_ejemplo("054321", "Carla", "Mendoza Ruiz", "1", "L", "08:00", "12:00")
        clinica.registrar_medico(carla)
    except ValueError as error:
        print(error)

    print("Nombres vacíos:")
    try:
        validar_nombre("")
    except ValueError as error:
        print(error)

    print("Especialidad 4:")
    try:
        validar_especialidad("4")
    except ValueError as error:
        print(error)

    print("Días con la letra D:")
    try:
        validar_dias("L D")
    except ValueError as error:
        print(error)

    print("Hora 08:15:")
    try:
        validar_hora("08:15")
    except ValueError as error:
        print(error)

    print("Hora de fin 07:00 con inicio 08:00:")
    try:
        validar_hora("07:00", time(8, 0))
    except ValueError as error:
        print(error)
