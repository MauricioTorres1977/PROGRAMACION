# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Mauricio Torres",
    "edad": 30,
    "ciudad": "Ciudad A",
    "profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Ciudad de Puyo"

# Agregar nueva clave-valor para la profesión
informacion_personal["profesion"] = "Ing. Sistemas"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "099-563-563"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)

