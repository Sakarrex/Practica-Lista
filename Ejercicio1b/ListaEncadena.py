from NodoLista import NodoLista

class ListaEncadenadaContenido:
    __cabeza = None
    __cantidad = None
    

    def __init__(self) -> None:
        self.__cabeza = None
        self.__cantidad = 0
        

    def Insertar(self,elemento):
        NuevoNodo= NodoLista(elemento)
        if self.__cabeza == None:
            self.__cabeza = NuevoNodo
        else:
            aux = self.__cabeza
            while aux.getSiguiente() != None and aux.getSiguiente().getValor() < elemento:
                aux = aux.getSiguiente()
            NuevoNodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(NuevoNodo)
        



    def vacio(self):
        return self.__cabeza == None
    
    def Suprimir(self,posicion):
        if self.vacio():
            print("No se puede suprimir lista vacia")
        elif posicion < 0 or posicion >= self.__cantidad+1:
            print("Posicion no valida")
        else:
            aux = self.__cabeza
            actualPos = 1
            while actualPos < posicion-1:
                aux = aux.getSiguiente()
                actualPos += 1
            eliminar = aux.getSiguiente()
            aux.setSiguiente(eliminar.getSiguiente())
            del eliminar
            self.__cantidad -= 1
    
    def Buscar(self,elemento):
        encontrado = False
        aux = self.__cabeza
        while aux != None and encontrado == False:
            if aux.getValor() == elemento:
                encontrado = True
            aux = aux.getSiguiente()
        if not encontrado:
            print("Elemento no encontrado")
        else:
            print("Elemento encontrado")

    def Recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getValor())
            aux= aux.getSiguiente()

    def Primer_Elemento(self):
        return self.__cabeza.getValor()
    
    def Ultimo_Elemento(self):
        aux = self.__cabeza
        while aux.getSiguiente() != None:
            aux = aux.getSiguiente()
        return aux.getValor()
    
    def getAnterior(self,posicion):
        if not self.vacio() and posicion == 1:
            aux = self.__cabeza
            actualPos = 1
            while actualPos < posicion-1:
                aux = aux.getSiguiente()
                actualPos += 1
            return aux.getValor()
    
    def getSiguiente(self,posicion):
        if not self.vacio() and posicion < self.__cantidad:
            aux = self.__cabeza
            actualPos = 1
            while actualPos < posicion:
                aux = aux.getSiguiente()
                actualPos += 1
           
            return aux.getSiguiente().getValor()


