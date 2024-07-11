x# Definición de listas para estudiantes, materias y notas
codigos_estudiantes = []
nombres_estudiantes = []
codigos_materias = []
nombres_materias = []
notas_estudiantes = {}

# Función para mostrar el menú principal
def mostrar_menu():
    print("------ Menú Principal ------")
    print("1. Agregar Estudiante")
    print("2. Agregar Materia")
    print("3. Registrar Nota")
    print("4. Mostrar Notas de un Estudiante")
    print("5. Mostrar Promedio de Notas por Materia")
    print("6. Mostrar Nota Más Alta por Materia")
    print("0. Salir")

# Función para agregar un estudiante
def agregar_estudiante():
    codigo = input("Ingrese el código del estudiante: ")
    if codigo in codigos_estudiantes:
        print("Error: El código del estudiante ya existe.")
        return
    nombre = input("Ingrese el nombre del estudiante: ")
    codigos_estudiantes.append(codigo)
    nombres_estudiantes.append(nombre)
    notas_estudiantes[codigo] = {}

# Función para agregar una materia
def agregar_materia():
    codigo = input("Ingrese el código de la materia: ")
    if codigo in codigos_materias:
        print("Error: El código de la materia ya existe.")
        return
    nombre = input("Ingrese el nombre de la materia: ")
    codigos_materias.append(codigo)
    nombres_materias.append(nombre)

# Función para registrar una nota
def registrar_nota():
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    if codigo_estudiante not in codigos_estudiantes:
        print("Error: El código del estudiante no existe.")
        return
    codigo_materia = input("Ingrese el código de la materia: ")
    if codigo_materia not in codigos_materias:
        print("Error: El código de la materia no existe.")
        return
    if codigo_materia in notas_estudiantes[codigo_estudiante]:
        print("Error: El estudiante ya tiene una nota en esta materia.")
        return
    nota = float(input("Ingrese la nota del estudiante en la materia: "))
    notas_estudiantes[codigo_estudiante][codigo_materia] = nota

# Función para mostrar las notas de un estudiante
def mostrar_notas_estudiante():
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    if codigo_estudiante not in codigos_estudiantes:
        print("Error: El código del estudiante no existe.")
        return
    notas = notas_estudiantes[codigo_estudiante]
    print(f"Notas del estudiante {nombres_estudiantes[codigos_estudiantes.index(codigo_estudiante)]}:")
    for codigo_materia in notas:
        nombre_materia = nombres_materias[codigos_materias.index(codigo_materia)]
        print(f"{nombre_materia}: {notas[codigo_materia]}")

# Función para mostrar el promedio de notas por materia
def mostrar_promedio_notas_materia():
    for i in range(len(codigos_materias)):
        codigo_materia = codigos_materias[i]
        nombre_materia = nombres_materias[i]
        notas_materia = []
        for notas_estudiante in notas_estudiantes.values():
            if codigo_materia in notas_estudiante:
                notas_materia.append(notas_est