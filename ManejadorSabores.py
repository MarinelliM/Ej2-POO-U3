import csv
from Sabores import Sabor
class ManejaSabores:
    __lista: list

    def __init__(self) -> None:
        self.__lista = []
        pass

    def initms(self):
        with open('sabores.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                id = int(fila[0])
                nombre = str(fila[1])
                ingredientes = str(fila[2])
                sabor = Sabor(id,nombre,ingredientes)
                self.__lista.append(sabor)

    def test(self):
        i = 0
        for e in self.__lista:
            print('\n')
            print('Sabor {}' .format(i+1))
            e.mostrar()
            i+=1
        print('\n')

    def buscarsabor(self,sabor):
        i = 0
        obj = None
        while i < len(self.__lista):
            if sabor == self.__lista[i].getnombre():
                obj = self.__lista[i]
                i = len(self.__lista)
            else: i+=1
        if obj != None:
            return obj
        else: print('No se encontro el sabor')
