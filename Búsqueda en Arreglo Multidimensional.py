# Definimos una matriz bidimensional de ejemplo (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return (fila, columna)  # Devolvemos la posición del valor encontrado
    return None  # Devolvemos None si el valor no se encuentra en la matriz

# Valor que deseamos buscar en la matriz
valor_a_buscar = 5

# Llamamos a la función de búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)

# Verificamos si se encontró el valor
if posicion:
    fila, columna = posicion
    print(f"El valor {valor_a_buscar} se encontró en la posición ({fila}, {columna}) de la matriz.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")


