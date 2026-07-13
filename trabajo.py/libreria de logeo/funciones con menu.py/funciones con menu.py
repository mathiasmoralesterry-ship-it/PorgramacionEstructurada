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

def abrir_sistema(ventana_bienvenida):

    # Cierra la ventana de bienvenida
    ventana_bienvenida.destroy()

    # Nueva ventana del sistema
    sistema = tk.Toplevel()
    sistema.title("Sistema Principal")
    sistema.geometry("900x600")
    sistema.config(bg="#d9d9d9")
    panel = tk.Frame(
    sistema,
    bg="#3c3f41",
    width=220
)

    panel.pack(side="left", fill="y")
    contenido = tk.Frame(
    sistema,
    bg="#d9d9d9"
)

    contenido.pack(side="right", expand=True, fill="both")
    marco = tk.Frame(
        contenido,
        bg="white",
        bd=2,
        relief="groove"
    )

    marco.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
        width=550,
        height=380
    )
    
    # -------------------------
    # Barra de Menú
    # -------------------------
    barra = tk.Menu(sistema)

    # Menú Usuario
    menu_usuario = tk.Menu(barra, tearoff=0)
    menu_usuario.add_command(label="Mi Perfil")
    menu_usuario.add_command(label="Cambiar Contraseña")
    menu_usuario.add_separator()
    menu_usuario.add_command(label="Cerrar Sesión", command=sistema.destroy)

    barra.add_cascade(label="Usuario", menu=menu_usuario)

    # Menú Configuración
    menu_config = tk.Menu(barra, tearoff=0)
    menu_config.add_command(label="Configuración General")
    menu_config.add_command(label="Tema")
    menu_config.add_command(label="Idioma")

    barra.add_cascade(label="Configuración", menu=menu_config)

    # Menú Reportes
    menu_reportes = tk.Menu(barra, tearoff=0)
    menu_reportes.add_command(label="Ver Reportes")
    menu_reportes.add_command(label="Exportar PDF")
    menu_reportes.add_command(label="Exportar Excel")

    barra.add_cascade(label="Reportes", menu=menu_reportes)

    # Menú Herramientas
    menu_herramientas = tk.Menu(barra, tearoff=0)
    menu_herramientas.add_command(label="Calculadora")
    menu_herramientas.add_command(label="Calendario")

    barra.add_cascade(label="Herramientas", menu=menu_herramientas)

    # Menú Ayuda
    menu_ayuda = tk.Menu(barra, tearoff=0)
    menu_ayuda.add_command(label="Manual")
    menu_ayuda.add_command(label="Acerca del Sistema")

    barra.add_cascade(label="Ayuda", menu=menu_ayuda)

    sistema.config(menu=barra)

    # -------------------------
    # Título
    # -------------------------
    titulo = tk.Label(
        sistema,
        text="SISTEMA PRINCIPAL",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="navy"
    )

    titulo.pack(pady=20)

    bienvenida = tk.Label(
        sistema,
        text="Bienvenido al sistema.\nSeleccione una opción del menú superior.",
        font=("Arial",14),
        bg="white"
    )

    bienvenida.pack(pady=20)
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
        
        tk.Button(
        ventana_bienvenida,
        text="Siguiente",
        font=("Arial", 12, "bold"),
        bg="blue",
        fg="white",
        command=lambda: abrir_sistema(ventana_bienvenida)
        ).pack(pady=15)

        # Actualizar token en ventana principal
        label_token.config(text=f"Token: {token}")

    else:
        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )

# ------------------------
# Funciones del menú
# ------------------------

def limpiar_campos():
    entry_usuario.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    label_token.config(text="Token: ")

def nuevo_token():
    token = generar_token()
    label_token.config(text=f"Token: {token}")
    messagebox.showinfo("Nuevo Token", f"Se generó un nuevo token:\n\n{token}")

def acerca_de():
    messagebox.showinfo(
        "Acerca del sistema",
        "Sistema de Login\n\n"
        "Versión: 1.0\n"
        "Desarrollado en Python con Tkinter."
    )

def salir():
    respuesta = messagebox.askyesno(
        "Salir",
        "¿Deseas salir del sistema?"
    )

    if respuesta:
        ventana.destroy()
# ------------------------
# Ventana principal
# ------------------------
ventana = tk.Tk()
ventana.title("Sistema de Login")
ventana.geometry("500x600")
ventana.config(bg="white")
# ------------------------
# Barra de menú
# ------------------------

barra_menu = tk.Menu(ventana)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Iniciar sesión", command=ingresar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Opciones
menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Limpiar campos", command=limpiar_campos)
menu_opciones.add_command(label="Generar nuevo token", command=nuevo_token)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menu)
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
