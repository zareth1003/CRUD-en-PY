def menuPrincipal():
  while True:
    print("===== Menu-Principal ======")
    print("1-Menú Estudiantes")
    print("2-Menú Materias")
    print("3-Menú Notas")
    print("4-Estadisticas/Notas")
    print("5-Salir")
    print("======================")

    opcion = int(input('Escoja una opción: '))

    if opcion ==1:
      crudEstudiante(estudiantes, codigo_estudiantes, codigo_materia_nota)
    elif opcion ==2:
      crudMateria(codigo_materias, lista_materias, codigo_materia_nota)
    elif opcion ==3:
      crudNotas(estudiantes,codigo_estudiantes ,notas, lista_materias,codigo_materias)
    elif opcion ==4:
      CrudEstadistica(estudiantes,codigo_estudiantes, notas, lista_materias, codigo_materia_nota, codigo_materias, codigo_estudiante_nota)
    elif opcion ==5:
      print('Saliendo del programa...')
      break
    else:
      print('ERROR Opcion invalida, intente nuevamente...')


def crudEstudiante(estudiantes, codigo_estudiantes, notas):
  while True:
    print("=======CRUD Estudiante========")
    print("1-Ingresar Estudiantes")
    print("2-Listar Estudiante")
    print("3-Actualizar Estudiante")
    print("4-Eliminar Estudiante")
    print("5-Buscar Estudiantes")
    print("6-Volver al menu principal")
    print("================================")

    opcion = int (input('Escoja una opción: '))

    if opcion == 1:
      agregarEstudiante(estudiantes,codigo_estudiantes)
    if opcion ==2:
      listarEstudiante(estudiantes, codigo_estudiantes)
    if opcion ==3:
      actualizarEstudiante(estudiantes, codigo_estudiantes)
    if opcion ==4:
      eliminarEstudiante(estudiantes, codigo_estudiantes, codigo_estudiante_nota)
    if opcion ==5:
      buscarEstudiante(estudiantes, codigo_estudiantes, notas)
    if opcion ==6:
      break
  else:
    print('ERROR...Opcion incorrecta... Intente de nuevo')

def agregarEstudiante(estudiantes, codigo_estudiantes):
    while True:
      nombreEstudiante = str(input('Ingrese el nombre del estudiante que desea agregar (Presiones 1 para salir): '))
      if nombreEstudiante =="1":
        print('Volviendo al mení anterior...')
        break
      codigo = int(input('Ingrese el codigo del estudiante: '))

      if codigo=='1':
        break
      elif nombreEstudiante in estudiantes:
        print(f'{nombreEstudiante} ya se encuentra en la base de datos')
        break
      elif codigo in codigo_estudiantes:
        print(f'EL codigo ingresado {codigo} ya se encuentra  registrado en la base de datos')
        break
      elif codigo not in codigo_estudiantes and nombreEstudiante not in estudiantes:
        estudiantes.append(nombreEstudiante)
        codigo_estudiantes.append(codigo)
        print('Estudiante agregado satisfactoriamente...')
        break
      else:
       print('Saliendo...')

def listarEstudiante(estudiantes, codigo_estudiantes):
  for listarNombre in estudiantes:
    for listarCodigo in codigo_estudiantes:
      posicion= estudiantes.index(listarNombre)
    print(estudiantes[posicion], codigo_estudiantes[posicion])


def actualizarEstudiante(estudiantes, codigo_estudiantes):
  while True:
    codigo = int(input('Ingrese el codigo del estudiante que desea actualizar (Presione 0 para salir del menú): '))
    if codigo == 0:
      break
    if codigo not in codigo_estudiantes:
      print('ERROR... El codigo ingresado no existe..')
    else:  
      if codigo in codigo_estudiantes:
        nombreNuevo = input('Ingrese el nuevo nombre: ')
        indice = codigo_estudiantes.index(codigo)
        if nombreNuevo in estudiantes:
          print('ERROR... el nombre del estudiante ya existe')
        else:
          estudiantes[indice] = nombreNuevo
          codigo_estudiantes[indice] = codigo
          print('El estudiante ha sido actualizado con Existo!!!')


