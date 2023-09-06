def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])

if __name__ == "__main__":
    matriz = [[5, 3, 8],
              [1, 6, 2],
              [7, 4, 9]]

    print("Matriz original:")
    imprimir_matriz(matriz)

    fila_a_ordenar = 1  # Cambia esto para ordenar una fila diferente (0, 1 o 2)
    ordenar_fila(matriz, fila_a_ordenar)

    print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
    imprimir_matriz(matriz)



