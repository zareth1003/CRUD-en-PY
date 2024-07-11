estudiantes=["maria","luisa","marta"]
codigo_estudiantes=[1020,1021,1022]
#estudiantes=[]
#codigo_estudiantes=[]
#lista_materias=[]
#codigo_materias=[]

lista_materias=["español","arte","deporte"]
codigo_materias=[5020,5021,5022]

lista_tipos=["estudiante","materia","nota"]


codigo_estudiante_nota=[1020,1020,1020,1021,1022,1022,1022,1021]
codigo_materia_nota=[5020,5021,5022,5020,5020,5022,5021,5021]
notas=[7.5,6.5,4.0,8.0,6.0,10,8.0,9.0]

def menu_principal():
    print("===========================")
    print("MENU PRINCIPAL")
    print("1.CRUD Estudiante")
    print("2.CRUD Materias")
    print("3.CRUD Notas")
    print("4.Estadistico")
    print("5.Salir")
    print("===========================")

def menu_crud_estudiantes():
    print("===========================")
    print("MENU CRUD ESTUDIANTES")
    print("1.Ingresar Estudiante")
    print("2.Actualizar Estudiante")
    print("3.Borrar Estudiante")
    print("4.Listar Estudiante")
    print("5.Buscar Estudiantes")
    print("6.Regresar al menu principal")
    print("===========================")
def menu_crud_materia():
    print("===========================")
    print("MENU CRUD MATERIA")
    print("1.Ingresar Materia")
    print("2.Actualizar Materia")
    print("3.Borrar Materia")
    print("4.Listar Materia")
    print("5.Buscar Materia")
    print("6.Regresar al menu principal")

    print("===========================")
def menu_crud_notas():
    print("===========================")
    print("MENU CRUD NOTAS")
    print("1.Ingresar Notas")
    print("2.Actualizar Notas")
    print("3.Borrar Notas")
    print("4.Listar Notas")
    print("5.Buscar Notas")
    print("6.Regresar al menu principal")
    print("===========================")
    
def menu_estadistico():
    print("===========================")  
    print("MENU CRUD ESTADISTICOS")
    print("1.Consultar notas registradas")
    print("2.Promedio de notas de la asignatura")
    print("3.Nota mayor")
    print("4.Nota menor")
    print("5.Regresar al menu principal")
    print("===========================")
def opcion1_crud_ingresar (lista,lista1,tipo):
    while True:
        nombre= input(f"Digite nombre del {tipo} ")
        codigo=int(input(f"Digite codigo de {tipo} "))    
        if nombre=="1" or codigo_estudiantes==1:
         break
        elif nombre in lista:
         print(f"{nombre} ya se encuentra en la lista {lista}")
         break
        elif codigo in lista1:
         print(f"El codigo digitado ya se encuentra registrado en la lista")
         break
        elif codigo not in lista1 and nombre not in lista:
         lista.append(nombre)
         lista1.append(codigo)
         print("Estudiante agregado con exito")
        
         
def opcion2_crud_actualizar(lista,lista1,tipo):
    while True:
        codigo= int(input(f"Digite codigo del {tipo} a actualizar"))
        if codigo==1:
            break
        if codigo in lista1:
         nombre= input(f"Digite nuevo nombre de {tipo}")
         codigo_nuevo=int (input(f"Digite el nuevo codigo de {tipo}"))
         posicion=lista1.index(codigo)
         lista1[posicion]=codigo_nuevo
         lista[posicion]= nombre
         print("Estudiante actualizado con exito")
         continue
        else:
            print("El codigo de estudiante es incorrecto o no se encuentra registrado")
    
def opcion3_crud_borrar(nombres,codigos,tipo):
    while True:
        codigo=int(input (f"Digite codigo del {tipo} al que desea borrar"))
        if codigo in codigos:
         posicion= codigos.index(codigo)
         nombre=nombres.pop(posicion)
         codigos.pop(posicion)
         print("El borrado ha sido exitoso")
        else:
         print("El codigo ingresado no se encuentra en la lista")
        if codigo==1:
            break
def opcion4_crud_listar(lista,lista1,tipo):
    for nombre in lista:
     for cd_materia in lista1:
         poscion=lista.index(nombre)
     print (lista[poscion], lista1[poscion])
     
def opcion5_crud_buscar(lista,lista1,tipo):
    while True:

     codigo=int(input("Digite codigo"))
     if codigo==1:
         break
     if codigo not in lista1:
         print("el codigo ingresado no se encuentra en la lista de estudiantes")
     elif codigo in lista1:
         lugar= lista1.index(codigo)+1
         lugar1=lista1.index(codigo)
         print(f"El codigo digitado se encuentra en la lista de {tipo} en la posicion {lugar} con el nombre {lista[lugar1]}")
         