def eliminarEstudiante(estudiantes, codigos, notas):
  while True:
    codigo=int(input (f"Ingrese el codigo del estudiante que desea borrar o ingrese ´0´ volver al menu: "))
    if codigo==0:
      break

    elif codigo in codigos:

      if  codigo in notas:
        print('No se puede eliminar estudiante, porque ya tiene notas asignadas')

      else:
        indice= codigos.index(codigo)
        codigos.pop(indice)
        estudiantes.pop(indice)
        print('El estudiante ha sido eliminado con Exito!!')
    
    else:
      print("NO existe")

def buscarEstudiante(estudiantes, codigos, notas):
  while True:
    print("======Menú Buscar=======")
    print("1. Buscar por nombre.")
    print("2. Buscar por codigo")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion==1:
      #Por Nombre
      while True:
        nombre = input("Ingrese el nombre que desea buscar: ")
        if nombre in estudiantes:
          indice = estudiantes.index(nombre)
          codigo = codigos[indice]
          print(f"Se encuentra enlistado en la posicion {indice+1}, cuyo codigo es {codigo}")
        else:
          print("El nombre no se encuentra enlistado...")

        continuar = input("¿Desea continuar? (si / no): ")
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
        nombre = estudiantes[indice]
        print(f"Se encuentra enlistado en la posicion {indice +1}, cuyo nombre es {nombre}")
      else:
        print("El codigo no se encuentra en nuestra base de datos...")
    elif opcion == 3:
      print("Saliendo...")
      break
    else:
      print("Ingrese una opción valida...")
            

def crudMateria(codigo_materias, lista_materias, codigo_materia_nota):
   while True:
        print("=========================")
        print("       Materias")
        print("=========================")
        print("1. Agregar materias.")
        print("2. Listar materias.")
        print("3. Actualizar materias.")
        print("4. Borrar materias.")
        print("5. Buscar materias.")
        print("6. Salir.")
        print("=========================")
        opcion = int(input("Ingrese una opcion: "))
    
        if  opcion == 1:
          agregarMateria(lista_materias, codigo_materias)
        elif opcion == 2:
          listarMateria(lista_materias, codigo_materias)
        elif opcion == 3:
          actualizarMateria(lista_materias, codigo_materias)
        elif opcion == 4:
          borrarMateria(lista_materias, codigo_materias, codigo_materia_nota)
        elif opcion == 5:
          buscarMateria(lista_materias, codigo_materias, codigo_materia_nota)      
        elif opcion == 6:    
          print("Saliendo del programa...")
          break
        else:
          print("Selecione una opción valida...")

def agregarMateria(lista_materias, codigo_materias):
  while True:
    nombreMateria = str(input('Ingrese el nombre de la materia que desea agregar (Presione 1 para salir): '))
    if nombreMateria =='1':
      break
    nombreMateria=nombreMateria.capitalize()
    codigo= int(input('Ingrese el codigo de la materia: '))
    if codigo =='1':
      break
    elif nombreMateria in lista_materias:
      print(f'{nombreMateria} ya se encuentra en la base de datos')
      break
    elif codigo in codigo_materias:
      print(f'EL codigo ingresado {codigo} ya se encuentra  registrado en la base de datos')
      break
    elif codigo not in codigo_materias and nombreMateria not in lista_materias:
      lista_materias.append(nombreMateria)
      codigo_materias.append(codigo)
      print('Materia Agregada satisfacotiamente...')
      break
    else:
      print('Saliendo...')

def listarMateria (lista_materias, codigo_materias):
  for listarMateria in lista_materias:
    for listarCodigo in codigo_materias:
      posicion = lista_materias.index(listarMateria)
    print(lista_materias[posicion], codigo_materias[posicion])

def actualizarMateria(lista_materias, codigo_materias):
  while True:
    codigo = int(input('Ingrese el codigo de la materia que desea actualizar (Presione 0 para salir del menú): '))
    if codigo == 0:
      break
    if codigo not in codigo_materias:
      print('ERROR... El codigo ingresado no existe..')
    else:  
      if codigo in codigo_materias:
        nombreNuevo = input('Ingrese el nuevo nombre: ')
        indice = codigo_materias.index(codigo)
        if nombreNuevo in lista_materias:
          print('ERROR... el nombre de la materia ya existe')
        else:
          lista_materias[indice] = nombreNuevo
          codigo_materias[indice] = codigo
          print('La materia ha sido actualizado con Existo!!!')
    
