alumnosList=[]
diccionarioAlumnos={}
def abrirCrear():
    try:
        with open('alumnos.txt', 'r', encoding='utf-8') as archivo:
            for alumnos in archivo:
                archivoMostrar=alumnos.strip()
                archivoMostrarFinal=archivoMostrar.split(';')
                print(f'Alumno:{archivoMostrarFinal[0],archivoMostrarFinal[1]} Nota Promedio:{archivoMostrarFinal[3]}')
                nombreAlumno=archivoMostrarFinal[0]
                apellidoAlumno=archivoMostrarFinal[1]
                legajoAlumno=int(archivoMostrarFinal[2])
                notaPromedio=float(archivoMostrarFinal[3])
                alumnosGuardar={'Nombre':nombreAlumno,'Apellido':apellidoAlumno, 'Legajo':legajoAlumno, 'Promedio':notaPromedio}
                alumnosList.append(alumnosGuardar)
                diccionarioAlumnos[legajoAlumno] = {'Legajo':legajoAlumno, 'Nombre':nombreAlumno, 'Apellido':apellidoAlumno, 'Promedio':notaPromedio}
            print(alumnosList)
            print(diccionarioAlumnos)


    except FileNotFoundError:
        with open('alumnos.txt', 'a', encoding='utf-8') as archivo:
            print('el archivo se creo correctamente')

def agregarAlumno(diccionarioAlumnos, alumnosList):
    with open('alumnos.txt', 'a', encoding='utf-8') as arhcivo:
        while True:
            nombreAlumno=input('ingrese el nombre del alumno').capitalize()
            apellidoAlumno=input('ingrese el apellido del alumno').capitalize()
            legajoAlumno=input('ingrese el legajo del alumno')
            if len(legajoAlumno)==5:
                notaAlumno=input('ingrese la nota del alumno')
                try:
                    legajoAlumno=int(legajoAlumno)
                    print('el legajo es correcto')
                    if legajoAlumno in diccionarioAlumnos:
                        print('el alumno ya esta en la lista')
                    else:
                        try:
                            notaAlumno=float(notaAlumno)
                            if 1 <= notaAlumno <= 10:
                                print('continue')
                                alumnosGuardar={'Nombre':nombreAlumno,'Apellido':apellidoAlumno,'Legajo':legajoAlumno,'Promedio':notaAlumno}
                                alumnosList.append(alumnosGuardar)
                                diccionarioAlumnos[legajoAlumno] = {'Legajo':legajoAlumno,'Nombre':nombreAlumno,'Apellido':apellidoAlumno,'Promedio':notaAlumno}
                                guardarArchivo=(f'{nombreAlumno};{apellidoAlumno};{legajoAlumno};{notaAlumno}\n')
                                arhcivo.write(guardarArchivo)
                                break
                            else:
                                print('ingrese una nota dentro del ragno valido')
                        except ValueError:
                            print('ingrese solo valores numericos')

                except ValueError:
                    print('ingrese un legajo valido de solo numeros')
            else:
                print('ingrese un legajo valido que contenga 5 digitos')

def aprobados(diccionarioAlumnos):
    with open('alumnosAprobados.txt', 'w', encoding='utf-8') as archivo:
        for notasALumnos in diccionarioAlumnos:
            datosAlumnos= diccionarioAlumnos[notasALumnos]
            if datosAlumnos['Promedio'] >= 6:
                guardarArchivo=(f'{datosAlumnos["Nombre"]};{datosAlumnos["Apellido"]};{datosAlumnos["Legajo"]};{datosAlumnos["Promedio"]}\n')
                archivo.write(guardarArchivo)

funcion=None
abrirCrear()
while True:
    funcion=input('ingrese el numero de la funcion que desea ejecutar \n 1=Ver Alumnos \n 2=Agregar Alumnos \n 3=Alumnos Aprobados \n 0=Salir')
    try:
        funcion=int(funcion)
        if funcion == 1:
            print(alumnosList)
        elif funcion == 2:
            agregarAlumno(diccionarioAlumnos, alumnosList)
        elif funcion == 3:
            aprobados(diccionarioAlumnos)
        elif funcion == 0:
            print('adios')
            break
        else:
            print('ingrese un valor valido dentro de las opciones')
    except ValueError:
        print('ingrese un valor numerico dentro de las opciones')
