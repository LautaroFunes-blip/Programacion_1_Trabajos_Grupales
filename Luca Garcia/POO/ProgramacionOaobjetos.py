class Celda:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregar_celda(self, celda: Celda):
        self.celdasMatriz.append(celda)

    def existe_celda(self, fila: int, columna: int) -> bool:
        for c in self.celdasMatriz:
            if c.fila == fila and c.columna == columna:
                return True
        return False

    def obtener_valor(self, fila: int, columna: int) -> str:
        for c in self.celdasMatriz:
            if c.fila == fila and c.columna == columna:
                return c.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"


# PROGRAMA PRINCIPAL
matriz = Matriz()

while True:
    valor = input("Ingrese el valor para la celda (o 'FIN' para terminar): ")
    if valor.upper() == "FIN":
        break

    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))

    if matriz.existe_celda(fila, columna):
        print("¡Error! La celda en esa posición ya ha sido cargada anteriormente.")
    else:
        nueva_celda = Celda(fila, columna, valor)
        matriz.agregar_celda(nueva_celda)
        print("Celda guardada con éxito.")

# Mostrar celdas cargadas
print("\n--- CELDAS CARGADAS ---")
for c in matriz.celdasMatriz:
    print(f"Fila: {c.fila} | Columna: {c.columna} | Valor: {c.valor}")

# Probar la búsqueda
print("\n--- BÚSQUEDA DE CELDA ---")
f_buscar = int(input("Ingrese fila a buscar: "))
c_buscar = int(input("Ingrese columna a buscar: "))
print("Resultado:", matriz.obtener_valor(f_buscar, c_buscar))

#Actividad 2

# Archivo: nota.py
class Nota:
    def __init__(self, catedra: str, notaExamen: float):
        self.catedra = catedra
        self.notaExamen = notaExamen

# Archivo: alumno.py
class Alumno:
    def __init__(self, nombreCompleto: str, legajo: int):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, nota: Nota):
        self.notas.append(nota)

    def calcular_promedio(self) -> float:
        if not self.notas:
            return 0.0
        total = sum(n.notaExamen for n in self.notas)
        return total / len(self.notas)

# Archivo: carga_notas.py (Main)
class CargaNotas:
    @staticmethod
    def main():
        alumnos = []
        
        # Bucle para alumnos
        mientras_alumnos = True
        while mientras_alumnos:
            print("\n--- INGRESE DATOS DEL ALUMNO ---")
            nombre = input("Ingrese Nombre Completo: ")
            legajo = int(input("Ingrese Legajo: "))
            
            alumno = Alumno(nombre, legajo)
            
            # Bucle para notas
            mientras_notas = True
            while mientras_notas:
                catedra = input("Ingrese Nombre Cátedra: ")
                nota_val = float(input("Ingrese Nota Examen: "))
                
                alumno.agregar_nota(Nota(catedra, nota_val))
                
                resp_nota = input("¿Desea salir de la carga de notas? (SI/NO): ")
                if resp_nota.upper() == "SI":
                    mientras_notas = False
            
            alumnos.append(alumno)
            
            resp_alumno = input("¿Desea salir de la carga de alumnos? (SI/NO): ")
            if resp_alumno.upper() == "SI":
                mientras_alumnos = False

        # Mostrar resultados
        print("\n=== RESUMEN DE ALUMNOS Y NOTAS ===")
        for a in alumnos:
            print(f"\nAlumno: {a.nombreCompleto} (Legajo: {a.legajo})")
            for n in a.notas:
                print(f"  - Cátedra: {n.catedra} | Nota: {n.notaExamen}")
            print(f"  El promedio del alumno es: {a.calcular_promedio():.2f}")

if __name__ == "__main__":
    CargaNotas.main()

    #Ejercicio 3 
    # Archivo: ingrediente.py
class Ingrediente:
    def __init__(self, nombre: str, cantidad: float, unidadMedida: str):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidadMedida = unidadMedida

# Archivo: plato.py
class Plato:
    def __init__(self, nombreCompleto: str, precio: float, esBebida: bool):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)

