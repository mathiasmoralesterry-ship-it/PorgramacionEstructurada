import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
from datetime import datetime

# ------------------------
# Función de autenticación
# ------------------------
def autentificar(usuario, password):
    return usuario == "admin" and password == "1234"

# ------------------------
# Función para generar token
# ------------------------
def generar_token():
    caracteres = string.ascii_letters + string.digits
    token = ''.join(random.choice(caracteres) for _ in range(12))
    return token

# ------------------------
# Función para ingresar
# ------------------------
def ingresar():
    usuario = entry_usuario.get()
    password = entry_password.get()

    if autentificar(usuario, password):

        token = generar_token()
        hora_ingreso = datetime.now().strftime("%H:%M:%S")

        # Nueva ventana de bienvenida
        ventana_bienvenida = tk.Toplevel()
        ventana_bienvenida.title("Bienvenido")
        ventana_bienvenida.geometry("400x300")
        ventana_bienvenida.config(bg="white")

        # Mensaje de bienvenida
        tk.Label(
            ventana_bienvenida,
            text=f"¡Bienvenido {usuario}!",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="green"
        ).pack(pady=20)

        # Hora
        tk.Label(
            ventana_bienvenida,
            text=f"Hora de ingreso: {hora_ingreso}",
            font=("Arial", 12),
            bg="white"
        ).pack(pady=10)

        # Token
        tk.Label(
            ventana_bienvenida,
            text=f"Token:\n{token}",
            font=("Arial", 12),
            bg="white"
        ).pack(pady=10)
        # Imagen de bienvenida
        imagen_bienvenida = Image.open("bienvenido.jpg")
        imagen_bienvenida = imagen_bienvenida.resize((120, 120))
        foto_bienvenida = ImageTk.PhotoImage(imagen_bienvenida)

        label_bienvenida = tk.Label(
        ventana_bienvenida,
        image=foto_bienvenida,
        bg="white"
        )
        label_bienvenida.image = foto_bienvenida
        label_bienvenida.pack(pady=10)

        # Actualizar token en ventana principal
        label_token.config(text=f"Token: {token}")

    else:
        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )


# ------------------------
# Ventana principal
# ------------------------
ventana = tk.Tk()
ventana.title("Sistema de Login")
ventana.geometry("500x600")
ventana.config(bg="white")

# ------------------------
# Imagen
# ------------------------
# Cambia "logo.png" por el nombre de tu imagen
imagen = Image.open("images.png")
imagen = imagen.resize((150, 150))
foto = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(ventana, image=foto, bg="white")
label_imagen.pack(pady=10)

# ------------------------
# Título
# ------------------------
titulo = tk.Label(
    ventana,
    text="INICIO DE SESIÓN",
    font=("Arial", 18, "bold"),
    bg="white"
)
titulo.pack(pady=10)

# ------------------------
# Usuario
# ------------------------
tk.Label(
    ventana,
    text="Usuario:",
    font=("Arial", 12),
    bg="white"
).pack()

entry_usuario = tk.Entry(
    ventana,
    font=("Arial", 12),
    width=25
)
entry_usuario.pack(pady=5)

# ------------------------
# Contraseña
# ------------------------
tk.Label(
    ventana,
    text="Contraseña:",
    font=("Arial", 12),
    bg="white"
).pack()

entry_password = tk.Entry(
    ventana,
    show="*",
    font=("Arial", 12),
    width=25
)
entry_password.pack(pady=5)

# ------------------------
# Botón ingresar
# ------------------------
btn_ingresar = tk.Button(
    ventana,
    text="Ingresar",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=ingresar
)
btn_ingresar.pack(pady=20)

# ------------------------
# Mostrar token
# ------------------------
label_token = tk.Label(
    ventana,
    text="Token: ",
    font=("Arial", 10),
    bg="white"
)
label_token.pack(pady=10)

ventana.mainloop()
