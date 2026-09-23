def pedir_golosina(golosinas, empleados, golosinas_pedidas):
    legajo = int(input("Ingrese su legajo: "))
    if legajo not in empleados:
        print("Usted no es un empleado de la empresa")
        return

    print(f"Bienvenido/a {empleados[legajo]}")
    pedir = True
    while pedir:
        codigo = int(input("Ingrese el código de la golosina que desea: "))
        encontrada = False
        
        for g in golosinas:
            if g[0] == codigo:
                encontrada = True
                if g[2] <= 0:
                    accion = input(f"Lo sentimos la golosina {g[1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina: ")
                    if accion.lower() == "salir":
                        pedir = False
                else:
                    g[2] -= 1
                    pedir = False
                    
                   
                    ya_registrada = False
                    for gp in golosinas_pedidas:
                        if gp[0] == codigo:
                            gp[2] += 1
                            ya_registrada = True
                            break
                    if not ya_registrada:
                        golosinas_pedidas.append([codigo, g[1], 1])
                    
                    print(f"¡Disfrute su {g[1]}!")
                break
        
        if not encontrada:
            print("El código ingresado no existe.")


def mostrar_golosinas(golosinas):
    print("\n--- STOCK ACTUAL DE GOLOSINAS ---")
    for g in golosinas:
        print(f"Código: {g[0]:2d} | Golosina: {g[1]:20s} | Stock: {g[2]}")


def rellenar_golosinas(golosinas, claves_tecnico):
    print("\n--- RECARGA DE TÉCNICO ---")
    c1 = input("Paso 1 - Ingrese la primera clave: ")
    c2 = input("Paso 2 - Ingrese la segunda clave: ")
    c3 = input("Paso 3 - Ingrese la tercera clave: ")
    
    if (c1, c2, c3) == claves_tecnico:
        cod_recarga = int(input("Ingrese el código de la golosina a recargar: "))
        encontrada = False
        for g in golosinas:
            if g[0] == cod_recarga:
                encontrada = True
                cantidad = int(input(f"Ingresá la cantidad de {g[1]} a recargar (mayor a 0): "))
                if cantidad > 0:
                    g[2] += cantidad
                    print(f"Stock de {g[1]} actualizado a {g[2]} unidades.")
                else:
                    print("La cantidad a recargar debe ser mayor a cero.")
                break
        if not encontrada:
            print("Código de golosina no existente.")
    else:
        print("No tiene permiso para ejecutar la función de recarga")



golosinas = [
    [1, "KitKat", 20], [2, "Chicles", 50], [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10], [5, "Chetoos", 10], [6, "Twix", 10],
    [7, "M&M'S", 10], [8, "Papas Lays", 2], [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15], [11, "Lata Coca", 20], [12, "Chitos", 10]
]

empleados = {
    1100: "José Alonso", 1200: "Federico Pacheco",
    1300: "Nelson Pereira", 1400: "Osvaldo Tejada", 1500: "Gastón Garcia"
}

clavesTecnico = ("admin", "CCCDDD", "2020")
golosinasPedidas = []

opcion = ""
while opcion != "4":
    print("\n--- MENÚ MÁQUINA DE GOLOSINAS ---")
    print("1. Pedir golosina")
    print("2. Mostrar golosinas")
    print("3. Rellenar golosinas")
    print("4. Apagar máquina")
    opcion = input("Seleccione una opción: ").lower()

    if opcion == "1":
        pedir_golosina(golosinas, empleados, golosinasPedidas)
    elif opcion == "2":
        mostrar_golosinas(golosinas)
    elif opcion == "3":
        rellenar_golosinas(golosinas, clavesTecnico)
    elif opcion == "4":
        print("\n--- APAGANDO MÁQUINA ---")
        total_pedidas = sum(gp[2] for gp in golosinasPedidas)
        for gp in golosinasPedidas:
            print(f"Código: {gp[0]} | Golosina: {gp[1]} | Cantidad Total Pedida: {gp[2]}")
        print(f"\nTotal general de golosinas entregadas: {total_pedidas}")