def opcion1_ingresar_nota(notas,lista_codigo_materia,codigo_materia_nota,lista_codigo_estudiantes,lista_codigo_estudiante_nota):
    while True:
     codigo= int(input ("Digite codigo del estudiantes: "))
     materia_codigo=int(input("Digite materia a la que le registrara la nota: "))
     
     if codigo== 1:
          break
      
     if materia_codigo not in lista_codigo_materia:
         print("la materia digitada no esta registrada, debe registrarla primero para  poder ingresar la nota")
     if codigo not in lista_codigo_estudiantes:
             print("El estudiante ingresado no existe, debe registrarlo para luego ingresar la nota")
        
     if codigo in lista_codigo_estudiantes and materia_codigo in lista_codigo_materia:
         repetido_s= False
         for repetido in range(len(codigo_materia_nota)):
            if lista_codigo_estudiante_nota [repetido]== codigo and codigo_materia_nota[repetido]==materia_codigo:
                 repetido_s=True
         if repetido_s==True:
             print("Ya se registro una nota para este estudiante en esta materia")
             break
         else:
             nota=float(input("Digite nota: "))
             if nota>0 and nota<=10:
                 notas.append (nota)   
                 lista_codigo_estudiante_nota.append(codigo)
                 codigo_materia_nota.append(materia_codigo)
                 print("Nota registrada con exito")
         
         
def opcion2_crud_actualizar_nota(codigo_materia_nota,codigo_estudiante_nota,notas):
    while True:
        cd_materia= int(input("Digite codigo de la materia: "))
        cd_estudiante=int(input("Digite codigo del estudiante: "))
        if cd_materia==1:
            break
        if (cd_materia in codigo_materia_nota) and (cd_estudiante in codigo_estudiante_nota):
         nota_nueva= float(input("Digite nota nueva nota: "))
         posicion=codigo_materia_nota.index(cd_materia)
         notas.pop(posicion)
         notas.insert(posicion,nota_nueva) 
         print("Nota actualizada con exito")
        else:
         print("no existe nota asociada a esa materia aun, debe registrala primero")
         break
            

def lista_notas(codigo_materia_nota,lista_materias,codigo_estudiante_nota,codigo_estudiantes,estudiantes,notas):
    cd_materia=int(input("ingrese el codigo de la materia: "))
    if cd_materia in codigo_materias:
     for i in range (len(codigo_materia_nota)):
         var= codigo_materia_nota[i]
         posicion= codigo_materias.index(cd_materia)
         posicion2=codigo_estudiante_nota [i]
         posicion3=codigo_estudiantes.index(posicion2)
         
         if var==cd_materia:
            print(f"estudiante {estudiantes[posicion3]}  - materia {lista_materias[posicion]} - nota final: {notas[i]} ")
    else:
       print("la materia ingresada no esta regisstrada en el sistema")

def eliminar_nota(codigo_materia_nota,codigo_materias,lista_materias,codigo_estudiante_nota,codigo_estudiantes,notas):
    codigo_estudiante=int(input("ingrese el codio del estudiante para eliminar su nota: "))
    materia=int(input("ingrese codigo de la materia de la que desea eliminar la nota: "))
    if codigo_estudiante not in codigo_estudiantes:
        print("el estudiante no esta registrado")
    if materia not in codigo_materias:
        print("La materia digitada no ha sido registrada")
    else:
     pos=codigo_estudiante_nota.index(codigo_estudiante)
     codigo_estudiante_nota.pop(pos)
     codigo_materia_nota.pop(pos)
     notas.pop(pos)
     print(f"la nota del estudiante {codigo_estudiante} se ha eliminado ")
    
def buscar_nota(codigo_materias,lista_materias,codigo_estudiante_nota,codigo_estudiantes,notas):
    cd_estudiante=int(input("ingrese el codigo del estudiante: "))
    cd_materia=int(input("ingrese el codigo de la materia: "))
    if cd_estudiante not in codigo_estudiantes:
        print("intente nuevamente")
    elif cd_materia not in  codigo_materias:
        print("intente nuevamente")
    else:
        pos1=codigo_estudiante_nota.index(cd_estudiante)
        pos2=codigo_materias.index(cd_materia)
        pos3= codigo_estudiantes.index(cd_estudiante)
        print(f"el codigo del estudiante es {estudiantes[pos3]} nombre de materia {lista_materias[pos2]} nota {notas[pos1]} ")   
        
def notas_codigo_estadisticas(codigo_materias,lista_materias,codigo_estudiante_nota,codigo_estudiantes,notas):
   cd_estudiantes= int (input("Digite codigo de estudiante: "))
   if cd_estudiantes in codigo_estudiante_nota:
     for i in range (len(codigo_estudiante_nota)):
         var= codigo_estudiante_nota[i]
         if var==cd_estudiantes:
             posicion= codigo_estudiantes.index(cd_estudiantes)
             posicion2= codigo_materia_nota[i]
             posicion3= codigo_materias.index(posicion2)
             print(f"estudiante: {estudiantes[posicion]}- materia: {lista_materias[posicion3]} - nota final: {notas[i]} ")

def promedio_materia(codigo_materias,lista_materias,notas):
    for i in range(len(codigo_materias)):
        nota = 0
        cantidad = 0
        for j in range(len(codigo_materia_nota)):
            if codigo_materia_nota[j] == codigo_materias[i]:
                nota += notas[j]
                cantidad += 1
        if cantidad > 0:
            promedio = nota / cantidad
            print(f"El promedio de {lista_materias[i]} es {promedio:.1f}")
        else:
            print(f"No hay notas para {lista_materias[i]} (código {codigo_materias[i]})")
        
        
