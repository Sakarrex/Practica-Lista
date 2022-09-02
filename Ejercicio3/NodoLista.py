class NodoLista:
    __provincia = None
    __superficieTotal = None
    __siguiente = None
    

    def __init__(self,provincia) -> None:
        self.__provincia = provincia
        self.__superficieTotal = 0
        self.__siguiente = None
    
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getProvincia(self):
        return self.__provincia
    
    def getSuperficie(self):
        return self.__superficieTotal
    
    def setSuperficieTotal(self, num):
        self.__superficieTotal = num