from datetime import datetime

from agendalo.medico import DIAS, ESPECIALIDADES

DIGITOS = "0123456789"


def validar_cmp(texto):
    """Revisa que el CMP tenga 6 dígitos y lo devuelve como texto."""
    mensaje = ">> Error: el CMP debe tener 6 dígitos numéricos. Intente de nuevo."
    cmp = texto.strip()

    if len(cmp) != 6:
        raise ValueError(mensaje)

    for caracter in cmp:
        if caracter not in DIGITOS:
            raise ValueError(mensaje)

    return cmp


def validar_nombre(texto):
    """Revisa que el nombre o apellido tenga texto y lo devuelve sin espacios sobrantes."""
    nombre = texto.strip()

    if nombre == "":
        raise ValueError(">> Error: ingrese nombres y apellidos.")

    return nombre


def validar_especialidad(texto):
    """Recibe el número elegido (1, 2 o 3) y devuelve el nombre de la especialidad."""
    opcion = texto.strip()

    if opcion not in ESPECIALIDADES:
        raise ValueError(">> Error: opción no válida. Elija un número de la lista.")

    return ESPECIALIDADES[opcion]


def validar_dias(texto):
    """Revisa los días de atención y los devuelve en el orden L M X J V S."""
    mensaje = ">> Error: ingrese al menos un día (L M X J V S)."
    letras_ingresadas = texto.upper().split()

    if len(letras_ingresadas) == 0:
        raise ValueError(mensaje)

    dias_elegidos = []
    for letra in letras_ingresadas:
        if letra not in DIAS:
            raise ValueError(mensaje)
        if letra in dias_elegidos:
            raise ValueError(mensaje)
        dias_elegidos.append(letra)

    dias_en_orden = []
    for dia in DIAS:
        if dia in dias_elegidos:
            dias_en_orden.append(dia)

    return dias_en_orden


def validar_hora(texto, inicio=None):
    """Revisa una hora HH:MM en :00 o :30. Si recibe la hora de inicio, revisa que esta hora sea mayor."""
    mensaje_formato = ">> Error: la hora debe tener el formato HH:MM, en :00 o :30."

    try:
        hora = datetime.strptime(texto.strip(), "%H:%M").time()
    except ValueError:
        raise ValueError(mensaje_formato)

    if hora.minute != 0 and hora.minute != 30:
        raise ValueError(mensaje_formato)

    if inicio is not None and hora <= inicio:
        raise ValueError(">> Error: la hora de inicio debe ser menor que la hora de fin.")

    return hora


def validar_dni(texto):
    """Revisa que el DNI tenga 8 dígitos y lo devuelve como texto."""
    mensaje = ">> Error: el DNI debe tener 8 dígitos numéricos. Intente de nuevo."
    dni = texto.strip()

    if len(dni) != 8:
        raise ValueError(mensaje)

    for caracter in dni:
        if caracter not in DIGITOS:
            raise ValueError(mensaje)

    return dni


def validar_fecha(texto):
    """Revisa una fecha DD/MM/AAAA y la devuelve como fecha."""
    try:
        fecha = datetime.strptime(texto.strip(), "%d/%m/%Y").date()
    except ValueError:
        raise ValueError(">> Error: la fecha debe tener el formato DD/MM/AAAA.")

    return fecha


def validar_confirmacion(texto):
    """Recibe S o N y devuelve True si es S o False si es N."""
    respuesta = texto.strip().upper()

    if respuesta == "S":
        return True
    if respuesta == "N":
        return False

    raise ValueError(">> Error: responda S o N.")
