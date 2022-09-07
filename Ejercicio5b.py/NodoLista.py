class NodoLista:
    __valor = None
    __siguiente = None
    

    def __init__(self,valor) -> None:
        self.__valor = valor
        self.__siguiente = None
    
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getValor(self):
        return self.__valor