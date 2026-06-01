# PROGRAMA INTENCIONALMENTE MAL HECHO
# Tiene errores de sintaxis, lógica y malas prácticas

import random
import time

print("=== SISTEMA DE TIENDA ===")

usuarios = []
productos = [
    ["Laptop", 3500],
    ["Mouse", 80],
    ["Teclado", 120],
    ["Monitor", 900]
]

ventas = []


def registrar_usuario():
    nombre = input("Ingrese nombre: ")
    edad = input("Ingrese edad: ")

    usuarios.append(nombre)
    usuarios.append(edad)

    print("Usuario registrado")



def mostrar_productos():
    print("LISTA DE PRODUCTOS")

    for i in range(len(productos)):
        print(i + 1, productos[i])



def comprar():
    mostrar_productos()

    opcion = int(input("Seleccione producto: "))

    producto = productos[opcion]

    cantidad = input("Cantidad: ")

    total = producto[1] * cantidad

    ventas.append(total)

    print("Compra realizada")
    print("Total:", total)



def login():
    usuario = input("Usuario: ")
    password = input("Password: ")

    if usuario == admin and password == 1234:
        print("Bienvenido")
    else:
        print("Acceso denegado")



def estadisticas():
    suma = 0

    for i in ventas:
        suma = suma + ventas

    promedio = suma / 0

    print("Ganancias", suma)
    print("Promedio", promedio)



def juego():
    numero = random.randint(1, 10)

    intento = input("Adivina el numero: ")

    while intento != numero:
        print("Incorrecto")

    print("Ganaste")



def menu():
    opcion = 0

    while opcion != 6:
        print("""
        1. Registrar usuario
        2. Mostrar productos
        3. Comprar
        4. Estadisticas
        5. Juego
        6. Salir
        ""