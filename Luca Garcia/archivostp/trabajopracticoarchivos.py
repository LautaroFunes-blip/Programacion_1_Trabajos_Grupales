# ==============================================================================
# FUNCIÓN 1: Leer alumnos desde el archivo
# ==============================================================================
def leer_alumnos(nombre_archivo="alumnos.txt"):
    """
    Asegura la existencia del archivo abre en modo 'a' y luego lo lee en 'r'.
    Devuelve la lista de alumnos y un diccionario con clave = legajo.
    """
    alumnos_lista = []
    alumnos_dict = {}

    try:
        # Modo 'a' crea el archivo si no existe, y si existe no borra nada
        with open(nombre_archivo, "a", encoding="utf-8") as f:
            pass

        # Leemos el contenido
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue  # Omitir líneas vacías

                datos = linea_limpia.split(";")
                if len(datos) == 4:
                    nombre = datos[0].strip()
                    apellido = datos[1].strip()
                    legajo = datos[2].strip()
                    
                    try:
                        nota = float(datos[3].strip())
                    except ValueError:
                        continue  # Omitir si la nota guardada no es un número válido

                    alumno = {
                        "nombre": nombre,
                        "apellido": apellido,
                        "legajo": legajo,
                        "nota": nota
                    }
                    
                    alumnos_lista.append(alumno)
                    alumnos_dict[legajo] = alumno

    except IOError as e:
        print(f"Error al acceder al archivo {nombre_archivo}: {e}")

    return alumnos_lista, alumnos_dict


# ==============================================================================
# FUNCIÓN 2: Validar si existe el alumno
# ==============================================================================
def validar_existe_alumno(legajo, alumnos_dict):
    """
    Verifica si el legajo ingresado ya se encuentra registrado en el diccionario.
    """
    return legajo in alumnos_dict


# ==============================================================================
# FUNCIÓN 3: Agregar un nuevo alumno
# ==============================================================================
def agregar_alumno(alumnos_lista, alumnos_dict, nombre_archivo="alumnos.txt"):
    """
    Pide datos por teclado validándolos. Si hay un error de ingreso,
    vuelve a pedir el dato individualmente sin volver al menú principal.
    """
    print("\n--- Carga de Nuevo Alumno ---")

    # 1. Validar Nombre (Solo letras)
    while True:
        nombre = input("Ingrese el Nombre: ").strip()
        if nombre.replace(" ", "").isalpha():
            break
        print("Error: El nombre debe contener únicamente letras.")

    # 2. Validar Apellido (Solo letras)
    while True:
        apellido = input("Ingrese el Apellido: ").strip()
        if apellido.replace(" ", "").isalpha():
            break
        print("Error: El apellido debe contener únicamente letras.")

    # 3. Validar Legajo (5 dígitos y no existente)
    while True:
        legajo = input("Ingrese el Legajo (5 dígitos): ").strip()
        if not (legajo.isdigit() and len(legajo) == 5):
            print("Error: El legajo debe ser un número entero de exactamente 5 dígitos.")
            continue
        
        # Validar si ya existe en el diccionario
        if validar_existe_alumno(legajo, alumnos_dict):
            print(f"El legajo {legajo} ya existe en el archivo {nombre_archivo}, no se permite su escritura.")
            return  # Retorna al menú al detectar duplicado
        
        break

    # 4. Validar Nota Promedio (Número float entre 1 y 10)
    while True:
        try:
            nota_input = input("Ingrese la Nota Promedio (1 a 10): ").strip()
            nota = float(nota_input)
            if 1 <= nota <= 10:
                break
            else:
                print("Error: La nota debe ser un número entre 1 y 10.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico (no se admiten letras).")

    # Guardar en el archivo usando modo Append ('a')
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as f:
            f.write(f"{nombre};{apellido};{legajo};{nota}\n")
        
        # Actualizar las estructuras en memoria
        nuevo_alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "legajo": legajo,
            "nota": nota
        }
        alumnos_lista.append(nuevo_alumno)
        alumnos_dict[legajo] = nuevo_alumno
        
        print("¡Alumno registrado y guardado con éxito!")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")


# ==============================================================================
# FUNCIÓN 4: Guardar y mostrar aprobados
# ==============================================================================
def guardar_aprobados(alumnos_lista, archivo_salida="aprobados.txt"):
    """
    Genera aprobados.txt con los alumnos aprobados (nota >= 6) y lo muestra.
    """
    try:
        # Filtrar alumnos con nota mayor o igual a 6
        aprobados = [a for a in alumnos_lista if a["nota"] >= 6]
        
        with open(archivo_salida, "w", encoding="utf-8") as f:
            for a in aprobados:
                f.write(f"{a['nombre']};{a['apellido']};{a['legajo']};{a['nota']}\n")

        print(f"\n--- Archivo '{archivo_salida}' generado ---")
        if not aprobados:
            print("No hay alumnos aprobados registrados.")
        else:
            with open(archivo_salida, "r", encoding="utf-8") as f:
                print(f.read())

    except IOError as e:
        print(f"Error al gestionar el archivo de aprobados: {e}")


# ==============================================================================
# PROGRAMA PRINCIPAL / MENÚ CON WILE
# ==============================================================================
def main():
    # Carga inicial al comenzar el programa
    alumnos_lista, alumnos_dict = leer_alumnos()

    opcion = ""
    # Menú repetitivo hasta presionar 4 (Salir)
    while opcion != "4":
        print("\n" + "="*35)
        print("    MENÚ DE GESTIÓN DE ALUMNOS    ")
        print("="*35)
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar archivo de aprobados")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Lista de Alumnos Registrados ---")
            if not alumnos_lista:
                print("No hay alumnos cargados.")
            else:
                for a in alumnos_lista:
                    print(f"Legajo: {a['legajo']} | Nombre: {a['nombre']} {a['apellido']} | Nota Promedio: {a['nota']}")

        elif opcion == "2":
            agregar_alumno(alumnos_lista, alumnos_dict)

        elif opcion == "3":
            guardar_aprobados(alumnos_lista)

        elif opcion == "4":
            print("Saliendo del programa...")

        else:
            print("Opción inválida. Ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()