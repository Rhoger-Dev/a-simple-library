# pylint: disable=all

biblioteca = {}

def agregar_libro(libro):
    biblioteca[libro.titulo.lower()] = libro

def obtener_libro(titulo):
    return biblioteca.get(titulo.lower())

def obtener_todos():
    return list(biblioteca.values())