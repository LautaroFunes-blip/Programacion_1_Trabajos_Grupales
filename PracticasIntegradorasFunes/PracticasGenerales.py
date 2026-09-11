import PedirGolosinas, MostrarGolosinas, RellenarGolosinas, ApagarMaquina

golosinas=[
    [1,'KitKat', 20],
    [2,'Chicles',50],
    [3,'Carameloos de Menta',50],
    [4,'Huevos Kinder',10],
    [5,'Chetoos',10],
    [6,'Twix',10],
    [7,"M&M's",10],
    [8,"Papas Lay's",2],
    [9,'Milkybar',10],
    [10,'Alfajor Tofi',15],
    [11,'Lata Coca',20],
    [12,'Chitos',10],
]

empleados={
    1100:'José Alonso',
    1200:'Federico Pacheco',
    1300: 'Nelson Pereira', 
    1400: 'Osvaldo Tejeda',
    1500: 'Gastón Garcia'
}

clavesTecnico=('admin', 'CCCDDD', '2020')

golosinasPedidas=[]
opcion=None
while True:
    opcion=input('ingrese el numero de la funcion que quiere realizar' \
    '1=Pedir Golosinas \n 2=Mostrar Golosinas \n 3=Rellenar Golosinas' \
    '\n 4=Apagar Maquina')
    try:
        opcion=int(opcion)
        if opcion == 1:
            PedirGolosinas.PedirGolosinas(empleados, golosinas, golosinasPedidas)
        elif opcion==2:
            MostrarGolosinas.mostrarGolosinas(golosinas)
        elif opcion==3:
            RellenarGolosinas.rellenarGolosinas(golosinas, clavesTecnico)
        elif opcion==4:
            ApagarMaquina.apagarMaquina(golosinasPedidas)
            print('adios')
            break
    except ValueError:
        print('ingrese una opcion valida dentro de las fuinciones')