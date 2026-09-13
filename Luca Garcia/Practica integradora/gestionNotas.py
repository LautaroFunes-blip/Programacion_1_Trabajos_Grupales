alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

materias_base = [
    ["Ciencias", 0.0, 0.0, 0.0],
    ["Historia", 0.0, 0.0, 0.0],
    ["Geografia", 0.0, 0.0, 0.0],
    ["Matematicas", 0.0, 0.0, 0.0],
    ["Fisica", 0.0, 0.0, 0.0]
]


notasFinales = []


for legajo, nombre_alumno in alumnos.items():
    print(f"\n==========================================")
    print(f"Alumno: {nombre_alumno} (Legajo: {legajo})")
    print(f"==========================================")
    

    materias_alumno = [f[:] for f in materias_base]
    
    suma_promedios_materias = 0.0
    materia_mas_alta = ""
    nota_mas_alta = -1.0
    

    for m in materias_alumno:
        print(f"\nIngrese las notas para la materia {m[0]}:")
        

        nota1 = -1.0
        while nota1 < 0 or nota1 > 10:
            nota1 = float(input("  Nota 1 (0 a 10): "))
            if nota1 < 0 or nota1 > 10:
                print("  [Error] La nota debe estar entre 0 y 10.")
        
        nota2 = -1.0
        while nota2 < 0 or nota2 > 10:
            nota2 = float(input("  Nota 2 (0 a 10): "))
            if nota2 < 0 or nota2 > 10:
                print("  [Error] La nota debe estar entre 0 y 10.")
        

        promedio_materia = (nota1 + nota2) / 2
        m[1] = nota1
        m[2] = nota2
        m[3] = promedio_materia
        
        print(f"  Nota Final en {m[0]}: {promedio_materia:.2f}")
        
       
        suma_promedios_materias += promedio_materia
        
       
        if promedio_materia > nota_mas_alta:
            nota_mas_alta = promedio_materia
            materia_mas_alta = m[0]
            

    print(f"\n--- Resumen de materias de {nombre_alumno} ---")
    for m in materias_alumno:
        print(f"Materia: {m[0]:12s} | Nota 1: {m[1]:.1f} | Nota 2: {m[2]:.1f} | Promedio: {m[3]:.2f}")
        
    print(f"\n-> La materia con la calificación más alta fue: {materia_mas_alta} ({nota_mas_alta:.2f})")
    

    promedio_general = suma_promedios_materias / len(materias_alumno)
    notasFinales.append([nombre_alumno, promedio_general])


print("\n==========================================")
print("--- RESUMEN FINAL Y MEJOR PROMEDIO ---")
print("==========================================")

mejor_alumno = ""
mejor_promedio_general = -1.0

for nf in notasFinales:
    print(f"Estudiante: {nf[0]:22s} | Promedio General: {nf[1]:.2f}")
    if nf[1] > mejor_promedio_general:
        mejor_promedio_general = nf[1]
        mejor_alumno = nf[0]

print(f"\n El estudiante con el mejor promedio general de la institución es: {mejor_alumno} con {mejor_promedio_general:.2f}")