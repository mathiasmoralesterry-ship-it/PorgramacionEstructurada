from datetime import datetime
#Pedimos la fecha de nacimiento
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (DD/MM/AAAA): ")
#Lo convertimos de texto a fecha
fecha_nac = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
#Fecha actual
hoy = datetime.today()
#Calcular edad
edad = hoy.year - fecha_nac.year
#Una verificacion de que si ya cumplio años, este año
if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
    edad -= 1
#Resultado
print(f"Tienes {edad} años.")