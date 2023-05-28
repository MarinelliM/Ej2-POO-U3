class Sabor:
    __idsabor: str
    __nombre: str
    __ingredientes: str

    def __init__(self,id,nombre,ingredientes) -> None:
        self.__idsabor = id
        self.__nombre = nombre
        self.__ingredientes = ingredientes
        pass

    def getid(self):
        return self.__idsabor
    
    def getnombre(self):
        return self.__nombre
    
    def getingredientes(self):
        return self.__ingredientes

    def mostrar(self):
        print('Idsabor: {}, Nombre: {}, Ingredientes: {}' .format(self.getid(),self.getnombre(),self.getingredientes()))
        