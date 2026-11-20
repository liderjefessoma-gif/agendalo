import sys

from agendalo.clinica import Clinica
from agendalo.hu02 import datos_ejemplo as datos_hu02
from agendalo.hu02.pantalla import pantalla_registrar_medico
from agendalo.hu03 import datos_ejemplo as datos_hu03
from agendalo.hu03.pantalla import pantalla_reservar_cita
from agendalo.hu04 import datos_ejemplo as datos_hu04
from agendalo.hu04.pantalla import pantalla_reprogramar_cita
from agendalo.hu05 import datos_ejemplo as datos_hu05
from agendalo.hu05.pantalla import pantalla_cancelar_cita

ERROR_OPCION_MENU = ">> Error: opción no válida. Elija un número del menú."

TEXTO_INICIO = """===== AGÉNDALO =====
1. Admisión
2. Médico
3. Administrador
0. Salir"""

TEXTO_MENU_ADMISION = """===== MENÚ ADMISIÓN =====
3. Reservar cita
4. Reprogramar cita
5. Cancelar cita
0. Volver al inicio"""

TEXTO_MENU_MEDICO = """===== MENÚ MÉDICO =====
0. Volver al inicio"""

TEXTO_MENU_ADMINISTRADOR = """===== MENÚ ADMINISTRADOR =====
2. Registrar médico
0. Volver al inicio"""

MENU_ADMISION = {
    "3": pantalla_reservar_cita,
    "4": pantalla_reprogramar_cita,
    "5": pantalla_cancelar_cita,
}

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
    datos_hu03.cargar_datos_ejemplo(clinica)
    datos_hu04.cargar_datos_ejemplo(clinica)
    datos_hu05.cargar_datos_ejemplo(clinica)


def mostrar_pruebas(clinica):
    """Muestra la prueba automática de cada historia, en orden."""
    print("Prueba automática del sistema.")
    datos_hu02.mostrar_pruebas(clinica)
    datos_hu03.mostrar_pruebas(clinica)
    datos_hu04.mostrar_pruebas(clinica)
    datos_hu05.mostrar_pruebas(clinica)


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
- Dr. Carmen Ruiz Paz — Medicina general (CMP 072345)
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
===== HU03 RESERVAR CITA: DATOS DE EJEMPLO =====
Pacientes de ejemplo registrados:
- Ana María Quispe Rojas (DNI 45678912)
- Jorge Salas Medina (DNI 41234567)
Citas de ejemplo:
- C0001: 24/11/2026 09:00 — Dr. Luis Fernández Soto — Ana María Quispe Rojas (Reservada)
- C0002: 24/11/2026 10:00 — Dr. Luis Fernández Soto — Jorge Salas Medina (Reservada)
- C0003: 24/11/2026 14:00 — Dr. Ana Ríos Paredes — Jorge Salas Medina (Cancelada)
- C0004: 24/11/2026 15:00 — Dr. Ana Ríos Paredes — Ana María Quispe Rojas (Reservada)
----- Reserva válida -----
>> Cita reservada. Código: C0005
   24/11/2026 16:00 — Dr. Carmen Ruiz Paz
----- Casos rechazados -----
DNI con 4 dígitos:
>> Error: el DNI debe tener 8 dígitos numéricos. Intente de nuevo.
DNI no registrado (99999999):
>> Error: paciente no encontrado. Verifique el DNI.
Fecha 2026-11-25:
>> Error: la fecha debe tener el formato DD/MM/AAAA.
Fecha 01/01/2020:
>> Error: la fecha ya pasó.
Dr. Luis un sábado:
>> Error: el médico no atiende ese día.
Dr. Luis a las 15:00:
>> Error: la hora está fuera del horario del médico (08:00 a 13:00).
Dr. Luis a las 09:00, ya ocupado por C0001:
>> Error: horario ocupado. Elija uno de los horarios libres.
Ana María con la Dra. Carmen a las 15:00, pero ya tiene C0004 a esa hora:
>> Error: el paciente ya tiene una cita a esa hora.
===== HU04 REPROGRAMAR CITA: DATOS DE EJEMPLO =====
----- Reprogramación válida -----
C0002 de 24/11/2026 10:00 a 24/11/2026 11:00:
>> Cita C0002 reprogramada.
----- Casos rechazados -----
Código C9999:
>> Error: cita no encontrada.
C0003, que está Cancelada:
>> Error: solo se reprograman citas en estado "Reservada".
C0001 a las 11:00, ya ocupado por C0002:
>> Error: horario ocupado. Elija uno de los horarios libres.
Citas después de reprogramar:
- C0001: 24/11/2026 09:00 — Dr. Luis Fernández Soto — Ana María Quispe Rojas (Reservada)
- C0002: 24/11/2026 11:00 — Dr. Luis Fernández Soto — Jorge Salas Medina (Reservada)
- C0003: 24/11/2026 14:00 — Dr. Ana Ríos Paredes — Jorge Salas Medina (Cancelada)
- C0004: 24/11/2026 15:00 — Dr. Ana Ríos Paredes — Ana María Quispe Rojas (Reservada)
- C0005: 24/11/2026 16:00 — Dr. Carmen Ruiz Paz — Jorge Salas Medina (Reservada)
===== HU05 CANCELAR CITA: DATOS DE EJEMPLO =====
----- Cancelación válida -----
>> Cita C0001 cancelada. El horario quedó libre.
El horario de C0001 se puede reservar otra vez:
>> Cita reservada. Código: C0006
   24/11/2026 09:00 — Dr. Luis Fernández Soto
----- Casos rechazados -----
Código C9999:
>> Error: cita no encontrada.
C0001 otra vez, que ya está Cancelada:
>> Error: solo se cancelan citas en estado "Reservada".
Citas después de cancelar:
- C0001: 24/11/2026 09:00 — Dr. Luis Fernández Soto — Ana María Quispe Rojas (Cancelada)
- C0002: 24/11/2026 11:00 — Dr. Luis Fernández Soto — Jorge Salas Medina (Reservada)
- C0003: 24/11/2026 14:00 — Dr. Ana Ríos Paredes — Jorge Salas Medina (Cancelada)
- C0004: 24/11/2026 15:00 — Dr. Ana Ríos Paredes — Ana María Quispe Rojas (Reservada)
- C0005: 24/11/2026 16:00 — Dr. Carmen Ruiz Paz — Jorge Salas Medina (Reservada)
- C0006: 24/11/2026 09:00 — Dr. Luis Fernández Soto — Jorge Salas Medina (Reservada)
'''