# Archivo: menu_restaurant.py (Main)
class MenuRestaurant:
    @staticmethod
    def main():
        platosMenu = []
        
        mientras_platos = True
        while mientras_platos:
            print("\n--- NUEVO PLATO ---")
            
            # 1. Validar nombre del plato (que no quede vacío)
            while True:
                nombre = input("Nombre del plato/bebida: ").strip()
                if nombre:
                    break
                print("Error: El nombre no puede estar vacío. Reintente.")

            # 2. Validar precio (numérico y mayor a 0)
            while True:
                try:
                    precio = float(input("Precio: "))
                    if precio > 0:
                        break
                    print("Error: El precio debe ser un número positivo.")
                except ValueError:
                    print("Error: Debe ingresar un valor numérico válido para el precio.")

            # 3. Validar si es bebida (SI/NO)
            while True:
                es_bebida_str = input("¿Es bebida? (SI/NO): ").strip().upper()
                if es_bebida_str in ["SI", "NO"]:
                    es_bebida = (es_bebida_str == "SI")
                    break
                print("Error: Responda únicamente 'SI' o 'NO'.")

            plato = Plato(nombre, precio, es_bebida)
            
            # Carga de ingredientes si no es bebida
            if not es_bebida:
                print("\nCarga de ingredientes (Mínimo 1):")
                mientras_ingredientes = True
                while mientras_ingredientes:
                    # Validar nombre del ingrediente
                    while True:
                        nom_ing = input("  Nombre ingrediente: ").strip()
                        if nom_ing:
                            break
                        print("  Error: El nombre del ingrediente no puede estar vacío.")

                    # Validar cantidad del ingrediente (Evita el error de la foto)
                    while True:
                        try:
                            cant_ing = float(input("  Cantidad: "))
                            if cant_ing > 0:
                                break
                            print("  Error: La cantidad debe ser mayor a 0.")
                        except ValueError:
                            print("  Error: Debe ingresar un valor numérico para la cantidad (ej: 100, 1.5).")

                    # Validar unidad de medida
                    while True:
                        um_ing = input("  Unidad de Medida (ej: gramos, ml, unidades): ").strip()
                        if um_ing:
                            break
                        print("  Error: La unidad de medida no puede estar vacía.")

                    plato.agregar_ingrediente(Ingrediente(nom_ing, cant_ing, um_ing))
                    
                    # Confirmar si desea finalizar los ingredientes
                    while True:
                        resp = input("  ¿Desea finalizar la carga de ingredientes de este plato? (SI/NO): ").strip().upper()
                        if resp in ["SI", "NO"]:
                            if resp == "SI":
                                mientras_ingredientes = False
                            break
                        print("  Error: Responda 'SI' o 'NO'.")

            platosMenu.append(plato)
            
            # Confirmar si desea finalizar la carga de platos
            while True:
                resp_p = input("\n¿Desea finalizar la carga de todos los platos? (SI/NO): ").strip().upper()
                if resp_p in ["SI", "NO"]:
                    if resp_p == "SI":
                        mientras_platos = False
                    break
                print("Error: Responda 'SI' o 'NO'.")

        # Mostrar Menú
        print("\n=== MENÚ DEL RESTAURANT ===")
        for p in platosMenu:
            print(f"\n{p.nombreCompleto}")
            print(f"Precio: $ {p.precio:.2f}")
            if not p.esBebida:
                print("Ingredientes:")
                print("Nombre | Cantidad | Unidad de Medida")
                for ing in p.ingredientes:
                    print(f"{ing.nombre} | {ing.cantidad} | {ing.unidadMedida}")

if __name__ == "__main__":
    MenuRestaurant.main()

#Ejercicio 4
# Archivo: componente_cpu.py
class ComponenteCPU:
    def __init__(self, componente: str, marca: str, cantidad: int, precio: float):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def get_subtotal(self) -> float:
        return self.cantidad * self.precio

# Archivo: computadora.py
class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []

    def agregar_componente(self, componente: ComponenteCPU):
        self.componentes.append(componente)

    def calcular_costo_total(self) -> float:
        return sum(c.get_subtotal() for c in self.componentes)

    def calcular_precio_sugerido(self) -> float:
        costo = self.calcular_costo_total()
        if costo < 50000:
            return costo * 1.40
        else:
            return costo * 1.30

