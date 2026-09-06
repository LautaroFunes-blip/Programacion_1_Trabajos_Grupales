#Ejercicio 1 
def calcular_factura_final(
    monto_base: float, 
    impuesto: float = 21.0, 
    descuento: float = 0.0, 
    envio_prioritario: float | None = None
) -> float:
    monto_con_descuento = monto_base * (1 - descuento / 100)
    
    subtotal = monto_con_descuento * (1 + impuesto / 100)
    

    if envio_prioritario is not None:
        subtotal += envio_prioritario
    return round(subtotal, 2)

print(calcular_factura_final(1000.0))  
print(calcular_factura_final(1000.0, descuento=10.0))  
print(calcular_factura_final(1000.0, impuesto=10.0, descuento=5.0, envio_prioritario=150.0)) 

#Ejrecicio 2 
class ValidadorFinanciero:
    
    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        return cuit.isdigit() and len(cuit) == 11

    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float, comision: float = 0.02) -> float:
        monto_convertido = monto * tasa_cambio
        

        monto_final = monto_convertido * (1 - comision)
        
        return monto_final

print(ValidadorFinanciero.es_cuit_valido("20384920194"))   
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4")) 
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05)) 

#Ejercicio 3
class Notificador:
    def enviar_recibo(self, cliente: str, total: float) -> None:
        print(f"[RECIBO] Cliente: {cliente} | Total Cobrado: ${total:.2f}")


class ProcesadorPagos:
    def __init__(self, notificador: Notificador | None = None):
        if notificador is None:
            self.notificador = Notificador()
        else:
            self.notificador = notificador

    def procesar_transaccion(self, cliente: str, items: list[dict], descuento_cupon: float = 0.0) -> float:
        total_acumulado = 0.0
        for item in items:
            total_acumulado += item["precio"]

        total_final = total_acumulado * (1 - descuento_cupon / 100)
        self.notificador.enviar_recibo(cliente, total_final)
        
        return total_final

#Ejercicio 4
def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:

    reporte = [f"=== REPORTE DE AUDITORÍA: {modulo.upper()} ==="]
    
    reporte.append("MENSAJES:")
    for idx, mensaje in enumerate(mensajes, start=1):
        reporte.append(f"  [{idx}] {mensaje}")
        
    reporte.append("METADATOS:")
    for clave, valor in metadatos.items():
        reporte.append(f"  {clave.upper()}: {valor}")
    return "\n".join(reporte)


log = generar_auditoria_sistema(
    "AUTH", 
    "Intento fallido", 
    "Bloqueo de IP", 
    usuario="admin", 
    ip="192.168.1.10"
)
print(log)


#Ejercicio 5 
class CalculadoraFitness:
    
    @staticmethod
    def calcular_imc(peso_kg: float, altura_m: float) -> float:
        return peso_kg / (altura_m ** 2)

    @staticmethod
    def clasificar_nivel(imc: float) -> str:
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25.0:
            return "Normal"
        else:
            return "Sobrepeso"


class Atleta:
    def __init__(self, nombre: str, peso: float, altura: float):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def obtener_reporte(self, incluir_recomendacion: bool = False, **metricas_extra) -> str:
        imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        clasificacion = CalculadoraFitness.clasificar_nivel(imc)
        
        lineas = [
            f"Atleta: {self.nombre}",
            f"IMC: {imc:.2f} ({clasificacion})"
        ]
        
        if metricas_extra:
            lineas.append("Métricas Adicionales:")
            for clave, valor in metricas_extra.items():
                lineas.append(f"  - {clave.replace('_', ' ').capitalize()}: {valor}")
                
        if incluir_recomendacion:
            if clasificacion == "Normal":
                rec = "Mantener la rutina de entrenamiento actual."
            elif clasificacion == "Bajo peso":
                rec = "Aumentar la ingesta calórica y entrenamiento de fuerza."
            else:
                rec = "Incrementar trabajo aeróbico y ajustar plan nutricional."
            lineas.append(f"Recomendación: {rec}")
            
        return "\n".join(lineas)

atleta = Atleta("Marcos", 75.0, 1.75)
reporte = atleta.obtener_reporte(
    incluir_recomendacion=True, 
    frecuencia_cardiaca=65, 
    horas_sueño=8
)
print(reporte)