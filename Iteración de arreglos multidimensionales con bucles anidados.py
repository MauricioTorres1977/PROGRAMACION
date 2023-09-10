
import numpy as np

# Definir las ciudades y temperaturas diarias para tres semanas
ciudades = ['Quito', 'Guayaquil', 'Ambato', 'Cuenca', 'Puyo']
semanas = [
    [
        [20, 20, 20, 20, 20, 20, 20],  # Semana 1
        [28, 28, 28, 28, 28, 28, 28],  # Semana 1
        [23, 23, 23, 23, 23, 23, 23],  # Semana 1
        [16, 16, 16, 16, 16, 16, 16],  # Semana 1
        [27, 27, 27, 27, 27, 27, 27]   # Semana 1
    ],
    [
        [14, 14, 14, 14, 14, 14, 14],  # Semana 2
        [24, 24, 24, 24, 24, 24, 24],  # Semana 2
        [19, 19, 19, 19, 19, 19, 19],  # Semana 2
        [18, 18, 18, 18, 18, 18, 18],  # Semana 2
        [29, 29, 29, 29, 29, 29, 29]   # Semana 2
    ],
    [
        [12, 12, 12, 12, 12, 12, 12],  # Semana 3
        [31, 31, 31, 31, 31, 31, 31],  # Semana 3
        [16, 16, 16, 16, 16, 16, 16],  # Semana 3
        [19, 19, 19, 19, 19, 19, 19],  # Semana 3
        [30, 30, 30, 30, 30, 30, 30]   # Semana 3
    ]
]

# Crear una matriz 3D para almacenar las temperaturas
matriz_temperaturas = np.array(semanas)

# Calcular el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    for k, semana in enumerate(matriz_temperaturas):
        # Obtener las temperaturas de la ciudad para la semana actual
        temperaturas_semana = matriz_temperaturas[k, i, :]

        # Calcular el promedio de temperaturas para la ciudad y semana actual
        promedio_semana = np.mean(temperaturas_semana)

        # Mostrar el promedio de temperaturas en la pantalla
        print(f'Promedio de temperatura en {ciudad} para la Semana {k + 1}: {promedio_semana:.2f}°C')
