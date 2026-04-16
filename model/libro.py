# pylint: disable=all

from uuid import uuid4

class Libro:
    def __init__(self, titulo, autor, ubicacion):
        self.id = str(uuid4())
        self.titulo = titulo
        self.autor = autor
        self.ubicacion = ubicacion

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Ubicación: {self.ubicacion})"