def borrarMateria(lista_materias, codigo_materias, codigo_materia_nota):
  while True:
    codigo=int(input (f"Ingrese el codigo de la materia que desea borrar o ingrese ´0´ volver al menu: "))
    if codigo==0:
      break
    elif codigo in codigo_materias:
      if  codigo in codigo_materia_nota:
        print('No se puede eliminar la materia, porque ya tiene notas asignadas')
      else:
        indice= codigo_materias.index(codigo)
        codigo_materia_nota.pop(indice)
        lista_materias.pop(indice)
        print('La materia ha sido eliminada con Exito!!')
    else:
      print("NO existe")

def buscarMateria(lista_materias, codigo_materias, codigo_materia_nota):
  while True:
    print("======Menú Buscar=======")
    print("1. Buscar por nombre.")
    print("2. Buscar por codigo")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion==1:
        #Por Nombre
      while True:
        nombre = input("Ingrese el nombre que desea buscar: ")
        if nombre in lista_materias:
          indice = lista_materias.index(nombre)
          codigo = codigo_materias[indice]
          print(f"Se encuentra enlistado en la posicion {indice+1}, cuyo codigo es {codigo}")
        else:
          print("El nombre no se encuentra enlistado...")

        continuar = input("¿Desea continuar? (si / no): ")
        if continuar == "si":
          print("continuando")
        elif continuar == "no":
          print("Saliendo...")
          break
        else:
          print("Digite una opción valida...")
    elif opcion == 2:
        codigo = int(input("Ingrese el codigo que desea buscar: "))
        if codigo in codigo_materias:
          indice = codigo_materias.index(codigo)
          nombre = lista_materias[indice]
          print(f"Se encuentra enlistado en la posicion {indice +1}, cuyo nombre es {nombre}")
        else:
          print("El codigo no se encuentra en nuestra base de datos...")
    elif opcion == 3:
      print("Saliendo...")
      break
    else:
      print("Ingrese una opción valida...")


def crudNotas(estudiantes,codigo_estudiantes ,notas, lista_materias,codigo_materias):
  #Actualizar....
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
        #validar codigo estudiante
        codigoEstudiante = int(input("Ingrese el codigo del estudiante (1 si desea salir): ")) 
        if codigoEstudiante == 1:
          break  
        if codigoEstudiante not in codigo_estudiantes:
          print('El estudiante no tiene matriculado')
          break
        
        codigoMateria = int(input("Ingrese el codigo de la materia: "))
        if codigoEstudiante in codigo_estudiantes and codigoMateria in codigo_materias:
          sinRepetir = False
          for repetido in range(len(codigo_materia_nota)):
            if codigo_estudiante_nota[repetido] == codigoEstudiante and codigo_materia_nota[repetido] == codigoMateria:
              sinRepetir = True
          if sinRepetir:
            print(f"La {codigoMateria} del estudiante {codigoEstudiante} ya tiene una nota.")
            
          else:
            while True:
              nota = float(input("Ingrese la nota: "))
              if nota >= 0 and nota <= 10:
                codigo_estudiante_nota.append(codigoEstudiante)
                codigo_materia_nota.append(codigoMateria)
                notas.append(nota)
                print("Se ha añadido la nota: ", nota)
                break
              else:
                print("Digite una nota valida")

    elif opcion == 2:
      print("=========================")
      print("         Lista de Notas.")
      for elementos in range(len(notas)):
        buscar = codigo_materia_nota[elementos]
        indice = codigo_materias.index(buscar)
        print("Estudiante:", codigo_estudiante_nota[elementos],  lista_materias[indice], ":", notas[elementos])
                
    elif opcion == 3:
      print("=========================")
      print("    Actualizar Notas.")            
      while True:
        codigoEstudiante = int(input("Ingrese el codigo del estudiante (1 si desea salir): "))
        if codigoEstudiante == 1:
          break
        if codigoEstudiante not in codigo_estudiantes:
          print("EL ESTUDIANTE NO ESTÁ REGISTRADO!!")
        codigoMaterias = int(input("Ingrese el codigo de la materia: "))
        if codigoMaterias in codigo_materia_nota:
          while True:
            notaNueva = float(input("Ingrese la nueva nota: "))
            buscar = codigo_materia_nota.index(codigoMaterias)
            notas.pop(buscar)
            notas.insert(buscar,notaNueva)
            print("Se ha actualizado con exito")
            break
        else:
          print(f"\nError. {codigo_materias} no está en la lista.")
          break


    elif opcion == 4:
      print("=========================")
      print("         Borrar Notas.")
      while True:
        codigoEstudiante = int(input("Ingrese el codigo del estudiante (1 si desea salir): "))
        if codigoEstudiante == 1:
          break
        codigoMateria = int(input("Ingrese el codigo de la materia: "))
        indice = codigo_materias.index(codigoMateria)
        indice2 = codigo_estudiantes.index(codigoEstudiante)
        if indice == indice2:
          codigo_estudiante_nota.pop(indice)
          codigo_materia_nota.pop(indice)
          notas.pop(indice)
          print('Nota borrada con EXITO!!')
    else:
      print("Saliendo...")
      break

