def temp_prom(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio semanal de cuatro ciudades de Ecuador.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas como valores.
    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "Quito": [22, 25, 26, 24],
    "Puyo": [28, 30, 29, 31 ],
    "Cuenca": [21, 20, 22, 18],
    "Nueva Loja": [32, 33, 34, 30],
    "El Coca": [26, 28, 27, 29]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temp_prom(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio Semanal por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")
