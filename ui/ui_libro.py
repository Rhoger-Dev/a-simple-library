# pylint: disable=all

import tkinter as tk
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.libro_service import crear_libro, buscar_libro, listar_libros


BG = "#0f172a"          # Fondo principal
CARD = "#1e293b"        
PRIMARY = "#38bdf8"     
TEXT = "#e2e8f0"        
ACCENT = "#22c55e"      


FONT = ("Segoe UI", 10)
FONT_TITLE = ("Segoe UI", 16, "bold")


def guardar_libro():
    try:
        libro = crear_libro(
            entrada_titulo.get().strip(),
            entrada_autor.get().strip(),
            entrada_ubicacion.get().strip()
        )
        mensaje.set("✔ Libro guardado: " + libro.titulo)
        limpiar_campos()
        actualizar_lista()
    except ValueError as e:
        mensaje.set(str(e))


def buscar():
    titulo = entrada_busqueda.get().strip()
    libro = buscar_libro(titulo)
    if libro:
        mensaje.set("✔ Libro encontrado")
        ver_detalles(libro)
    else:
        mensaje.set("✖ No está en la biblioteca")


def ver_detalles(libro):
    ventana = tk.Toplevel(app)
    ventana.title("Detalles")
    ventana.geometry("300x200")
    ventana.config(bg=BG)

    tk.Label(ventana, text="Detalles del libro", font=FONT_TITLE, bg=BG, fg=PRIMARY).pack(pady=10)
    tk.Label(ventana, text=f"Título: {libro.titulo}", bg=BG, fg=TEXT, font=FONT).pack(pady=5)
    tk.Label(ventana, text=f"Autor: {libro.autor}", bg=BG, fg=TEXT, font=FONT).pack(pady=5)
    tk.Label(ventana, text=f"Ubicación: {libro.ubicacion}", bg=BG, fg=TEXT, font=FONT).pack(pady=5)


def limpiar_campos():
    entrada_titulo.delete(0, tk.END)
    entrada_autor.delete(0, tk.END)
    entrada_ubicacion.delete(0, tk.END)


def actualizar_lista():
    lista_libros.delete(0, tk.END)
    for libro in listar_libros():
        lista_libros.insert(tk.END, libro.titulo)


app = tk.Tk()
app.title("Gestor de Libros")
app.geometry("420x520")
app.config(bg=BG)


frame = tk.Frame(app, bg=CARD, padx=15, pady=15)
frame.pack(padx=15, pady=15, fill="both", expand=True)


tk.Label(frame, text="📚Gestor de Libros", font=FONT_TITLE, bg=CARD, fg=PRIMARY).pack(pady=10)


tk.Label(frame, text="Título", bg=CARD, fg=TEXT, font=FONT).pack(anchor="w")
entrada_titulo = tk.Entry(frame, bg="#334155", fg=TEXT, insertbackground=TEXT, relief="flat")
entrada_titulo.pack(fill="x", pady=5)

tk.Label(frame, text="Autor", bg=CARD, fg=TEXT, font=FONT).pack(anchor="w")
entrada_autor = tk.Entry(frame, bg="#334155", fg=TEXT, insertbackground=TEXT, relief="flat")
entrada_autor.pack(fill="x", pady=5)

tk.Label(frame, text="Ubicación", bg=CARD, fg=TEXT, font=FONT).pack(anchor="w")
entrada_ubicacion = tk.Entry(frame, bg="#334155", fg=TEXT, insertbackground=TEXT, relief="flat")
entrada_ubicacion.pack(fill="x", pady=5)


tk.Button(
    frame,
    text="Guardar libro",
    command=guardar_libro,
    bg=PRIMARY,
    fg="black",
    relief="flat",
    padx=10,
    pady=5
).pack(pady=10)


tk.Label(frame, text="Buscar libro", bg=CARD, fg=TEXT, font=FONT).pack(anchor="w")

entrada_busqueda = tk.Entry(frame, bg="#334155", fg=TEXT, insertbackground=TEXT, relief="flat")
entrada_busqueda.pack(fill="x", pady=5)

tk.Button(
    frame,
    text="Buscar",
    command=buscar,
    bg="#64748b",
    fg="white",
    relief="flat"
).pack(pady=5)


tk.Label(frame, text="Libros", bg=CARD, fg=TEXT, font=FONT).pack(anchor="w")

lista_libros = tk.Listbox(
    frame,
    bg="#020617",
    fg=TEXT,
    selectbackground=PRIMARY,
    relief="flat"
)
lista_libros.pack(fill="both", expand=True, pady=10)


mensaje = tk.StringVar()
tk.Label(frame, textvariable=mensaje, bg=CARD, fg=ACCENT, font=FONT).pack(pady=5)


actualizar_lista()

icono = tk.PhotoImage(file="icon2.png")
app.iconphoto(True, icono)