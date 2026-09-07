## Ejercicio 1

def calcular_factura_final(monto_base: float, impuesto: float = 21.0,
                           descuento: float = 0.0,
                           envio_prioritario: float | None = None) -> float:

    # Primero aplicamos el descuento
    subtotal = monto_base * (1 - descuento / 100)

    # Después aplicamos el impuesto
    total = subtotal * (1 + impuesto / 100)

    # Si hay envío prioritario, lo sumamos
    if envio_prioritario is not None:
        total = total + envio_prioritario

    # Redondeamos el resultado a 2 decimales
    return round(total, 2)


# Prueba 1
print(calcular_factura_final(1000.0))

# Prueba 2
print(calcular_factura_final(1000.0, descuento=10.0))

# Prueba 3
print(calcular_factura_final(1000.0, impuesto=10.0,
                             descuento=5.0,
                             envio_prioritario=150.0))


## Ejercicio 2

class ValidadorFinanciero:

    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:

        # Verificamos que tenga exactamente 11 caracteres
        # y que todos sean números
        if len(cuit) == 11 and cuit.isdigit():
            return True
        else:
            return False

    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float,
                         comision: float = 0.02) -> float:

        # Convertimos el monto usando la tasa de cambio
        total = monto * tasa_cambio

        # Descontamos la comisión
        total = total * (1 - comision)

        # Redondeamos a 2 decimales
        return round(total, 2)


# Prueba 1
print(ValidadorFinanciero.es_cuit_valido("20384920194"))

# Prueba 2
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))

# Prueba 3
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05)) 


### Ejercicio 3


class Notificador:

    def enviar_recibo(self, cliente: str, total: float) -> None:

        # Mostramos el resumen del cobro
        print("----- RECIBO DE COMPRA -----")
        print("Cliente:", cliente)
        print("Total cobrado: $", total)
        print("----------------------------")


class ProcesadorPagos:

    def __init__(self, notificador=None):

        # Si no recibimos un notificador, creamos uno
        if notificador is None:
            self.notificador = Notificador()
        else:
            self.notificador = notificador

    def procesar_transaccion(self, cliente: str, items: list[dict],
                             descuento_cupon: float = 0.0) -> float:

        # Comenzamos el total en cero
        total = 0

        # Recorremos cada producto del carrito
        for item in items:
            total = total + item["precio"]

        # Aplicamos el descuento
        total = total * (1 - descuento_cupon / 100)

        # Le pedimos al notificador que envíe el recibo
        self.notificador.enviar_recibo(cliente, total)

        # Devolvemos el total
        return total


# Creamos el carrito
carrito = [
    {"nombre": "Teclado", "precio": 50.0},
    {"nombre": "Mouse", "precio": 30.0}
]

# Creamos el procesador
procesador = ProcesadorPagos()

# Procesamos la compra
procesador.procesar_transaccion(
    "Ana Gómez",
    carrito,
    descuento_cupon=10.0
)


## Ejercicio 4

def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:

    # Comenzamos el reporte
    reporte = "MÓDULO: " + modulo.upper() + "\n"

    # Agregamos los mensajes numerados
    reporte = reporte + "\nMENSAJES:\n"

    numero = 1

    for mensaje in mensajes:
        reporte = reporte + "[" + str(numero) + "] " + mensaje + "\n"
        numero = numero + 1

    # Agregamos los metadatos
    reporte = reporte + "\nMETADATOS:\n"

    for clave, valor in metadatos.items():
        reporte = reporte + clave.upper() + ": " + str(valor) + "\n"

    return reporte


# Prueba requerida
log = generar_auditoria_sistema(
    "AUTH",
    "Intento fallido",
    "Bloqueo de IP",
    usuario="admin",
    ip="192.168.1.10"
)

print(log)


### Ejercicio 5


class CalculadoraFitness:

    @staticmethod
    def calcular_imc(peso_kg: float, altura_m: float) -> float:

        # Calculamos el IMC
        imc = peso_kg / (altura_m ** 2)

        # Redondeamos a 2 decimales
        return round(imc, 2)

    @staticmethod
    def clasificar_nivel(imc: float) -> str:

        # Clasificamos el IMC según el valor
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25.0:
            return "Normal"
        else:
            return "Sobrepeso"


class Atleta:

    def __init__(self, nombre: str, peso: float, altura: float):

        # Guardamos los datos del atleta
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def obtener_reporte(self, incluir_recomendacion: bool = False,
                        **metricas_extra) -> str:

        # Calculamos el IMC usando la clase CalculadoraFitness
        imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)

        # Obtenemos la clasificación del IMC
        nivel = CalculadoraFitness.clasificar_nivel(imc)

        # Comenzamos a armar el reporte
        reporte = "----- REPORTE DEL ATLETA -----\n"
        reporte = reporte + "Nombre: " + self.nombre + "\n"
        reporte = reporte + "Peso: " + str(self.peso) + " kg\n"
        reporte = reporte + "Altura: " + str(self.altura) + " m\n"
        reporte = reporte + "IMC: " + str(imc) + "\n"
        reporte = reporte + "Nivel: " + nivel + "\n"

        # Agregamos las métricas extras
        if len(metricas_extra) > 0:
            reporte = reporte + "\nMétricas extra:\n"

            for clave, valor in metricas_extra.items():
                reporte = reporte + clave.upper() + ": " + str(valor) + "\n"

        # Agregamos una recomendación si se solicita
        if incluir_recomendacion:
            reporte = reporte + "\nRecomendación: Mantener una alimentación "
            reporte = reporte + "equilibrada y realizar actividad física regularmente.\n"

        return reporte


# Creamos un atleta
atleta = Atleta("Juan", 70.0, 1.68)

# Obtenemos el reporte
reporte = atleta.obtener_reporte(
    incluir_recomendacion=True,
    velocidad="10 km/h",
    entrenamiento="Fuerza"
)

print(reporte)