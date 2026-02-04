import tkinter as tk
import webbrowser
from api import obtener_url_logo

def buscar_logo():
    nombre = entry.get()
    if not nombre:
        return

    url = obtener_url_logo(nombre)
    webbrowser.open(url)

root = tk.Tk()
root.title("Buscador de Logos")
root.geometry("320x160")

tk.Label(root, text="Nombre del logo:").pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Ver logo", command=buscar_logo).pack(pady=15)

root.mainloop()