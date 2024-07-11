def menuPrincipal():
  while True:
  
    print("==========Menu Principal==========")
    print("1. listar cursos")
    print("2. Registrar curso")
    print("3. Actualizar curso")
    print("4. Eliminar curso")
    print("5. Salir")
    print("================================")
    opcion = int(input("Seleccione una opcion: "))

    if opcion < 1 or opcion > 5:
      print("Opcion incorrecta, ingrese nuevamente...")
    elif opcion == 5:
      print("Gracias por utilizar este sistema!!")
      break
    else:
      ejercutar(opcion)


def ejercutar(opcion):
  dao = DAO()

  if opcion ==1:
  elif opcion == 2: 
    print('Regsitro')
  elif opcion == 3: 
    print('Actualización')
    elif opcion == 4: 
    print('Eliminación')



  print(opcion)


menuPrincipal()

