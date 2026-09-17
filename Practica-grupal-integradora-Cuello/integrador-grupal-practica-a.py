### Practia A
# ==========================================
# ESTRUCTURAS DE DATOS INICIALES
# ==========================================

# Lista de 2 dimensiones: [Código, Denominación, Stock]
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

# Diccionario de empleados: Legajo -> Nombre
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

# Tupla con claves del técnico
clavesTecnico = ("admin", "CCCDDD", "2020")

# Historial de golosinas pedidas: [Código, Denominación, Cantidad Total]
golosinasPedidas = []


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def buscar_golosina(codigo):
    """Busca una golosina por su código y retorna su fila o None si no existe."""
    for golosina in golosinas:
        if golosina[0] == codigo:
            return golosina
    return None

def registrar_pedido(codigo, denominacion):
    """Registra o incrementa el pedido en la lista golosinasPedidas."""
    encontrado = False
    for pedido in golosinasPedidas:
        if pedido[0] == codigo:
            pedido[2] += 1
            encontrado = True
            break
    
    # Si la golosina no estaba registrada en el historial, agregamos una nueva fila
    if not encontrado:
        golosinasPedidas.append([codigo, denominacion, 1])


# ==========================================
# FUNCIONES DEL MENÚ
# ==========================================

def pedir_golosina():
    print("\n--- PEDIR GOLOSINA ---")
    legajo = int(input("Ingrese su número de legajo: "))
    
    # Validar empleado
    if legajo not in empleados:
        print("Usted no es un empleado de la empresa")
        return

    print(f"Bienvenido/a {empleados[legajo]}")
    
    # Bucle para pedir golosina
    bandera = True
    while bandera:
        entrada = input("Ingrese el código de la golosina (o 'salir'): ")
        
        if entrada.lower() == "salir":
            bandera = False
        else:
            codigo = int(entrada)
            golosina = buscar_golosina(codigo)
            
            if golosina is None:
                print("Código invalido. Intente nuevamente.")
            else:
                denominacion = golosina[1]
                stock = golosina[2]
                
                if stock > 0:
                    # Descontar stock
                    golosina[2] -= 1
                    # Registrar pedido
                    registrar_pedido(codigo, denominacion)
                    print(f"¡Disfrute su {denominacion}!")
                    bandera = False
                else:
                    print(f"Lo sentimos la golosina {denominacion} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")


def mostrar_golosinas():
    print("\n--- LISTA DE GOLOSINAS DISPONIBLES ---")
    print("Código | Golosina | Stock")
    print("-" * 35)
    for g in golosinas:
        print(f"{g[0]:<6} | {g[1]:<20} | {g[2]}")


def rellenar_golosinas():
    print("\n--- RELLENAR GOLOSINAS (TÉCNICO) ---")
    # Validación de contraseña en 3 pasos
    c1 = input("Ingrese clave 1: ")
    c2 = input("Ingrese clave 2: ")
    c3 = input("Ingrese clave 3: ")
    
    if (c1, c2, c3) == clavesTecnico:
        codigo = int(input("Ingrese el código de la golosina a recargar: "))
        golosina = buscar_golosina(codigo)
        
        if golosina is not None:
            cantidad = int(input("Ingrese la cantidad a recargar (mayor a 0): "))
            while cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                cantidad = int(input("Ingrese la cantidad a recargar: "))
            
            # Sumar al stock existente
            golosina[2] += cantidad
            print(f"Recarga exitosa. Nuevo stock de {golosina[1]}: {golosina[2]}")
        else:
            print("El código ingresado no existe.")
    else:
        print("No tiene permiso para ejecutar la función de recarga")


def apagar_maquina():
    print("\n--- APAGANDO MÁQUINA ---")
    print("Historial de golosinas pedidas:")
    print("Código | Golosina | Cantidad Total Pedida")
    print("-" * 45)
    
    total_acumulado = 0
    for pedido in golosinasPedidas:
        print(f"{pedido[0]:<6} | {pedido[1]:<20} | {pedido[2]}")
        total_acumulado += pedido[2]
        
    print("-" * 45)
    print(f"Total general de golosinas pedidas: {total_acumulado}")
    print("Programa finalizado.")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def menu_principal():
    ejecutando = True
    while ejecutando:
        print("\n=== MENÚ MÁQUINA DE GOLOSINAS ===")
        print("a. Pedir golosina")
        print("b. Mostrar golosinas")
        print("c. Rellenar golosinas")
        print("d. Apagar maquina")
        
        opcion = input("Seleccione una opción: ").lower()
        
        if opcion == 'a':
            pedir_golosina()
        elif opcion == 'b':
            mostrar_golosinas()
        elif opcion == 'c':
            rellenar_golosinas()
        elif opcion == 'd':
            apagar_maquina()
            ejecutando = False
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar programa A
menu_principal()  