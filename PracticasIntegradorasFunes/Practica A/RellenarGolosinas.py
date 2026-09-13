def rellenarGolosinas(golosinas, clavesTecnico):
    clave1=input('ignrese la primera clave de tecnico')
    if clave1== clavesTecnico[0]:
        clave2=input('ingrese la segunta clade de tecnico')
        if clave2 == clavesTecnico[1]:
            clave3=input('ignrese la ultima clave')
            if clave3 == clavesTecnico[2]:
                print('bienvenido admin')
                golosinaRellenar=input('ingrese el numero correspondiente a la golosina que quiere rellenar')
                try:
                    golosinaRellenar=int(golosinaRellenar)
                    if 1<= golosinaRellenar <= len(golosinas):
                        indice=golosinaRellenar-1
                        stockActual=golosinas[indice][2]
                        nombreGolosina=golosinas[indice][1]
                        cantidadAgregar=input(f'ingrese la cantidad de {nombreGolosina}')
                        try:
                            cantidadAgregar=int(cantidadAgregar)
                            if cantidadAgregar > 0:
                                stockFinal=stockActual+cantidadAgregar
                                golosinas[indice][2]=stockFinal
                            else:
                                print('ingrese una cantidad mayor a cero (0)')
                        except ValueError:
                            print('ingrese una cantidad numerica')
                    else:
                        print('no existe una golosina con es numero asignado')
                except ValueError:
                    print('ingrese un valor valido para las golosinas a agregar')
            else:
                print('no tiene permiso para ejecutar la funcion de recarga')
        else:
            print('no tiene permiso para ejecutar la funcion de recarga')        
    else:
        print('no tiene permiso para ejecutar la funcion de recarga')