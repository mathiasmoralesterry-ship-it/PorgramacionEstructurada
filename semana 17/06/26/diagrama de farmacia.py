# DIAGRAMA DE FLUJO - FARMACIA DE LA CLÍNICA

print("=== FARMACIA DE LA CLÍNICA ===")

# INICIO
print("\nPaciente llega a farmacia")

# Entrega de receta
print("Paciente entrega receta médica")

# Verificación de receta
print("Farmacéutico verifica la receta")

# ¿Medicamento disponible?
disponible = input("¿Medicamento disponible? (SI/NO): ").upper()

if disponible == "SI":
    print("\nPreparando medicamentos...")

    medicamento = input("Nombre del medicamento: ")

    print(f"Medicamento entregado: {medicamento}")

else:
    print("\nMedicamento no disponible")

    opcion = input("¿Desea solicitar el medicamento? (SI/NO): ").upper()

    if opcion == "SI":
        print("Pedido registrado.")
        print("Se notificará al paciente cuando llegue.")
    else:
        print("Paciente rechaza la solicitud.")

# Ambos caminos continúan aquí
print("\nFarmacéutico explica la dosis y horario de uso")

print("Paciente recibe indicaciones")

# FIN
print("\n=== FIN DEL PROCESO ===")