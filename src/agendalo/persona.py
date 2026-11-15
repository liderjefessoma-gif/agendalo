from abc import ABC, abstractmethod


class Persona(ABC):
    """Una persona de la clínica, con sus nombres y apellidos."""

    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos

    def nombre_completo(self):
        """Devuelve los nombres y los apellidos juntos."""
        return f"{self.nombres} {self.apellidos}"

    @abstractmethod
    def describir(self):
        """Devuelve el texto con el que el programa presenta a la persona."""
