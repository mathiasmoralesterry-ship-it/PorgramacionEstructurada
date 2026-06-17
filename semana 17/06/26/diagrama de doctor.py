# DIAGRAMA DE FLUJO - DOCTOR DE LA CLÍNICA

print("=== ATENCIÓN MÉDICA ===")

# INICIO
print("\nPaciente llega con cita")

# Doctor llama al paciente
print("Doctor llama al paciente")

# Verificar datos
nombre = input("Ingrese nombre del paciente: ")
dni = input("Ingrese DNI del paciente: ")

print("\nDatos verificados correctamente")

# Consulta y evaluación
print("\nDoctor realiza consulta y evaluación")

diagnostico = input("Ingrese diagnóstico preliminar: ")

# ¿Requiere exámenes o estudios?
requiere_examenes = input("¿Requiere exámenes o estudios? (SI/NO): ").upper()

if requiere_examenes == "SI":
    print("\nSolicitando exámenes o estudios...")
    
    examen = input("Tipo de examen solicitado: ")
    
    print(f"Examen solicitado: {examen}")
    print("Paciente realiza los exámenes.")
else:
    print("\nIndicando tratamiento o medicación...")
    
    tratamiento = input("Ingrese tratamiento o medicación: ")
    
    print(f"Tratamiento indicado: {tratamiento}")

# Ambos caminos continúan aquí
print("\nExplicando diagnóstico y tratamiento al paciente...")

# Resolver dudas
print("Resolviendo dudas del paciente...")

# Registrar atención
print("Registrando la atención en el sistema...")

# Entrega de indicaciones o receta
print("Entregando indicaciones y/o receta médica...")

# FIN
print("\n=== FIN DEL PROCESO ===")