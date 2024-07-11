def menuPrincipal():
    print("=========================")
    print("          Menu")
    print("=========================")
    print("1. Crud estudiantes.")
    print("2. Crud Materias.")
    print("3. Crud Notas.")
    print("4. Estadisticas.")
    print("5. Salir.")
    print("=========================")

def crudEstudiante(lista, codigos):

    while True:
        
        print("=========================")
        print("       Estudiantes")
        print("=========================")
        print("1. Agregar estudiantes.")
        print("2. Actualizar estudiantes.")
        print("3. Borrar estudiantes.")
        print("4. Lista de estudiantes.")
        print("5. Buscar de estudiantes.")
        print("6. Salir.")
        print("=========================")
        
        opcion = int(input("Ingrese una opcion: "))

        if  opcion == 1:
            
            agregar(lista, codigos)

        elif opcion == 2:
            
            actualizar(lista, codigos)

        elif opcion == 3:
            
            borrar(lista, codigos)

        elif opcion == 4:
            
            listas(lista, codigos)
        
        elif opcion == 5:
            
            buscar(lista, codigos)
                
        elif opcion == 6:
            
            print("Saliendo del programa...")
            break
        
        else:
            print("Selecione una opción valida...")

def crudMaterias(lista, codigos):
    while True:
        
        print("=========================")
        print("       Materias")
        print("=========================")
        print("1. Agregar materias.")
        print("2. Actualizar materias.")
        print("3. Borrar materias.")
        print("4. Lista de materias.")
        print("5. Buscar materias.")
        
        print("6. Salir.")
        print("=========================")
        
        opcion = int(input("Ingrese una opcion: "))
    
        if  opcion == 1:
            
            agregar(lista, codigos)

        elif opcion == 2:
            
            actualizar(lista, codigos)

        elif opcion == 3:
            
            borrar(lista, codigos)

        elif opcion == 4:
            
            listas(lista, codigos)
        
        elif opcion == 5:
            
            buscar(lista, codigos)
                
        elif opcion == 6:
            
            print("Saliendo del programa...")
            break
        
        else:
            print("Selecione una opción valida...")

def crudNotas(codEstudiantes, codMaterias, codE, codM, notas,listaMaterias):
  
    while True:
        print("=========================")
        print("         Notas")
        print("1. Agregar notas.")
        print("2. Lista de notas.")
        print("3. Actualizar notas.")
        print("4. Borrar notas.")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print("=========================")
            print("         Agregar Notas.")        
            while True:
                codigoEstudiante = int(input("Ingrese el codigo del estudiante (1 si desea salir): "))
                if codigoEstudiante == 1:
                    break
                if codigoEstudiante not in codigoEstudiantes:
                  print("El codigo de estudiante no se encuentra.")
                  break

                codigoMateria = int(input("Ingrese el codigo de la materia: "))
                if codigoEstudiante in codEstudiantes and codigoMateria in codMaterias:
                    sinRepetir = False
                    for repetido in range(len(codM)):
                        if codE[repetido] == codigoEstudiante and codM[repetido] == codigoMateria:
                            sinRepetir = True
                    if sinRepetir == True:
                        print(f"La {codigoMateria} del estudiante {codigoEstudiante} ya tiene una nota.")
                    else:
                        while True:
                            nota = float(input("Ingrese la nota: ")) 
                            if nota >= 0 and nota <= 10:
                                codE.append(codigoEstudiante)
                                codM.append(codigoMateria)
                                notas.append(nota)
                                print("Se ha añadido la nota: ", nota)
                                break
                            else:
                                print("Digite una nota valida")
                else:
                    print("Datos Invalidos")
                        
        elif opcion == 2:
            print("=========================")
            print("         Lista de Notas.")
            
            for elementos in range(len(notas)):
                buscar = codM[elementos]
                indice = codMaterias.index(buscar)
                print("Estudiante:", codE[elementos],  listaMaterias[indice], ":", notas[elementos])
                
        elif opcion == 3:
            print("=========================")
            print("    Actualizar Notas.")            
                    
            while True:
                codigoEstudiante = int(input("Ingrese el codigo del estudiante (1 si desea salir): "))
                if codigoEstudiante == 1:
                    break
                codigoMaterias = int(input("Ingrese el codigo de la materia: "))
                if codigoMaterias in codM:
                    while True:
                        notaNueva = float(input("Ingrese la nueva nota: "))
                        notas[indice] = notaNueva
                        print("Se ha actualizado con exito")
                        break
                else:
                    print(f"\nError. {codigoMaterias} no está en la lista.")
                    break
        elif opcion == 4:
            print("=========================")
            print("         Borrar Notas.")
            while True:
                codigoEstudiante = int(input("Ingrese el codigo del estudiante (1 si desea salir): "))
                if codigoEstudiante == 1:
                    break
                codigoMateria = int(input("Ingrese el codigo de la materia: "))
                indice = codMaterias.index(codigoMateria)
                indice2 = codEstudiantes.index(codigoEstudiante)
                if indice == indice2:
                    codE.pop(indice)
                    codM.pop(indice)
                    notas.pop(indice)
        else:
            print("Saliendo...")
            break