# Archivo: costo_computadora.py (Main)
class CostoComputadora:
    @staticmethod
    def main():
        continuar = "SI"
        while continuar.upper() == "SI":
            print("\n--- COTIZACIÓN DE COMPUTADORA ---")
            marca = input("Marca de la Computadora: ")
            modelo = input("Modelo de la Computadora: ")
            
            pc = Computadora(marca, modelo)
            
            mientras_comp = True
            while mientras_comp:
                comp = input("  Nombre del Componente (ej. RAM, Placa Madre): ")
                m_comp = input("  Marca del Componente: ")
                cant = int(input("  Cantidad: "))
                precio = float(input("  Precio por unidad: "))
                
                pc.agregar_componente(ComponenteCPU(comp, m_comp, cant, precio))
                
                resp = input("  ¿Desea agregar otro componente? (SI/NO): ")
                if resp.upper() == "NO":
                    mientras_comp = False

            # Imprimir Comprobante
            print(f"\nComputadora")
            print(f"Marca: {pc.marca}")
            print(f"Modelo: {pc.modelo}")
            print("Componentes:")
            print("Componente | Marca | Cantidad | Precio X Unidad | SubTotal")
            for c in pc.componentes:
                print(f"{c.componente} | {c.marca} | {c.cantidad} | {c.precio} | {c.get_subtotal()}")
            
            costo = pc.calcular_costo_total()
            sugerido = pc.calcular_precio_sugerido()
            print(f"Costo Total: {costo}")
            print(f"El precio sugerido de venta es: {sugerido}")
            
            continuar = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ")

if __name__ == "__main__":
    CostoComputadora.main()

#Ejercicio 5
# ==========================================
# 1. CLASE HABITACIÓN
# ==========================================
class Habitacion:
    def __init__(self, nombre: str, metrosCuadrados: float):
        self.nombre = nombre
        self.metrosCuadrados = metrosCuadrados


# ==========================================
# 2. CLASE VIVIENDA
# ==========================================
class Vivienda:
    def __init__(self, calle: str, numero: int, manzana: str, nroCasa: int, superficieTerreno: float):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []  # Lista de objetos Habitacion

    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    # Punto c) Cálculo de metros cubiertos con validación de excepción
    def getMetrosCuadradosCubiertos(self) -> float:
        total_cubierto = sum(h.metrosCuadrados for h in self.habitaciones)
        
        # Validación solicitada: No puede ser mayor que la superficie del terreno
        if total_cubierto > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")
        
        return total_cubierto


# ==========================================
# 3. CLASE BARRIO
# ==========================================
class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []  # Lista de objetos Vivienda

    def agregar_vivienda(self, vivienda: Vivienda):
        self.viviendas.append(vivienda)

    # Punto a) Superficie total de terreno del barrio
    def getSuperficieTotalTerreno(self) -> float:
        return sum(v.superficieTerreno for v in self.viviendas)

    # Punto b) Superficie total de terreno filtrada por manzana
    def getSuperficieTotalTerrenoXManzana(self, manzana: str) -> float:
        return sum(v.superficieTerreno for v in self.viviendas if v.manzana.upper() == manzana.upper())

    # Punto d) Superficie total cubierta del barrio (reutiliza el método de vivienda)
    def getSuperficieTotalCubierta(self) -> float:
        return sum(v.getMetrosCuadradosCubiertos() for v in self.viviendas)


# ==========================================
# 4. PROGRAMA DE PRUEBA (Punto e)
# ==========================================
if __name__ == "__main__":
    # Creamos el Barrio
    mi_barrio = Barrio("Barrio Los Alamos", "Constructora del Sur S.A.")

    # Creamos Vivienda 1 (Manzana A)
    vivienda1 = Vivienda("Calle Falsa", 123, "A", 1, 300.0)
    vivienda1.agregar_habitacion(Habitacion("Living", 30.0))
    vivienda1.agregar_habitacion(Habitacion("Cocina", 20.0))
    vivienda1.agregar_habitacion(Habitacion("Dormitorio", 25.0))

    # Creamos Vivienda 2 (Manzana B)
    vivienda2 = Vivienda("Av. Principal", 456, "B", 12, 250.0)
    vivienda2.agregar_habitacion(Habitacion("Comedor", 40.0))
    vivienda2.agregar_habitacion(Habitacion("Baño", 10.0))

    # Asociamos las viviendas al barrio
    mi_barrio.agregar_vivienda(vivienda1)
    mi_barrio.agregar_vivienda(vivienda2)

    # Mostramos los resultados de la ejecución de los métodos
    print(f"=== REPORTE DEL BARRIO: {mi_barrio.nombre} ===")
    print(f"Empresa Constructora: {mi_barrio.empresaConstructora}")
    print(f"a) Superficie Total Terreno del Barrio: {mi_barrio.getSuperficieTotalTerreno()} m²")
    print(f"b) Superficie Terreno Manzana 'A': {mi_barrio.getSuperficieTotalTerrenoXManzana('A')} m²")
    print(f"d) Superficie Total Cubierta del Barrio: {mi_barrio.getSuperficieTotalCubierta()} m²")
    
