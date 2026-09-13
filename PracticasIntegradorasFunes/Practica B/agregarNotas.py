def agregarNotas(alumnos, alumno, materias):
        for materia in materias:
            nota1=(input(f'ingrese la primera nota del alumno {alumnos[alumno]}, para la materia {materia}'))
            try:
                nota1=float(nota1)
                nota2=input(f'ingrese la segunda nota de {alumnos[alumno]}')
                try:
                    if 0<=nota1<=10:
                        nota2=float(nota2)
                        if 0<=nota2<=10:                        
                            notaFinal=(nota1+nota2)/2
                            materia.append(nota1)
                            materia.append(nota2)
                            materia.append(notaFinal)
                        else:
                            print('ingrese un valor dentro de rango')
                    else:
                        print('ingrese un valor dentro del rango')
                except ValueError:
                    print('ingrese solo valores numericos')
            except ValueError:
                print('ingrese solo valores numericos')