def estadistica(codEstudiantes, codMaterias, codE, codM, notas, listaEstudiantes, listaMaterias):
    
     while True:
        print("=========================")
        print("         Estadisticas")
        print("1. Notas Estudiantes.")
        print("2. Promedio Materias.")
        print("3. Puntajes Mayores.")
        print("4. Puntajes Menores.")
        print("5. Salir")
        
        opcion = int(input("Digite una opcion: "))
    
        if opcion == 1:
            print("=========================")
            print("         Notas Estudiantes")
            
            codigoEstudiante = int(input("Ingrese el código del estudiante: "))
            
            if codigoEstudiante not in codEstudiantes:
                
                print("El estudiante no está en la lista.")
            else:
                indiceEstudiante = codEstudiantes.index(codigoEstudiante)
                nombreEstudiante = listaEstudiantes[indiceEstudiante]
            
                print("Notas de", nombreEstudiante)
                    
                for codigoEst in range(len(codE)):
                    if codE[codigoEst] == codigoEstudiante:
                        codigoMateria = codM[codigoEst]
                        indiceMateria = codMaterias.index(codigoMateria)
                        nombreMateria = listaMaterias[indiceMateria]
                        nota = notas[codigoEst]
                        print(nombreMateria, ":", nota)

        elif opcion == 2:

            print("=========================")
            print("         Promedio de Notas")
            for lista in range(len(listaMaterias)):
                nombreMateria = listaMaterias[lista]
                sumaNotas = 0
                cantidadEstudiantes = 0
                
                for codigo in range(len(codM)):
                    if codM[codigo] == codMaterias[lista]:
                        nota = notas[codigo]
                        sumaNotas += nota
                        cantidadEstudiantes += 1
                
                if cantidadEstudiantes > 0:
                    promedio = sumaNotas / cantidadEstudiantes
                    print(nombreMateria, ":", promedio)
                else:
                    print(nombreMateria, ": No hay notas registradas.")
                
        elif opcion == 3: 

            print("=========================")
            print("         Notas Mayores")

            for materia in listaMaterias:

                puntaje_mayor = 0

                for i in range(len(codM)):

                    if listaMaterias[codMaterias.index(codM[i])] == materia:

                        if notas[i] > puntaje_mayor:

                            puntaje_mayor = notas[i]

                print(f"{materia}: {puntaje_mayor}")
                
        elif opcion == 4:  
            print("=========================")
            print("         Notas Menores")

            for lista in range(len(listaMaterias)):
                nombreMateria = listaMaterias[lista]
                notasMateria = []
                
                for codigoMateria in range(len(codM)):
                    if codM[codigoMateria] == codMaterias[lista]:
                        nota = notas[codigoMateria]
                        notasMateria.append(nota)
                
                if len(notasMateria) > 0:
                    minNota = min(notasMateria)
                    print(f"{nombreMateria} : {minNota}")
                else:
                    print(nombreMateria, ": No hay notas registradas.")
        else:
            print("Saliendo del programa.")
            break
            
