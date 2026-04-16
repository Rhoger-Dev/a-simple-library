# pylint: disable=all

from model.libro import Libro
from repository.libro_repository import agregar_libro, obtener_libro, obtener_todos

def crear_libro(titulo, autor, ubicacion):
    if not (titulo and autor and ubicacion):
        raise ValueError("Todos los campos son obligatorios")

    libro = Libro(titulo, autor, ubicacion)
    agregar_libro(libro)
    return libro

def buscar_libro(titulo):
    if not titulo:
        return None
    return obtener_libro(titulo)

def listar_libros():
    return obtener_todos()