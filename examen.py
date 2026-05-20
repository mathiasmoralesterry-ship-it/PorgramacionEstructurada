def cargar_datos():
    lista = []
    cantidad = int(input("¿Cuántos números deseas ingresar?: "))
    for i in range(cantidad):
        num = int(input(f"Ingrese número {i+1}: "))
        lista.append(num)
    return lista

def filtrar_elementos(lista):
    filtrada = []
    for n in lista:
        if n % 2 == 0:
            filtrada.append(n)
    return filtrada

def procesar_calculos(lista):
    suma = 0
    for n in lista:
        suma += n
    promedio = suma / len(lista)
    print("\n--- RESULTADOS ---")
    print("Suma:", suma)
    print("Promedio:", promedio)

def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):

            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

datos = cargar_datos()
print("\nLista original:")
print(datos)
pares = filtrar_elementos(datos)
print("\nNúmeros pares:")
print(pares)
procesar_calculos(pares)
ordenada = ordenar_lista(pares)
print("\nLista ordenada:")
print(ordenada)