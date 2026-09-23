### Practica B
# ==========================================
# ESTRUCTURAS DE DATOS INICIALES
# ==========================================

# 1. Diccionario de alumnos: Legajo -> Apellido y Nombre
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# 3. Lista final para guardar [Nombre Alumno, Promedio General]
notasFinales = []


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def solicitar_nota(mensaje):
    """Solicita una nota por teclado, valida que sea un número y que esté en el rango [0, 10]."""
    while True:
        try:
            nota = float(input(mensaje))
            # Validar rango entre 0 y 10
            if 0 <= nota <= 10:
                return nota
            else:
                print("Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            # Captura si el usuario ingresó letras o caracteres no válidos
            print("Error: Debe ingresar un número.")


# ==========================================
# PROGRAMA PRINCIPAL / PROCESAMIENTO
# ==========================================

def gestionar_notas():
    # Iterar el diccionario de alumnos
    for legajo, nombre_alumno in alumnos.items():
        print("\n" + "=" * 40)
        print(f"Alumno: {nombre_alumno} (Legajo: {legajo})")
        print("=" * 40)
        
        # 2. Lista de materias para cada alumno
        # Columnas: [Materia, Nota 1, Nota 2, Nota Final]
        materias = [
            ["Ciencias", 0.0, 0.0, 0.0],
            ["Historia", 0.0, 0.0, 0.0],
            ["Geografia", 0.0, 0.0, 0.0],
            ["Matematicas", 0.0, 0.0, 0.0],
            ["Fisica", 0.0, 0.0, 0.0]
        ]
        
        suma_promedios_materias = 0.0
        
        # Cargar notas para cada materia
        for m in materias:
            print(f"\nIngrese las notas para la materia {m[0]}")
            n1 = solicitar_nota("Nota 1: ")
            n2 = solicitar_nota("Nota 2: ")
            
            promedio_materia = (n1 + n2) / 2
            
            # Asignar a la estructura de la materia
            m[1] = n1
            m[2] = n2
            m[3] = promedio_materia
            
            print(f"Nota Final en {m[0]}: {promedio_materia:.2f}")
            
            # Acumular para el promedio general del alumno
            suma_promedios_materias += promedio_materia
        
        # Mostrar por pantalla la lista materias completa cargada
        print(f"\n--- Resumen de materias de {nombre_alumno} ---")
        print("Materia       | Nota 1 | Nota 2 | Nota Final")
        print("-" * 45)
        for m in materias:
            print(f"{m[0]:<13} | {m[1]:<6} | {m[2]:<6} | {m[3]:.2f}")
            
        # Determinar la materia con la calificación más alta
        materia_max = materias[0]
        for m in materias:
            if m[3] > materia_max[3]:
                materia_max = m
                
        print(f"\nLa materia con la calificación más alta fue '{materia_max[0]}' con un promedio de {materia_max[3]:.2f}")
        
        # Calcular promedio general del alumno
        promedio_general = suma_promedios_materias / len(materias)
        
        # Asignar a la lista de notasFinales
        notasFinales.append([nombre_alumno, promedio_general])

    # ==========================================
    # RESULTADOS FINALES GLOBALES
    # ==========================================
    print("\n" + "=" * 50)
    print("RESUMEN DE NOTAS FINALES DE TODOS LOS ALUMNOS")
    print("=" * 50)
    for registro in notasFinales:
        print(f"Alumno: {registro[0]:<22} | Promedio General: {registro[1]:.2f}")
        
    # Determinar el alumno con el mejor promedio general
    mejor_alumno = notasFinales[0]
    for registro in notasFinales:
        if registro[1] > mejor_alumno[1]:
            mejor_alumno = registro
            
    print("-" * 50)
    print(f"¡El alumno con el mejor promedio general es {mejor_alumno[0]} con {mejor_alumno[1]:.2f}!")


# Ejecutar programa B
gestionar_notas()