def nota_mayor(codigo_materia_nota,codigo_estudiante_nota,estudiantes,notas):
    contador=0
    while contador<(len(codigo_materias)):
        cd_materia1= codigo_materias[contador]
        contador+=1
        notas1=[]
        for i in range(len(codigo_materia_nota)):
         var=codigo_materia_nota[i]
         if var==cd_materia1:
             notas1.append(notas[i])
        maxima=max(notas1)
        pos_n= notas.index(maxima)
        pos_ma= codigo_materia_nota [pos_n]
        pos_ma1= codigo_materias.index(pos_ma)
        pos_e=codigo_estudiante_nota[pos_n]
        pos_e1= codigo_estudiantes.index(pos_e)
        
        print(f"{lista_materias[pos_ma1]} : {estudiantes[pos_e1]} {max(notas1)}")

        
def nota_menor(codigo_materia_nota,codigo_estudiante_nota,estudiantes,notas):
    contador=0
    while contador<(len(codigo_materias)):
        cd_materia1= codigo_materias[contador]
        contador+=1
        notas1=[]
        for i in range(len(codigo_materia_nota)):
         var=codigo_materia_nota[i]
         if var==cd_materia1:
             notas1.append(notas[i])
        maxima=min(notas1)
        pos_n= notas.index(maxima)
        pos_ma= codigo_materia_nota [pos_n]
        pos_ma1= codigo_materias.index(pos_ma)
        pos_e=codigo_estudiante_nota[pos_n]
        pos_e1= codigo_estudiantes.index(pos_e)
        
        print(f"{lista_materias[pos_ma1]} : {estudiantes[pos_e1]} {min(notas1)}")
opcion=0 
opcion1=0
while opcion!=5:
 menu_principal()
 opcion= int(input("Digite opcion: "))
 
 if opcion==1:
     while opcion1!=6:
      menu_crud_estudiantes()
      opcion1= int(input("Digite opcion: "))
      if opcion1==1:
          opcion1_crud_ingresar(estudiantes,codigo_estudiantes,lista_tipos[0])
      elif opcion1==2:
          opcion2_crud_actualizar(estudiantes,codigo_estudiantes,lista_tipos[0])
      elif opcion1==3:
          opcion3_crud_borrar(estudiantes,codigo_estudiantes,lista_tipos[0])
      elif opcion1==4:
         opcion4_crud_listar(estudiantes,codigo_estudiantes,lista_tipos[0])
      elif opcion1==5:
          opcion5_crud_buscar(estudiantes,codigo_estudiantes,lista_tipos[0])
 elif opcion==2:
     while True:
         menu_crud_materia()
         opcion2=int (input("Digite opcion: "))    
         if opcion2==1:
             opcion1_crud_ingresar(lista_materias,codigo_materias,lista_tipos[1])
         elif opcion2==2:
             opcion2_crud_actualizar(lista_materias,codigo_materias,lista_tipos[1])
         elif opcion2==3:
             opcion3_crud_borrar(lista_materias,codigo_materias,lista_tipos[1])
         elif opcion2==4:
             opcion4_crud_listar(lista_materias,codigo_materias,lista_tipos[1])
         elif opcion2==5:
             opcion5_crud_buscar(lista_materias,codigo_materias,lista_tipos[1])
         elif opcion2==6:
             break
 elif opcion==3:
     while True:
         menu_crud_notas()
         opcion3=int(input("Digite opcion: "))
         if opcion3==1:
             opcion1_ingresar_nota(notas,codigo_materias,codigo_materia_nota,codigo_estudiantes,codigo_estudiante_nota)
         if opcion3==2:
             opcion2_crud_actualizar_nota(codigo_materia_nota,codigo_estudiante_nota,notas)
         if opcion3==3:
             eliminar_nota(codigo_materia_nota,codigo_materias,lista_materias,codigo_estudiante_nota,codigo_estudiantes,notas)
         if opcion3==4:
             lista_notas(codigo_materia_nota,lista_materias,codigo_estudiante_nota,codigo_estudiantes,estudiantes,notas)   
         if opcion3==5:
             buscar_nota(codigo_materias,lista_materias,codigo_estudiante_nota,codigo_estudiantes,notas)
         if opcion3==6:
             break
 elif opcion==4:
     while True:
         menu_estadistico ()
         opcion4=int(input("Digite opcion: "))
         if opcion4==1:
             notas_codigo_estadisticas(codigo_materias,lista_materias,codigo_estudiante_nota,codigo_estudiantes,notas)
         elif opcion4==2:
             promedio_materia(codigo_materias,lista_materias,notas)
         elif opcion4==3:
             nota_mayor(codigo_materia_nota,codigo_estudiante_nota,estudiantes,notas)
         elif opcion4==4:
             nota_menor(codigo_materia_nota,codigo_estudiante_nota,estudiantes,notas)
         elif opcion4==5:
             break
                     
                
print("programa finalizado")
    