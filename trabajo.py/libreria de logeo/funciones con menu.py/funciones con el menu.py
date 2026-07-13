import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
from datetime import datetime

# ==========================
# COLORES
# ==========================
COLOR_FONDO = "#d9d9d9"
COLOR_PANEL = "#2f3542"
COLOR_BOTON = "#1e90ff"
COLOR_HOVER = "#3742fa"
COLOR_TEXTO = "white"

usuario_actual = ""
token_actual = ""

# ==========================
# GENERAR TOKEN
# ==========================
def generar_token():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(12))

# ==========================
# LOGIN
# ==========================
def autentificar(usuario, password):
    return usuario == "admin" and password == "1234"

# ==========================
# EFECTO HOVER
# ==========================
def entrar(event):
    event.widget.config(bg=COLOR_HOVER)

def salir(event):
    event.widget.config(bg=COLOR_BOTON)

# ==========================
# CAMBIAR CONTENIDO
# ==========================
def mostrar_pantalla(titulo, descripcion):

    for widget in contenido.winfo_children():
        widget.destroy()

    cuadro = tk.Frame(
        contenido,
        bg="white",
        bd=2,
        relief="groove"
    )

    cuadro.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
        width=650,
        height=420
    )

    tk.Label(
        cuadro,
        text=titulo,
        font=("Arial",22,"bold"),
        bg="white",
        fg="#2f3542"
    ).pack(pady=20)

    tk.Label(
        cuadro,
        text=descripcion,
        font=("Arial",14),
        bg="white",
        justify="left"
    ).pack(pady=10)

# ==========================
# OPCIONES
# ==========================
def inicio():
    mostrar_pantalla(
        "🏠 INICIO",
        f"""Bienvenido {usuario_actual}

Has iniciado sesión correctamente.

Token:
{token_actual}

Seleccione una opción del menú lateral."""
    )

def usuarios():
    mostrar_pantalla(
        "👤 USUARIOS",
        """Aquí podrás:

• Registrar usuarios

• Modificar usuarios

• Eliminar usuarios

• Buscar usuarios"""
    )

def configuracion():
    mostrar_pantalla(
        "⚙ CONFIGURACIÓN",
        """Opciones disponibles:

• Cambiar contraseña

• Cambiar tema

• Configuración general

• Idioma"""
    )

def reportes():
    mostrar_pantalla(
        "📊 REPORTES",
        """Aquí podrás generar:

• Reporte PDF

• Reporte Excel

• Historial

• Estadísticas"""
    )

def ayuda():
    mostrar_pantalla(
        "❓ AYUDA",
        """Sistema desarrollado en Python.

Versión 1.0

Proyecto Tkinter."""
    )

# ==========================
# SISTEMA PRINCIPAL
# ==========================
def abrir_sistema(ventana_bienvenida):

    global contenido

    ventana_bienvenida.destroy()

    sistema = tk.Toplevel()

    sistema.title("Sistema Principal")

    sistema.geometry("1100x650")

    sistema.config(bg=COLOR_FONDO)

    sistema.state("zoomed")

    # ==================
    # MENÚ SUPERIOR
    # ==================

    barra = tk.Menu(sistema)

    archivo = tk.Menu(barra, tearoff=0)

    archivo.add_command(label="Inicio", command=inicio)

    archivo.add_separator()

    archivo.add_command(
        label="Salir",
        command=sistema.destroy
    )

    barra.add_cascade(
        label="Archivo",
        menu=archivo
    )

    ayuda_menu = tk.Menu(barra, tearoff=0)

    ayuda_menu.add_command(
        label="Acerca del sistema",
        command=ayuda
    )

    barra.add_cascade(
        label="Ayuda",
        menu=ayuda_menu
    )

    sistema.config(menu=barra)

    # ==================
    # PANEL IZQUIERDO
    # ==================

    panel = tk.Frame(
        sistema,
        bg=COLOR_PANEL,
        width=220
    )

    panel.pack(
        side="left",
        fill="y"
    )

    # ==================
    # CONTENIDO
    # ==================

    contenido = tk.Frame(
        sistema,
        bg=COLOR_FONDO
    )

    contenido.pack(
        side="right",
        expand=True,
        fill="both"
    )
        # ==================
    # LOGO / TITULO
    # ==================

    tk.Label(
        panel,
        text="🐾 VETERINARIA",
        bg=COLOR_PANEL,
        fg="white",
        font=("Arial",18,"bold")
    ).pack(pady=20)

    # ==================
    # BOTONES DEL MENÚ
    # ==================

    botones = [

        ("🏠 Inicio", inicio),

        ("👤 Usuarios", usuarios),

        ("🐶 Mascotas", lambda: mostrar_pantalla(
            "🐶 MASCOTAS",
            """Aquí podrás:

• Registrar mascotas

• Buscar mascotas

• Modificar información

• Historial médico"""
        )),

        ("📅 Citas", lambda: mostrar_pantalla(
            "📅 CITAS",
            """Administración de citas.

• Registrar cita

• Editar cita

• Cancelar cita

• Consultar agenda"""
        )),

        ("🩺 Consultas", lambda: mostrar_pantalla(
            "🩺 CONSULTAS",
            """Consultas veterinarias.

• Nueva consulta

• Diagnóstico

• Tratamiento

• Recetas"""
        )),

        ("💉 Vacunas", lambda: mostrar_pantalla(
            "💉 VACUNAS",
            """Control de vacunas.

• Registrar vacuna

• Historial

• Próximas vacunas"""
        )),

        ("💊 Medicamentos", lambda: mostrar_pantalla(
            "💊 MEDICAMENTOS",
            """Inventario de medicamentos.

• Agregar

• Editar

• Stock

• Vencimientos"""
        )),

        ("📦 Inventario", lambda: mostrar_pantalla(
            "📦 INVENTARIO",
            """Control del inventario.

• Productos

• Entradas

• Salidas

• Stock"""
        )),

        ("📊 Reportes", reportes),

        ("⚙ Configuración", configuracion),

        ("❓ Ayuda", ayuda)

    ]

    for texto, comando in botones:

        boton = tk.Button(
            panel,
            text=texto,
            command=comando,
            bg=COLOR_BOTON,
            fg="white",
            activebackground=COLOR_HOVER,
            activeforeground="white",
            relief="flat",
            font=("Arial",11,"bold"),
            cursor="hand2",
            width=20,
            pady=8
        )

        boton.pack(pady=6)

        boton.bind("<Enter>", entrar)
        boton.bind("<Leave>", salir)

    # ==================
    # INFORMACIÓN INFERIOR
    # ==================

    tk.Label(
        panel,
        text=f"Usuario:\n{usuario_actual}",
        bg=COLOR_PANEL,
        fg="white",
        font=("Arial",10)
    ).pack(side="bottom", pady=20)

    # ==================
    # PANTALLA INICIAL
    # ==================

    inicio()