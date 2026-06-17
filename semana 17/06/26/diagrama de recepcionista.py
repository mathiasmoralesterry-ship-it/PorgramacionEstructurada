# DIAGRAMA DE FLUJO - RECEPCIONISTA DE CLÍNICA

print("=== SISTEMA DE GESTIÓN DE CITAS ===")

# INICIO
print("\nPaciente solicita una cita")

# Recepcionista registra datos
nombre = input("Ingrese nombre del paciente: ")
dni = input("Ingrese DNI: ")

print("\nRecepcionista registra los datos")

# ¿Paciente existe?
existe = input("¿El paciente ya existe en el sistema? (SI/NO): ").upper()

if existe == "SI":
    print("\nBuscando historial clínico...")
    print("Historial clínico encontrado.")
else:
    print("\nCreando historial clínico...")
    print("Historial clínico creado correctamente.")

# Consultar horarios
print("\nConsultando horarios disponibles...")

# ¿Hay disponibilidad?
disponibilidad = input("¿Hay disponibilidad? (SI/NO): ").upper()

if disponibilidad == "SI":
    fecha = input("Ingrese la fecha asignada para la cita: ")
    print(f"\nCita programada para: {fecha}")
else:
    nueva_fecha = input("No hay disponibilidad. Ofrecer otra fecha: ")
    print(f"\nNueva fecha propuesta: {nueva_fecha}")

# Entregar comprobante de cita
print("\nEntregando comprobante de cita al paciente...")

# Paciente llega a cita
print("Paciente llega a la cita médica.")

# FIN
print("\n=== FIN DEL PROCESO ===")