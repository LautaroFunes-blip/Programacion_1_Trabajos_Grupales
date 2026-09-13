"""practica B archivo de logica general"""
import agregarNotas


alumnos={60902:'Rodolfo Fernandez', 
        61654:'Luis Gomez',
        61852:'Andrea Pereira',
        61754:'Juan Cruz Gonzales'
}

notasFinales=[
    ['Rodolfo Fernandez'],
    ['Luis Gomez'],
    ['Andrea Pereira'],
    ['Juan Cruz Gonzales'],
]

for alumno in alumnos:
    materias=[
        ['ciencias'],
        ['Historia'],
        ['Geografia'],
        ['Matematicas'],
        ['Fisica'],
    ]
    notasFinalesTemporal=[]
    notaMaxima=[]
    notaMinima=[]
    notaAlta=None
    materiaAlta=None
    agregarNotas.agregarNotas(alumnos, alumno, materias)
    for materia in materias:
        notasFinalesTemporal.append(materia[3])
        if notaAlta is None or materia[3]>notaAlta:
            notaAlta= materia[3]
            materiaAlta=materia[0]

    mejorPromedio = None
    mejorAlumno = None

    for fila in notasFinales:
        if mejorPromedio is None or fila[1] > mejorPromedio:
            mejorPromedio = fila[1]
            mejorAlumno = fila[0]

    print(f'el alumno con el mejor promedio fue {mejorAlumno} con {mejorPromedio}')
    for notas in notasFinales:
        if notas[0] == alumnos[alumno]:
                notas.append(sum(notasFinalesTemporal)/5)
    notaMaxima.append(max(notasFinalesTemporal))
    notaMinima.append(min(notasFinalesTemporal))
    print(materias)
    print(f'nota mas alta del alumno {alumnos[alumno]} fue {notaMaxima}')
    print(f'nota mas baja del alumno {alumnos[alumno]} fue {notaMinima}')
    print(notasFinales)
    print(notaAlta)
    print(materiaAlta)