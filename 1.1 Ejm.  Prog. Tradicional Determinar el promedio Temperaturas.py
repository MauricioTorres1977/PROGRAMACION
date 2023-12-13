def ingresar_temperaturas_ciudad(ciudad):
    temperaturas_ciudad = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura para el día {dia} en {ciudad}: "))
        temperaturas_ciudad.append(temperatura)
    return temperaturas_ciudad

def calcular_promedio_semanal(temperaturas_ciudad):
    total_temperaturas = sum(temperaturas_ciudad)
    promedio = total_temperaturas / len(temperaturas_ciudad)
    return promedio

def main():
    ciudades = ["Quito", "Guayaquil", "Cuenca"]
    promedios_semanales = {}

    for ciudad in ciudades:
        print(f"\nIngrese las temperaturas diarias de la semana para {ciudad}:")
        temperaturas_ciudad = ingresar_temperaturas_ciudad(ciudad)

        promedio_semanal = calcular_promedio_semanal(temperaturas_ciudad)
        promedios_semanales[ciudad] = promedio_semanal

    print("\nPromedios semanales:")
    for ciudad, promedio in promedios_semanales.items():
        print(f"{ciudad}: {promedio:.2f}°C")

if __name__ == "__main__":
    main()

