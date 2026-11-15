ERROR_CMP_REPETIDO = ">> Error: el CMP ya está registrado. Ingrese otro CMP."


class Clinica:
    """Guarda en memoria los médicos registrados."""

    def __init__(self):
        self.medicos = []

    def registrar_medico(self, medico):
        """Agrega el médico a la lista, si su CMP todavía está libre."""
        if self.buscar_medico(medico.cmp) is not None:
            raise ValueError(ERROR_CMP_REPETIDO)

        self.medicos.append(medico)

    def buscar_medico(self, cmp):
        """Devuelve el médico con ese CMP, o None si nadie lo tiene."""
        for medico in self.medicos:
            if medico.cmp == cmp:
                return medico

        return None
