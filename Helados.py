from Sabores import Sabor
class Helado:
    __gramos: int
    __precio: int
    __sabores: list
    def __init__(self, gramos, precio=None, sabor=None) -> None:
        self.__gramos = gramos
        self.__sabores = []
        if precio != None:
            self.__precio = precio
        elif self.getgramos() == 100:
            self.__precio = 600
        elif self.getgramos() == 150:
            self.__precio = 700
        elif self.getgramos() == 250:
            self.__precio = 1300
        elif self.getgramos() == 500:
            self.__precio = 2100
        elif self.getgramos() == 1000:
            self.__precio = 3700
        elif self.getgramos() > 1000: self.__precio = 5000
        if sabor != None:
            self.addSabor(sabor,1)
        pass
    def addSabor(self,sabor, cantidad):
        for e in range(cantidad):
            self.__sabores.append(sabor)

    def getgramos(self):
        return self.__gramos
    
    def getprecio(self):
        return self.__precio
    
    def getsabores(self):
        for sabor in self.__sabores:
            sabor.mostrar()
    
    def gets(self):
        return self.__sabores
    
    def mostrar(self):
        print('Gramos: {}' .format(self.getgramos()))
        self.getsabores()
        print('TOTAL A PAGAR: {}' .format(self.getprecio()))
