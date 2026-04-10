# pylint: disable=all

import tkinter as tk

biblioteca = {}

def guardar_libro():
    titulo = entrada_titulo.get().strip().lower()
    autor = entrada_autor.get().strip()
    ubicacion = entrada_ubicacion.get().strip()
    
    if titulo and autor and ubicacion:
        biblioteca[titulo] = (autor, ubicacion)
        mensaje.set("Libro guardado.")
        limpiar_campos()
    else:
        mensaje.set("Faltan datos, revisa los campos.")

def limpiar_campos():
    entrada_titulo.delete(0, tk.END)
    entrada_autor.delete(0, tk.END)
    entrada_ubicacion.delete(0, tk.END)

def ver_detalles(titulo, autor, ubicacion):
    ventana_detalle = tk.Toplevel(app)
    ventana_detalle.title("Información del libro")
    ventana_detalle.geometry("380x220")
    ventana_detalle.config(bg="#0f172a")

    tk.Label(
        ventana_detalle,
        text="Información",
        font=("Arial", 15, "bold"),
        bg="#0f172a",
        fg="#38bdf8"
    ).pack(pady=12)

    tk.Label(
        ventana_detalle,
        text=f"Título: {titulo.title()}",
        bg="#0f172a",
        fg="white",
        font=("Arial", 11)
    ).pack(pady=4)

    tk.Label(
        ventana_detalle,
        text=f"Autor: {autor}",
        bg="#0f172a",
        fg="white",
        font=("Arial", 11)
    ).pack(pady=4)

    tk.Label(
        ventana_detalle,
        text=f"Ubicación: {ubicacion}",
        bg="#0f172a",
        fg="white",
        font=("Arial", 11)
    ).pack(pady=4)

    tk.Button(
        ventana_detalle,
        text="Cerrar",
        command=ventana_detalle.destroy,
        bg="#38bdf8",
        fg="black",
        relief="flat"
    ).pack(pady=15)

def buscar():
    titulo = entrada_busqueda.get().strip().lower()
    
    if titulo in biblioteca:
        autor, ubicacion = biblioteca[titulo]
        mensaje.set("Libro encontrado.")
        ver_detalles(titulo, autor, ubicacion)
    else:
        mensaje.set("No está en la biblioteca.")

app = tk.Tk()
app.title("Gestor de biblioteca")
app.geometry("500x450")
app.config(bg="#1e1e2f")

fuente_titulo = ("Arial", 15, "bold")
fuente_texto = ("Arial", 11)

bg = "#1e1e2f"
fg = "#ffffff"
input_bg = "#2c2c3e"

tk.Label(app, text="Agregar libro", font=fuente_titulo, bg=bg, fg=fg).pack(pady=10)

tk.Label(app, text="Título", bg=bg, fg=fg).pack()
entrada_titulo = tk.Entry(app, width=35, bg=input_bg, fg="white", insertbackground="white")
entrada_titulo.pack(pady=3, ipady=5)

tk.Label(app, text="Autor", bg=bg, fg=fg).pack()
entrada_autor = tk.Entry(app, width=35, bg=input_bg, fg="white", insertbackground="white")
entrada_autor.pack(pady=3, ipady=5)

tk.Label(app, text="Ubicación", bg=bg, fg=fg).pack()
entrada_ubicacion = tk.Entry(app, width=35, bg=input_bg, fg="white", insertbackground="white")
entrada_ubicacion.pack(pady=3, ipady=5)

tk.Button(
    app,
    text="Guardar",
    command=guardar_libro,
    bg="#4CAF50",
    fg="white"
).pack(pady=10)

tk.Label(app, text="------------------------", bg=bg, fg="#888").pack(pady=10)

tk.Label(app, text="Buscar libro", font=fuente_titulo, bg=bg, fg=fg).pack()

entrada_busqueda = tk.Entry(app, width=35, bg=input_bg, fg="white", insertbackground="white")
entrada_busqueda.pack(pady=8, ipady=5)

tk.Button(
    app,
    text="Buscar",
    command=buscar,
    bg="#2196F3",
    fg="white"
).pack(pady=5)

mensaje = tk.StringVar()
tk.Label(
    app,
    textvariable=mensaje,
    bg=bg,
    fg="#00ffcc",
    wraplength=400
).pack(pady=20)

app.mainloop()