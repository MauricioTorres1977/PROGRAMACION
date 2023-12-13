class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

    def obtener_temperatura(self):
        return self.temperatura

class PromedioSemanal:
    def __init__(self):
        self.clima_diario = []

    def agregar_dia(self, dia, temperatura):
        clima = ClimaDiario(dia, temperatura)
        self.clima_diario.append(clima)

    def calcular_promedio_semanal(self):
        total_temperaturas = 0
        for clima in self.clima_diario:
            total_temperaturas += clima.obtener_temperatura()
        promedio_semanal = total_temperaturas / len(self.clima_diario)
        return promedio_semanal

# Ejemplo de uso
promedio_semanal_ecuador = PromedioSemanal()

# Ingresar datos diarios
promedio_semanal_ecuador.agregar_dia("Lunes", 25)
promedio_semanal_ecuador.agregar_dia("Martes", 26)
promedio_semanal_ecuador.agregar_dia("Miércoles", 24)
promedio_semanal_ecuador.agregar_dia("Jueves", 27)
promedio_semanal_ecuador.agregar_dia("Viernes", 26)
promedio_semanal_ecuador.agregar_dia("Sábado", 25)
promedio_semanal_ecuador.agregar_dia("Domingo", 28)

# Calcular y mostrar el promedio semanal
promedio_semanal = promedio_semanal_ecuador.calcular_promedio_semanal()
print(f"El promedio semanal de temperatura en Ecuador es: {promedio_semanal} grados Celsius")
