import ValidadorFinanciero
"""esta primera funcion todavia no esta debugeada"""
def calcular_factura_final(
    monto_base: float,
    descuento: float = 0.0,
    envio_prioritario: float | None = None,
    impuesto: float = 21.0,
) -> float:
    monto_con_descuento=monto_base * (1-descuento/100)
    monto_con_impuesto=monto_con_descuento*(1+impuesto/100)
    factura_final=monto_con_impuesto
    if envio_prioritario is None:
        pass
    else:
        monto_con_envio_prioritario=monto_con_impuesto + envio_prioritario
        factura_final=monto_con_envio_prioritario
    return round(factura_final, 2)

"""lo ideal va a ser mantener separado el menu de eleccion y de input del resto de funcinoes
para que se vea mas limpio y podes organizar mejor todo ademas de facilitar cuando busquemos errores"""

class Validador_financiero:
    @staticmethod
    def es_cuit_valido(cuit:str) -> bool:
        cantidad_numeros=len(cuit)
        if cuit.isdigit() == True and cantidad_numeros == 11:
            return(True)
        else:
            return(False)
    @staticmethod
    def convertir_moneda(monto:float, tasa_cambio:float, comision:float=0.02) -> float:
        monto_total=monto*tasa_cambio
        comision_final=monto_total*comision
        conversion=monto_total-comision_final
        return(conversion)

"""la segunda funcion ya funcinoa correctamente en los casos solicitados dentro del archivo"""

class notificador:
    def enviar_recibo(self, cliente: str, total: float) -> None:
        print('funciona correctamente')

class procesar_pago:

    def __init__(self):
        self.notificacion=notificador()

    def procesar_transaccion(self, cliente: str, items: list[dict], descuento_cupon=0.0) -> float:
        total=0
        for productos in items:
            total = total + productos['precio']
        if descuento_cupon > 0:
            porcentaje_descuento=(total * descuento_cupon) / 100 
            total = total - porcentaje_descuento
        else:
            print('no hay descuento a calcular')
        self.notificacion.enviar_recibo(cliente, total)
        return total


"""tercera funcion terminada"""

def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    contador= 1
    reporte= 'MODULO' + ':' + modulo.upper() + '\n'
    for mensaje in mensajes:
        reporte= reporte + '[' + str(contador)+ '] ' + mensaje + '\n'
        contador += 1
    for clave in metadatos:
        valor = metadatos[clave]
        reporte = reporte + clave.upper() + ': ' + str(valor) + '\n'
    return reporte

class calculadora_fitness:
    @staticmethod
    def calculadora_imc(peso: float, altura: float):
        imc=peso/(altura)**2
        return imc

    @staticmethod
    def clasificador_nivel(imc: float):
        if imc < 18.5:
            estado='bajo peso'
        elif 18.5 < imc < 25.0:
            estado='normal'
        elif 25.0 <= imc: 
            estado='sobrepeso'
        return estado



class Atleta:
    def __init__(self, nombre, peso, altura):
        self.nombre=nombre
        self.peso=peso
        self.altura=altura


    def obtener_reporte(self, recomendacion=False, **metricas) -> str:
        imc = calculadora_fitness.calculadora_imc(self.peso, self.altura)
        nivel= calculadora_fitness.clasificador_nivel(imc)
        reporte = 'Nombre: ' + self.nombre + '\n' + 'IMC: ' + str(imc) + '\n' + 'Nivel: ' + nivel + '\n'

        for clave in metricas:
            valor = metricas[clave]
            reporte = reporte + clave.upper() + ': ' + str(valor) + '\n'

        if recomendacion == True:
            reporte = reporte + 'recomendacion: prueba'
        return reporte

"""//MANTENER SEPARADO EL BUCLE DE MENU DEL RESTO DE CODIGO//"""

numero_ejercicio=None
while True:
    numero_ejercicio=int(input('ingrese el numero del ejercicio que quiere ejecutar, o 0 para salir'))
    if numero_ejercicio == 0:
        print('adios')
        break
    elif numero_ejercicio == 1:
        monto_base=float(input('ingrese el monto a pagar'))
        descuento_s_n=input('se aplica un descuento?').capitalize()
        if descuento_s_n=='S' or descuento_s_n =='Si':
            descuento=float(input('ingrese el descuento a aplicar'))
        elif descuento_s_n == 'N' or descuento_s_n == 'No':
            descuento=0.0
            pass

        else:
            print('ingrese una opcion valida')
        envio_prioritario=input('ingrese si corresponde el envio prioritario, caso contrario deje este campo vacio')
        try:
            envio_prioritario=(float(envio_prioritario))
        except ValueError:
            envio_prioritario=None
            pass

        factura_final=calcular_factura_final(monto_base, descuento, envio_prioritario, impuesto=21.0)
        print(factura_final)

    elif numero_ejercicio == 2:
        while True:
            cuit=(input('ingrese el numero de cuit'))
            cuit_valido=Validador_financiero.es_cuit_valido(cuit)
            if cuit_valido == True:
                monto=float(input('ingrese la cantidad a cambiar: '))
                tasa_cambio=float(input('ignrese la tasa de cambio actual: '))
                conversion=Validador_financiero.convertir_moneda(monto, tasa_cambio, comision=0.02)
                print(conversion)
                break
            elif cuit_valido == False:
                print('ingrese un cuit valido')

    elif numero_ejercicio == 3:
        items= [{"nombre": "Teclado", "precio": 50.0}, {"nombre": "Mouse", "precio": 30.0}]
        hay_descuento=input('el cliente trae un cupon de descuento?').capitalize()
        if hay_descuento == 'S' or hay_descuento == 'Si':
            descuento_cupon=float(input('ingrese el valor del descuento actual'))
        elif hay_descuento== 'No' or hay_descuento == 'N':
            descuento_cupon=00.0
            pass
        else:
            print('ignrese una opcion valida')
        cliente=input('inrgese el nomrbe del cliente para facturacion').capitalize()
        procesar=procesar_pago()
        factura_final=procesar.procesar_transaccion(cliente, items, descuento_cupon)


    elif numero_ejercicio == 4:
        agregar=''
        mensajes=[]
        metadatos={}
        modulo=input('ingrese el modulo')
        while True:
            mensaje= input('ingrese un mensaje')
            if mensaje == '':
                break
            else:
                mensajes.append(mensaje)
        while True:
            metadato=input('ingrese la clave de metadatos')

            if metadato == '':
                break
            else:
                valor=input('ingrese el valor de los metadatos')
                metadatos[metadato] = valor

        reporte=generar_auditoria_sistema(modulo, *mensajes, **metadatos)
        print(reporte)

    elif numero_ejercicio == 5:
        nombre=input('ingrese su nomrbe').capitalize()
        peso=(float(input('ingrese su peso en kg')))
        altura=float(input('ingrese su altura'))

        atleta=Atleta(nombre, peso, altura)
        metricas={}
        while True:
            clave = input('ingrese una metrica extra o dejar vacio para continuar')
            if clave == '':
                break

            else:
                valor=input('ingrese el valor de la metrica')
                metricas[clave]=valor

        reporte=atleta.obtener_reporte(recomendacion=True, **metricas)
        print(reporte)