def agregar(lista, codigos):
    
    print("        Opcion 1 Agregar ")
    print("===================================")
            
    while True:
                
        nombre =input("Ingrese el nombre que desea agregar (1 si desea salir): ")
        if nombre != "1":
                    
            if nombre in lista:
                print(f"{nombre} ya se encuentra enlistado")
            else:
                        
                while True:
                            
                    codigo = int(input(f"Digite el codigo de {nombre}:"))
                            
                    if (codigo >= 1000 and codigo <= 9999):
                                
                        if codigo in codigos:
                                
                            print(f"El codigo {codigo} ya se encuentra enlistado...")
                                
                        else:
                                
                            print(f"Se ha agregado a {nombre} cuyo codigo es {codigo} correctamente")
                            lista.append(nombre)
                            codigos.append(codigo)
                            break
                    else:
                        print("Digite un codigo valido...")
                        
        else:
            print("Saliendo...")
            break
    
def actualizar(lista, codigos):
    
    while True:
                
            print("     Opcion 2 Actualizar")
            print("===================================")
            print("1. Actualizar nombre.")
            print("2. Actualizar codigo.")
            print("3. Salir.")
                            
            opcion = int(input("Ingrese una opción: "))
                
            #Actualizar nombre
                
            if opcion == 1:
            
                while True:
                
                    nombreAntiguo = input("Ingrese el nombre que desea actualizar (1 si desea salir): ")
                    if nombreAntiguo != "1":
                    
                        if nombreAntiguo in lista:
                        
                            while True:
                            
                                nombreNuevo = input("Ingrese el nuevo nombre: ")
                                if nombreNuevo in lista:
                                    print(f"El nombre {nombreNuevo} ya se encuentra enlistado...")
                                
                                else:
                                    indice = lista.index(nombreAntiguo)
                                    lista[indice] = nombreNuevo
                                    print(f"Se ha actualizado {nombreAntiguo} por {nombreNuevo}")
                                    break
                        else:
                            print(f"{nombreAntiguo} no se encuentra enlistado")
                                
                    else:
                        print("Saliendo...")
                        break
                        
            #Actualizar codigo
                
            elif opcion == 2:
                    
                while True:
                    codigoAntiguo = int(input("Ingrese el codigo que desea actualizar: "))
                    if codigoAntiguo != "x":
                        if codigoAntiguo >= 1000 and codigoAntiguo < 10000:
                            
                            if codigoAntiguo in codigos:
                                
                                while True:
                                    codigoNuevo = int(input("Ingrese el nuevo codigo: "))
                                    if codigoNuevo in codigos:
                                        print("Este codigo ya se encuentra enlistado")
                                    else:
                                        if codigoNuevo >= 1000 and codigoNuevo < 10000:
                                            indice = codigos.index(codigoAntiguo)
                                            codigos[indice] = codigoNuevo
                                            print(f"Se ha actualizado codigo {codigoAntiguo} por {codigoNuevo}")
                                            break
                                        else:
                                            print("Digite un codigo valido...")

                            else:
                                print(f"El codigo {codigoAntiguo} no se encuentra enlistado")
                        else:
                            print("Ingrese un codigo valido")
                        
                    else:
                        print("Saliendo...")
                        break
                    continuar = input("¿Desea continuar?(si / no): ")
                        
                    if continuar == "si":
                        print()
                    elif continuar == "no":
                        print("Saliendo...")
                        break    
                    else:
                        print("Ingrese una opcion valida...")
            elif opcion == 3:
                print("Saliendo")
                break
                
            else:
                print("Digite una opcion valida...")
                
