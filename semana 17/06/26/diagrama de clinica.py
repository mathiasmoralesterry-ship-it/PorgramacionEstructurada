#Clinica 

print("=== SISTEMA DE ATENCIÓN DE CLÍNICA ===")

# INICIO
print("\nUsuario llega a la clínica")

# Recepcionista solicita datos
print("Recepcionista solicita datos")

# Ingresar datos personales
nombre = input("Ingrese nombre del paciente: ")
edad = input("Ingrese edad: ")
dni = input("Ingrese DNI: ")

# Registrar datos
print("\nDatos registrados correctamente")

# Usuario pasa a ser paciente
print(f"{nombre} ahora es paciente de la clínica")

# Doctor recibe paciente
print("\nDoctor recibe al paciente")

# Evolución y diagnóstico
diagnostico = input("Ingrese diagnóstico del paciente: ")

# ¿Necesita tratamiento?
tratamiento = input("¿Necesita tratamiento? (SI/NO): ").upper()

if tratamiento == "SI":
    print("\n--- TRATAMIENTO ---")
    indicacion = input("Indique el tratamiento: ")
    print(f"Tratamiento asignado: {indicacion}")
else:
    print("\nPaciente dado de alta")

# FIN
print("\nFin del proceso")