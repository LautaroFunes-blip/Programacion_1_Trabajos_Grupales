def PedirGolosinas(empleados, golosinas, golosinasPedidas):
    legajo=input('ingrese su legajo')
    try:
        legajo=int(legajo)
        if legajo in empleados:
            golosinaInput=input('ingrese el valor de la golosina que quiere pedir ' \
            '1= KitKat \n 2= Chicles \n 3=Caramelos de Menta \n 4=Huevos Kinder \n 5=Chetoos \n 6=Twix \n 7=M&M´s \n ' \
            '8=Papas Lays \n 9=Milkybar \n 10=Alfajor Tofi \n 11=Latas Coca \n 12=Chitos \n')

            try:
                golosinaInput=int(golosinaInput)
                if 1<= golosinaInput <= len(golosinas):
                    indice=golosinaInput-1
                    stock=golosinas[indice][2]
                    if stock > 0:
                        stock_final=stock-1
                        golosinas[indice][2] = stock_final

                        codigo = golosinas[indice][0]
                        nombreGolosina = golosinas[indice][1]

                        encontrado = False
                        for fila in golosinasPedidas:
                            if fila[0] == codigo:
                                fila[2] = fila[2] + 1
                                encontrado = True

                        if not encontrado:
                            golosinasPedidas.append([codigo, nombreGolosina, 1])
                    elif stock <= 0:
                        print(f'no hay stock de la golosina {golosinas[indice][1]}, solicite al tecnico que reponga la maquina')
                else:
                    print('ingrese un valor correspondiente dentro de la lista de productos')
            except ValueError:
                print('ingrese el numero correspondiente a la golosina qeu esta buscando')
        else:
            print('usted no es empleado de la empresa')
    except ValueError:
        print('ingrese un legajo valido')