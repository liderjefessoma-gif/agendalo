from agendalo.cita import RESERVADA
from agendalo.clinica import ERROR_CANCELAR_NO_RESERVADA, ERROR_CITA_NO_ENCONTRADA
from agendalo.validaciones import validar_confirmacion


def pantalla_cancelar_cita(clinica):
    """Pide el código de una cita reservada y la cancela si el usuario confirma."""
    print("===== CANCELAR CITA =====")

    while True:
        codigo = input("Código de cita (0 para volver): ").strip().upper()
        if codigo == "0":
            return
        cita = clinica.buscar_cita(codigo)
        if cita is None:
            print(ERROR_CITA_NO_ENCONTRADA)
        elif cita.estado != RESERVADA:
            print(ERROR_CANCELAR_NO_RESERVADA)
        else:
            break

    print(f">> Cita: {cita.describir()}")
    print(f"   Paciente: {cita.paciente.nombre_completo()}")

    while True:
        try:
            confirma = validar_confirmacion(input("¿Seguro que desea cancelar esta cita? (S/N): "))
            break
        except ValueError as error:
            print(error)

    if confirma:
        clinica.cancelar_cita(cita)
        print(f">> Cita {cita.codigo} cancelada. El horario quedó libre.")
    else:
        print(">> La cita no se canceló.")

    input("Presione Enter para volver al menú.")
