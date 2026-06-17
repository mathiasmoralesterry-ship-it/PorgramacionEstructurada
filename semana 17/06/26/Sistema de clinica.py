# DIAGRAMA DE FLUJO - SISTEMA DE CLÍNICA

print("=== SISTEMA DE CLÍNICA ===")

# INICIO
print("\nPaciente llega a la clínica")

# Entrega de datos en recepción
nombre = input("Ingrese nombre del paciente: ")
dni = input("Ingrese DNI: ")

print("\nDatos recibidos en recepción")

# ¿Paciente existe?
existe = input("¿El paciente existe en el sistema? (SI/NO): ").upper()

if existe == "SI":
    print("\nBuscando historial clínico del paciente...")
    print("Historial clínico encontrado.")
else:
    print("\nRegistrando nuevo paciente en el sistema...")
    print("Paciente registrado correctamente.")
    print("Historial clínico creado.")

# Verificar agenda médica
print("\nVerificando agenda médica...")

# ¿Hay disponibilidad de cita?
disponibilidad = input("¿Hay disponibilidad de cita? (SI/NO): ").upper()

if disponibilidad == "SI":
    fecha = input("Ingrese fecha de la cita: ")
    medico = input("Ingrese nombre del médico asignado: ")

    print(f"\nCita asignada para {fecha}")
    print(f"Médico asignado: {medico}")

    # Entrega comprobante
    print("Comprobante de cita entregado.")
else:
    print("\nNo hay disponibilidad en la fecha solicitada.")

    fecha_alternativa = input("Ofrecer otra fecha al paciente: ")
    print(f"Fecha ofrecida: {fecha_alternativa}")

    eleccion = input("¿El paciente acepta la fecha? (SI/NO): ").upper()

    if eleccion == "SI":
        print("Nueva cita programada.")
        print("Comprobante de cita entregado.")
    else:
        print("Paciente no aceptó la fecha propuesta.")
        print("Se registrará una nueva solicitud posteriormente.")

# Ambos caminos continúan aquí
print("\nPaciente espera su turno...")

# Atención médica
print("Médico atiende al paciente.")

# FIN
print("\n=== FIN DEL PROCESO ===")