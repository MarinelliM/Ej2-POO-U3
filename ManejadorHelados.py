import csv
from Helados import Helado
from Sabores import Sabor
import operator
class ManejaHelados:
    __lista: list

    def __init__(self) -> None:
        self.__lista = []
        pass

    def initmh(self):
        with open('pedidos.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                gramos = int(fila[0])
                if fila[1] != '':
                    precio = int(fila[1])
                else: precio = None
                sabores = fila[2].split(',')
                pedido = Helado(gramos,precio,sabores)
                # for sabor in sabores:
                #     pedido.addSabor(sabor)
                self.__lista.append(pedido)
    
    def test(self):
        i = 0
        for e in self.__lista:
            print('\n')
            print('Pedido {}' .format(i+1))
            e.mostrar()
            i+=1

    def test2(self):
        sabor6 = Sabor(6,'Dulce de leche','cacao,azúcar,leche descremada')
        sabor1 = Sabor(1,'Chocolate','cacao, azúcar, leche')
        sabor2 = Sabor(2,'Vainilla','azúcar, leche, vainilla')
        sabor3 = Sabor(3,'Fresa','azúcar, leche, fresa')
        sabor4 = Sabor(4,'Menta','azúcar, leche, menta')
        sabor5 = Sabor(5,'Cookies and Cream','azúcar, leche, galletas oreo')
        pedido = Helado(500,2100,sabor6)
        pedido.addSabor(sabor1,1)
        pedido.addSabor(sabor2,2)
        self.__lista.append(pedido)
        pedido2 = Helado(1000,None,sabor3)
        pedido2.addSabor(sabor4,1)
        pedido2.addSabor(sabor5,1)
        self.__lista.append(pedido2)

        self.test()
        print('\n')

    def registrar(self,ms):
        print('Opciones:')
        print('100gr = $600 | 150gr = $700 | 250gr = $1300 | 500gr = $2100 | 1000gr = $3700')
        ms.test()
        print('Puede elegir hasta cuatro sabores.')
        print('Opcion o para salir')
        print('\n')
        gramos = int(input('Ingrese la cantidad a pedir:'))
        sabor = str(input('Ingrese sabor:'))
        cont = 0
        if sabor != 'o' and sabor != None:
            objsabor = ms.buscarsabor(sabor)
            pedido = Helado(gramos,None,objsabor)
            cont += 1
            sabor =  str(input('Ingrese sabor:'))
            while cont < 4 and sabor != 'o' and sabor != None:
                objsabor = ms.buscarsabor(sabor)
                pedido.addSabor(objsabor,1)
                cont += 1
                sabor =  str(input('Ingrese sabor:'))
        else: 
            print('Sabor incorrecto')
            return print('No se registro el pedido')
        print('\n')
        print('Pedido realizado:')
        pedido.mostrar()
        self.__lista.append(pedido)

    def maspedidos(self,ms):
        sabores = {}
        # Contar la cantidad de veces que se pide cada sabor
        for helado in self.__lista:
            for sabor in helado.gets():
                if sabor.getnombre() not in sabores:
                    sabores[sabor.getnombre()] = 1
                else:
                    sabores[sabor.getnombre()] += 1
        
        # Ordenar los sabores en función de las veces que se han pedido (de mayor a menor)
        #saboresOrdenados = sorted(sabores, reverse=False)
        # saboresOrdenados = sorted(sabores.items(), key=lambda x: x[1], reverse=True)
        # print(saboresOrdenados)
        saboresOrdenados = list(sabores.items())
        saboresOrdenados.sort(key=lambda x: x[1], reverse=True)
        print(saboresOrdenados)
        saboresNombresOrdenados = [sabor[0] for sabor in saboresOrdenados]
        print(saboresNombresOrdenados)
        # saboresOrdenados = sorted(sabores.items(), key=operator.itemgetter(1), reverse=True)
        # print(saboresOrdenados)
        # Mostrar los 5 sabores más pedidos
        print('\n')
        print('Sabores más pedidos:')
        for i in range(5):
            sabornombre = saboresOrdenados[i][0]
            sabor = ms.buscarsabor(sabornombre)
            if sabor is not None:
                print(f"{i+1}. {sabor.getnombre()}")
            else:
                print(f"{i+1}. Sabor no encontrado")

        

    
