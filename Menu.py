def menu(mh,ms):
    print('1 - Registrar un helado vendido.')
    print('2 - Mostrar el nombre de los 5 sabores de helado más pedidos.')
    print('0 - Salir')
    op = int(input('Ingrese la opcion a buscar:'))
    while op != 0:
        if op == 1:
           print('\n')
           mh.registrar(ms)
           print('\n')
        elif op == 2:
            mh.maspedidos(ms)
            print('\n')
        else:
            print('Opcion incorrecta')
            op = int(input('Ingrese la opcion a buscar:'))
        print('1 - Registrar un helado vendido.')
        print('2 - Mostrar el nombre de los 5 sabores de helado más pedidos.')
        print('0 - Salir')
        op = int(input('Ingrese la opcion a buscar:'))
    print('Fin del programa')