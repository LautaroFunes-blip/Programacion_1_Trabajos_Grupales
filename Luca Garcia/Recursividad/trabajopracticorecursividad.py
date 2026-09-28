# ==========================================
# 1. CLASES POO BASE
# ==========================================
class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []       # Lista de objetos de tipo Archivo
        self.subdirectorios = []  # Lista de objetos de tipo Directorio

# ==========================================
# 2. FUNCIONES RECURSIVAS DE LÓGICA
# ==========================================
def calcular_tamano_total(directorio: Directorio) -> int:
    """Calcula el tamaño total en bytes de forma recursiva."""
    total = sum(archivo.tamano_bytes for archivo in directorio.archivos)
    for subdirectorio in directorio.subdirectorios:
        total += calcular_tamano_total(subdirectorio)
    return total

def buscar_por_extension(directorio: Directorio, extension: str, ruta_actual: str = "") -> list[str]:
    """Busca archivos con una extensión determinada de forma recursiva."""
    if not ruta_actual:
        ruta_actual = directorio.nombre
        
    coincidencias = []
    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            coincidencias.append(f"{ruta_actual}/{archivo.nombre}")
            
    for subdirectorio in directorio.subdirectorios:
        nueva_ruta = f"{ruta_actual}/{subdirectorio.nombre}"
        coincidencias.extend(buscar_por_extension(subdirectorio, extension, nueva_ruta))
        
    return coincidencias

def limpiar_archivos_vacios(directorio: Directorio) -> int:
    """Elimina los archivos con tamaño 0 bytes de forma recursiva."""
    archivos_iniciales = len(directorio.archivos)
    directorio.archivos = [arch for arch in directorio.archivos if arch.tamano_bytes > 0]
    eliminados_locales = archivos_iniciales - len(directorio.archivos)
    
    eliminados_subdirectorios = 0
    for subdirectorio in directorio.subdirectorios:
        eliminados_subdirectorios += limpiar_archivos_vacios(subdirectorio)
        
    return eliminados_locales + eliminados_subdirectorios

# ==========================================
# 3. GENERACIÓN DEL ÁRBOL DE PRUEBA
# ==========================================
def crear_arbol_prueba() -> Directorio:
    """Construye la estructura de prueba original."""
    root = Directorio("root")
    
    root.archivos.append(Archivo("documento.pdf", 1500))
    root.archivos.append(Archivo("config.txt", 0))
    
    imagenes = Directorio("imagenes")
    imagenes.archivos.append(Archivo("foto1.png", 2000))
    imagenes.archivos.append(Archivo("foto2.png", 3500))
    root.subdirectorios.append(imagenes)
    
    proyectos = Directorio("proyectos")
    proyectos.archivos.append(Archivo("avance.pdf", 800))
    
    temp = Directorio("temp")
    temp.archivos.append(Archivo("log.txt", 0))
    
    proyectos.subdirectorios.append(temp)
    root.subdirectorios.append(proyectos)
    
    return root

# ==========================================
# 4. FUNCIONES DE LECTURA Y VALIDACIÓN LOCAL
# ==========================================
def pedir_opcion_menu() -> int:
    """Mantiene al usuario pidiendo la opción del menú si se equivoca."""
    while True:
        try:
            opcion = int(input("\nIngrese una opción (0-4): ").strip())
            if 0 <= opcion <= 4:
                return opcion
            else:
                print("  Error: Ingrese un número entre 0 y 4.")
        except ValueError:
            print("  Error: Entrada inválida. Debe ingresar un número entero.")

def sub_menu_busqueda(sistema_archivos: Directorio):
    """Sub-bucle: Se queda pidiendo la extensión sin volver al menú principal."""
    while True:
        ext = input("\nIngrese la extensión a buscar (ej: .pdf) o 'cancelar' para volver: ").strip().lower()
        
        if ext == 'cancelar' or ext == '0':
            print("↩  Cancelando búsqueda y volviendo al menú principal...")
            break
            
        if not ext:
            print("  Error: No ingresó nada. Intente nuevamente.")
            continue  
            
        if not ext.startswith("."):
            ext = "." + ext
            
        resultados = buscar_por_extension(sistema_archivos, ext)
        
        if resultados:
            print(f"\n Archivos encontrados para '{ext}':")
            for ruta in resultados:
                print(f"  • {ruta}")
        else:
            print(f"\n No se encontraron archivos con la extensión '{ext}'.")
        
        otra = input("\n¿Desea buscar otra extensión? (s/n): ").strip().lower()
        if otra not in ['s', 'si', 'sí']:
            break

def sub_menu_limpieza(sistema_archivos: Directorio):
    """Sub-bucle: Pide confirmación reintentando en la misma sub-opción si se equivoca."""
    while True:
        respuesta = input("\n¿Está seguro de eliminar los archivos de 0 bytes? (S/N): ").strip().upper()
        
        if respuesta in ['S', 'SI']:
            eliminados = limpiar_archivos_vacios(sistema_archivos)
            print(f"\n Limpieza completada. Se eliminaron {eliminados} archivos vacíos.")
            break
        elif respuesta in ['N', 'NO']:
            print(" Operación cancelada.")
            break
        else:
            print("  Opción no válida. Por favor, responda 'S' o 'N'.") 

# ==========================================
# 5. MENÚ PRINCIPAL
# ==========================================
def ejecutar_menu():
    sistema_archivos = crear_arbol_prueba()
    
    while True:
        print("\n" + "="*45)
        print("    SISTEMA DE GESTIÓN DE ARCHIVOS (RECURSIVO)")
        print("="*45)
        print("1. Calcular tamaño total del disco")
        print("2. Buscar archivos por extensión")
        print("3. Limpiar archivos vacíos (0 bytes)")
        print("4. Reiniciar árbol de prueba")
        print("0. Salir")
        print("="*45)
        
        opcion = pedir_opcion_menu()
        
        if opcion == 0:
            print("\nSaliendo del programa... ¡Hasta luego!")
            break
            
        elif opcion == 1:
            total = calcular_tamano_total(sistema_archivos)
            print(f"\n Tamaño total ocupado: {total} bytes")
            
        elif opcion == 2:
            sub_menu_busqueda(sistema_archivos)  # Entra al sub-bucle
            
        elif opcion == 3:
            sub_menu_limpieza(sistema_archivos)  # Entra al sub-bucle
            
        elif opcion == 4:
            sistema_archivos = crear_arbol_prueba()
            print("\n El árbol de archivos ha sido reiniciado a su estado inicial.")

if __name__ == "__main__":
    ejecutar_menu()