def borrar(lista, codigos):
    
    print("        Opcion 3 Borrar")
    print("===================================")
            
    while True: 
        print("1. Borrar por nombre")
        print("2. Borrar por codigo")
        print("3. Salir")          
        opcion = int(input("Ingrese una opción: "))
                
        #Borrar por nombre
                
        if opcion == 1:
                    
            while True:
                nombre = input("Ingrese el nombre que desea eliminar (1 si desea salir): ")
                    
                if nombre != "1":
                    if nombre in lista:
                        indice = lista.index(nombre)
                        lista.pop(indice)
                        codigo = codigos.pop(indice)
                        print(f"Se ha borrado a {nombre}, cuyo codigo era {codigo}")
                    else:
                        print(f"El nombre {nombre} no se encuentra enlistado")
                                
                                
                else:
                    print("Saliendo...")
                    break
                    
        #Borrar por codigo
                
        elif opcion == 2:
            
            while True:
                codigo = int(input("Ingrese el codigo que desea eliminar: "))
                        
                if codigo in codigos:
                    indice = codigos.index(codigo)
                    nombre = lista.pop(indice)
                    codigos.pop(indice)
                    print(f"Se a borrado a {nombre}, cuyo codigo era {codigo}")
                        
                else:
                    print(f"El codigo {codigo} no se encuentra enlistado")
                        
                continuar = input("¿Desea continuar?(si / no): ")
                        
                if continuar == "si":
                    print()
                elif continuar == "no":
                    print("Saliendo...")
                    break    
                else:
                    print("Digite una opcion valida...")
                    
        elif opcion == 3:
            print("Saliendo...")
            break
                    
        else:
            print("Digite una opción valida...")
            
def listas(lista, codigos):
    
    print("        Opcion 4 Lista")
    print("===================================")
    contador = 1
    print("Num    Nombre    Codigo")
    for elementos in range(len(lista)):
        print(contador,".  ", lista[elementos], "   ", codigos[elementos] ) # arreglar tabla 
        contador += 1

def buscar(lista, codigos):
    
    print("        Opcion 5 Buscar")
    print("===================================")
    
    while True:
        
        print("1. Buscar por nombre.")
        print("2. Buscar por codigo")
        print("3. Salir")
        
        opcion = int(input("Ingrese una opción: "))
        
        #Por nombre
        if opcion == 1:
            
            while True:
                
                nombre = input("Ingrese el nombre que desea buscar: ")
                if nombre in lista:
                    indice = lista.index(nombre)
                    codigo = codigos[indice]
                    print(f"Se encuentra enlistado en la posicion {indice}, cuyo codigo es {codigo}")
                    
                else:
                    print("El nombre no se encuentra enlistado...")
                    
                continuar = input("¿Desea continuar? (si / no)")
               
                    
                if continuar == "si":
                    print("continuando")
                elif continuar == "no":
                    print("Saliendo...")
                    break
                else:
                    print("Digite una opción valida...")
                    
        elif opcion == 2:
            
            codigo = int(input("Ingrese el codigo que desea buscar: "))
            if codigo in codigos:
                indice = codigos.index(codigo)
                nombre = lista[indice]
                print(f"Se encuentra enlistado en la posicion {indice}, cuyo nombre es {nombre}")
            
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Ingrese una opción valida...")
                    
listaEstudiantes=["Maria","Luisa","Marta"]
codigoEstudiantes=[1020,1021,1022]

listaMaterias=["Español","Arte","Deporte"]
codigoMaterias=[5020,5021,5022]

codE =[1020,1020,1020,1021,1022,1022,1022,1021]
codM =[5020,5021,5022,5020,5020,5022,5021,5021]
notas=[7.5,6.5,4.0,8.0,6.0,10,8.0,9.0]

while True:
    
    menuPrincipal()
    opcion = int(input("Ingrese una opcion: "))
    
    if  opcion == 1:
        crudEstudiante(listaEstudiantes, codigoEstudiantes)
    elif opcion == 2:
        crudMaterias(listaMaterias, codigoMaterias)
    elif opcion == 3:
        crudNotas(codigoEstudiantes,codigoMaterias, codE, codM, notas, listaMaterias)
    elif opcion == 4:
        estadistica(codigoEstudiantes, codigoMaterias, codE, codM, notas, listaEstudiantes, listaMaterias)
    elif opcion == 5:
        print("Saliendo del programa.| Vuelva pronto")
        break
    else:
        print("Selecione una opción valida...")