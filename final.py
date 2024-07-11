estudiantes = []
codigos_estudiantes = []
materias = []
codigos_materias = []
notas = {}

def menu_principal():
    while True:
        print("\n-- Menu principal --")
        print("1. Agregar estudiante")
        print("2. Agregar materia")
        print("3. Registrar nota")
        print("4. Mostrar notas de un estudiante")
        print("5. Mostrar promedio de notas por materia")
        print("6. Mostrar nota más alta por materia")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_materia()
        elif opcion == "3":
            registrar_nota()
        elif opcion == "4":
            mostrar_notas_estudiante()
        elif opcion == "5":
            mostrar_promedio_notas_materia()
        elif opcion == "6":
            mostrar_nota_mas_alta_materia()
        elif opcion == "7":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def agregar_estudiante():
    codigo = input("Ingrese el código del estudiante: ")
    if codigo in codigos_estudiantes:
        print("El código del estudiante ya existe, por favor intente de nuevo.")
        return
    
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nombre)
    codigos_estudiantes.append(codigo)
    notas[codigo] = {}

    print(f"Estudiante {nombre} agregado exitosamente.")

def agregar_materia():
    codigo = input("Ingrese el código de la materia: ")
    if codigo in codigos_materias:
        print("El código de la materia ya existe, por favor intente de nuevo.")
        return
    
    nombre = input("Ingrese el nombre de la materia: ")
    materias.append(nombre)
    codigos_materias.append(codigo)

    print(f"Materia {nombre} agregada exitosamente.")

def registrar_nota():
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    if codigo_estudiante not in codigos_estudiantes:
        print("El código del estudiante no existe, por favor intente de nuevo.")
        return
    
    codigo_materia = input("Ingrese el código de la materia: ")
    if codigo_materia not in codigos_materias:
        print("El código de la materia no existe, por favor intente de nuevo.")
        return
    
    if codigo_materia in notas[codigo_estudiante]:
        print("El estudiante ya tiene una nota registrada para esta materia, por favor intente de nuevo.")
        return
    
    nota = float(input("Ingrese la nota del estudiante: "))
    notas[codigo_estudiante][codigo_materia] = nota

    print(f"Nota {nota} registrada exitosamente para el estudiante con código {codigo_estudiante} en la materia con código {codigo_materia}.")

def mostrar_notas_estudiante():
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    if codigo_estudiante not in codigos_estudiantes:
        print("El código del estudiante no existe, por favor intente de nuevo.")
        return
    
    notas_estudiante = notas[codigo_estudiante]
    print(f"Notas del estudiante con código {codigo_estudiante}:")