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