def CrudEstadistica(estudiantes,codigo_estudiantes, notas, lista_materias, codigo_materia_nota, codigo_materias, codigo_estudiante_nota):
  
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
            if codigoEstudiante not in codigo_estudiantes:
              print("El estudiante no está en la lista.")
            else:
              indiceEstudiante = codigo_estudiantes.index(codigoEstudiante)
              nombreEstudiante = estudiantes[indiceEstudiante]
              print("Notas de", nombreEstudiante)
              for codigoEst in range(len(codigo_estudiante_nota)):
                if codigo_estudiante_nota[codigoEst] == codigoEstudiante:
                  codigo = codigo_materia_nota[codigoEst]
                  indiceMateria = codigo_materias.index(codigo)
                  nombreMateria = lista_materias[indiceMateria]
                  nota = notas[codigoEst]
                  print(nombreMateria, ":", nota)

        elif opcion == 2:
            print("=========================")
            print("         Promedio de Notas")
            for lista in range(len(lista_materias)):
                nombreMateria = lista_materias[lista]
                sumaNotas = 0
                cantidadEstudiantes = 0
                
                for codigo in range(len(codigo_materia_nota)):
                    if codigo_materia_nota[codigo] == codigo_materias[lista]:
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
            for materia in lista_materias:
                puntaje_mayor = 0
                for i in range(len(codigo_materias)):
                    if lista_materias[codigo_materias.index(codigo_materia_nota[i])] == materia:
                        if notas[i] > puntaje_mayor:
                            puntaje_mayor = notas[i]
                print(f"{materia}: {puntaje_mayor}")
      
        elif opcion == 4:  
            print("=========================")
            print("         Notas Menores")
            for lista in range(len(lista_materias)):
                nombreMateria = lista_materias[lista]
                notasMateria = []
                for codigo in range(len(codigo_materia_nota)):
                    if codigo_materia_nota[codigo] == codigo_materias[lista]:
                        nota = notas[codigo]
                        notasMateria.append(nota)
                if len(notasMateria) > 0:
                    minNota = min(notasMateria)
                    print(f"{nombreMateria} : {minNota}")
                else:
                    print(nombreMateria, ": No hay notas registradas.")
        else:
            print("Saliendo del programa.")
            break
    


estudiantes=["Maria","Luisa","Marta"]
codigo_estudiantes=[1020,1021,1022]

lista_materias=["Español","Arte","Deporte"]
codigo_materias=[5020,5021,5022]

lista_tipos=["Estudiante","Materia","Nota"]

codigo_estudiante_nota=[1020,1020,1020,1021,1022,1022,1022,1021]
codigo_materia_nota=[5020,5021,5022,5020,5020,5022,5021,5021]
notas=[7.5,6.5,4.0,8.0,6.0,10,8.0,9.0]




menuPrincipal()