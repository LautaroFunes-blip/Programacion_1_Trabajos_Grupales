def apagarMaquina(golosinasPedidas):
    golosinasCantidad=[]
    for golosinas in golosinasPedidas:
        print(golosinas[1], golosinas[2])
        golosinasCantidad.append(golosinas[2])
    suma=sum(golosinasCantidad)
    print(f'cantidad total de golosina vendidas {suma}')