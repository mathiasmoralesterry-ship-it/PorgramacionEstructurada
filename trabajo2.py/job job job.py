import tkinter as tk
from tkinter import messagebox

# Crear ventana
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("500x800")

# Función para ingresar
def ingresar():
    usuario = entry_usuario.get()
    password = entry_password.get()

    if usuario == "admin" and password == "1234":
        messagebox.showinfo("Acceso", "Ingreso correcto")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Título
titulo = tk.Label(ventana, text="INICIAR SESIÓN", font=("Arial", 20))
titulo.pack(pady=40)

# Usuario
lbl_usuario = tk.Label(ventana, text="Usuario")
lbl_usuario.pack()

entry_usuario = tk.Entry(ventana, width=30)
entry_usuario.pack(pady=10)

# Contraseña
lbl_password = tk.Label(ventana, text="Contraseña")
lbl_password.pack()

entry_password = tk.Entry(ventana, width=30, show="*")
entry_password.pack(pady=10)

# Botón ingresar
btn_login = tk.Button(ventana, text="Ingresar", width=20, command=ingresar)
btn_login.pack(pady=30)

ventana.mainloop()
