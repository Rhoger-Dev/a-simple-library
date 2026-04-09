# pylint: disable=all

import tkinter as tk

catalogo = {}

def agregar_libro():
    nombre = entrada_nombre.get().lower()
    autor = entrada_autor.get()
    ubicacion = entrada_ubicacion.get()
    
    if nombre and autor and ubicacion:
        catalogo[nombre] = (autor, ubicacion)
        resultado.set("¡Libro agregado correctamente!")
    else:
        resultado.set("¡Completa todos los campos!")

def buscar_libro():
    libro = entrada_buscar.get().lower()
    
    if libro in catalogo:
        autor, ubicacion = catalogo[libro]
        resultado.set(f"Libro: {libro.title()} | Autor: {autor} | Ubicación: {ubicacion}")
    else:
        resultado.set("¡Libro no encontrado!")

ventana = tk.Tk()
ventana.title("Sistema de Biblioteca")
ventana.geometry("450x400")

tk.Label(ventana, text="Agregar libro", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(ventana, text="Nombre del libro").pack()
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack()

tk.Label(ventana, text="Autor").pack()
entrada_autor = tk.Entry(ventana, width=30)
entrada_autor.pack()

tk.Label(ventana, text="Ubicación").pack()
entrada_ubicacion = tk.Entry(ventana, width=30)
entrada_ubicacion.pack()

tk.Button(ventana, text="Agregar libro", command=agregar_libro).pack(pady=10)

tk.Label(ventana, text="-------------------------").pack(pady=10)

tk.Label(ventana, text="Buscar libro", font=("Arial", 14, "bold")).pack()

entrada_buscar = tk.Entry(ventana, width=30)
entrada_buscar.pack(pady=5)

tk.Button(ventana, text="Buscar", command=buscar_libro).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 11)).pack(pady=20)

ventana.mainloop()