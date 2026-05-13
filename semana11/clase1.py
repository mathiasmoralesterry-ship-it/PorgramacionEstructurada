
# ¿Que es una variable Unidimensional y Bidimensional?
# "Una variable unidimensional es una característica única analizada en una población (ej. edad), mientras que una variable bidimensional 
# estudia dos características simultáneamente en los mismos individuos" 
# (ej. edad y sueldo) para encontrar relaciones entre ellas.

#Variables unidimensionales:
#Se refiere al estudio de una sola característica o atributo numérico de un grupo de individuos
# Variable unidimensional

print("Ejemplo de variable unidimensional: ")
numeros = [10, 20, 30, 40, 50]

# Mostrar toda la lista
print("Lista completa:")
print(numeros)

# Mostrar elementos individuales
print("\nElementos individuales:")
print(numeros[0])   # Primer elemento
print(numeros[2])   # Tercer elemento

# Recorrer la lista
print("\nRecorrido de la lista:")
for numero in numeros:
    print(numero)


#Variavles bidimensionales:
#Resulta del estudio de dos características diferentes (\(X\) e \(Y\)) simultáneamente sobre cada individuo de cada problación

print("Ejemeplo de variable bidimensional: ")
# Variable bidimensional

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostrar toda la matriz
print("Matriz completa:")
print(matriz)

# Mostrar elementos específicos
print("\nElemento fila 1 columna 2:")
print(matriz[0][1])

print("\nElemento fila 3 columna 1:")
print(matriz[2][0])

# Recorrer la matriz
print("\nRecorrido de la matriz:")

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()



