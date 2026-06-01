# Función para autentificar al usuario
def autentificar(usuario, password):
    if usuario == "admin" and password == "1234":
        return True
    return False


# Función para generar un token
def tokenizar(usuario):
    token = f"TOKEN(ingreso correcto papu:V)"
    return token


# Función para mostrar alertas
def alertar(mensaje):
    print(f"[ALERTA] {mensaje}")


# Función para redirigir
def redirigir(destino):
    print(f"Redirigiendo a: {destino}")


# Programa principal
usuario = input("Ingrese usuario: ")
password = input("Ingrese contraseña: ")

if autentificar(usuario, password):
    print("Acceso concedido")

    token = tokenizar(usuario)
    print("Token generado:", token)

    redirigir("Panel Principal")

else:
    alertar("Usuario o contraseña incorrectos")