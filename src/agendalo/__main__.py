import sys

from agendalo.clinica import Clinica
from agendalo.hu02 import datos_ejemplo as datos_hu02
from agendalo.hu02.pantalla import pantalla_registrar_medico

ERROR_OPCION_MENU = ">> Error: opción no válida. Elija un número del menú."

TEXTO_INICIO = """===== AGÉNDALO =====
1. Admisión
2. Médico
3. Administrador
0. Salir"""

TEXTO_MENU_ADMISION = """===== MENÚ ADMISIÓN =====
0. Volver al inicio"""

TEXTO_MENU_MEDICO = """===== MENÚ MÉDICO =====
0. Volver al inicio"""

TEXTO_MENU_ADMINISTRADOR = """===== MENÚ ADMINISTRADOR =====
2. Registrar médico
0. Volver al inicio"""

MENU_ADMISION = {}

MENU_MEDICO = {}

MENU_ADMINISTRADOR = {
    "2": pantalla_registrar_medico,
}


def mostrar_menu(texto_del_menu, menu, clinica):
    """Muestra el menú de un rol y abre la pantalla elegida, hasta que el usuario elija 0."""
    while True:
        print(texto_del_menu)
        opcion = input("Elija una opción: ").strip()

        if opcion == "0":
            return

        if opcion in menu:
            pantalla = menu[opcion]
            pantalla(clinica)
        else:
            print(ERROR_OPCION_MENU)


def cargar_datos_ejemplo(clinica):
    """Registra los datos de ejemplo de cada historia, en orden, sin mostrar nada en pantalla."""
    datos_hu02.cargar_datos_ejemplo(clinica)


def mostrar_pruebas(clinica):
    """Muestra la prueba automática de cada historia, en orden."""
    print("Prueba automática del sistema.")
    datos_hu02.mostrar_pruebas(clinica)


def principal():
    """Carga los datos de ejemplo y muestra la pantalla de inicio. Con --pruebas, solo muestra la prueba automática."""
    clinica = Clinica()
    cargar_datos_ejemplo(clinica)

    if "--pruebas" in sys.argv:
        mostrar_pruebas(clinica)
        return

    while True:
        print(TEXTO_INICIO)
        opcion = input("Elija su rol: ").strip()

        if opcion == "0":
            return
        elif opcion == "1":
            mostrar_menu(TEXTO_MENU_ADMISION, MENU_ADMISION, clinica)
        elif opcion == "2":
            mostrar_menu(TEXTO_MENU_MEDICO, MENU_MEDICO, clinica)
        elif opcion == "3":
            mostrar_menu(TEXTO_MENU_ADMINISTRADOR, MENU_ADMINISTRADOR, clinica)
        else:
            print(ERROR_OPCION_MENU)


if __name__ == "__main__":
    principal()






'''
ZONA DE PRUEBAS
Prueba automática del sistema.
===== HU02 REGISTRAR MÉDICO: DATOS DE EJEMPLO =====
Médicos de ejemplo registrados:
- Dr. Luis Fernández Soto — Cardiología (CMP 054321)
- Dr. Ana Ríos Paredes — Pediatría (CMP 061234)
----- Casos rechazados -----
CMP con 5 dígitos:
>> Error: el CMP debe tener 6 dígitos numéricos. Intente de nuevo.
CMP ya registrado:
>> Error: el CMP ya está registrado. Ingrese otro CMP.
Nombres vacíos:
>> Error: ingrese nombres y apellidos.
Especialidad 4:
>> Error: opción no válida. Elija un número de la lista.
Días con la letra D:
>> Error: ingrese al menos un día (L M X J V S).
Hora 08:15:
>> Error: la hora debe tener el formato HH:MM, en :00 o :30.
Hora de fin 07:00 con inicio 08:00:
>> Error: la hora de inicio debe ser menor que la hora de fin.
'''
