class NodoLista:
    __valor = None
    __siguiente = None
    

    def __init__(self) -> None:
        self.__valor = 0
        self.__siguiente = None
    
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getValor(self):
        return self.__valor
    
    def setValor(self, valor):
        self.__valor = valor