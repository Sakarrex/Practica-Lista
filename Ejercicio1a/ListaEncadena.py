
from NodoLista import NodoLista

class ListaEncadenada:
    __cabeza = None
    __cantidad = None
    __ultimo = None

    def __init__(self) -> None:
        self.__cabeza = None
        self.__cantidad = 0
        self.__ultimo = None

    def Insertar(self,elemento,posicion):
        if posicion < 0 or posicion > self.__cantidad+1:
            print("Posicion no valida")
        else:
            NuevoNodo = NodoLista(elemento)
            if self.__cabeza == None:
                self.__cabeza = NuevoNodo
                self.__ultimo = NuevoNodo
                self.__cantidad+=1
            else:
                aux = self.__cabeza
                posActual = 1
                while posActual != posicion:
                    aux = aux.getSiguiente()
                if aux.getSiguiente() == self.__ultimo:
                    aux.setSiguiente(NuevoNodo)
                else:
                    NuevoNodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(NuevoNodo)
            self.__cantidad += 1 


    def vacio(self):
        return self.__cabeza == None
    
    def Suprimir(self,posicion):
        if self.vacio():
            print("No se puede suprimir lista vacia")
    
    def Recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getValor())
            aux= aux.getSiguiente()


