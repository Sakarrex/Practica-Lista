
from NodoLista import NodoLista
import numpy as np

class ListaEnlazadaCursor:
    __arreglo = None

    def __init__(self,tamanio):
        self.__arreglo = np.empty(tamanio+2,dtype = NodoLista)
        for i in range(tamanio+2):
            self.__arreglo[i] = NodoLista()
        self.__arreglo[0].setValor(2)
        self.__arreglo[0].setSiguiente(tamanio)
        self.__arreglo[1].setValor(-1)
        self.__arreglo[1].setSiguiente(0)
        
        for i in range(2,tamanio+1):
            self.__arreglo[i].setSiguiente(i+1)
        self.__arreglo[tamanio+1].setSiguiente(-1)
    
    def lleno(self):
        return self.__arreglo[0].getSiguiente == 0
    
    def vacia(self):
        return self.__arreglo[1].getSiguiente() == 0

    def Insertar(self,valor,posicion):
        if self.lleno():
            print("Lista llena")
        elif posicion > self.__arreglo[1].getSiguiente()+1 or posicion < 1:
            print("Posicion no valida")
        else:
            posLibre = self.__arreglo[0].getValor()
            self.__arreglo[0].setValor(self.__arreglo[posLibre].getSiguiente())
            self.__arreglo[posLibre].setValor(valor)

            
            if posicion == 1:
                self.__arreglo[posLibre].setSiguiente(self.__arreglo[1].getValor())
                self.__arreglo[1].setValor(posLibre)
            else:
                aux = self.getAux(posicion)
                
                self.__arreglo[posLibre].setSiguiente(self.__arreglo[aux].getSiguiente())
                self.__arreglo[aux].setSiguiente(posLibre)
                
                
               
            self.__arreglo[0].setSiguiente(self.__arreglo[0].getSiguiente()-1)
            self.__arreglo[1].setSiguiente(self.__arreglo[1].getSiguiente()+1)
    
    def Suprimir(self,posicion):
        if posicion > self.__arreglo[1].getSiguiente()or posicion < 1:
            print("Posicion no valida")
        elif self.vacia():
            print("Lista Vacia")
        else:
            if posicion == 1:
                "Actualizo la cabeza a la siguienet pos"
                cabeza = self.__arreglo[1].getValor()
                self.__arreglo[1].setValor(self.__arreglo[cabeza].getSiguiente()) 
                "Coloco la vieja cabeza en las pos libres"
                self.__arreglo[cabeza].setSiguiente(self.__arreglo[0].getValor())
                self.__arreglo[0].setValor(cabeza)
            else:
                aux = self.getAux(posicion)
                posBorrar = self.__arreglo[aux].getSiguiente()
            
                self.__arreglo[aux].setSiguiente(self.__arreglo[posBorrar].getSiguiente())
                self.__arreglo[posBorrar].setSiguiente(self.__arreglo[0].getValor())
                self.__arreglo[0].setValor(posBorrar)
            self.__arreglo[0].setSiguiente(self.__arreglo[0].getSiguiente()+1)
            self.__arreglo[1].setSiguiente(self.__arreglo[1].getSiguiente()-1)

    def Buscar(self,valor):
        aux = self.__arreglo[1].getValor()
        while aux != -1 and self.__arreglo[aux].getValor() != valor:
            aux = self.__arreglo[aux].getSiguiente()
        if aux == -1:
            print("Valor no encontrado")
        else:
            print("Valor Encontrado")
    
    def Recuperar(self,posicion):
        if posicion > self.__arreglo[1].getSiguiente() or posicion < 1:
            raise IndexError
        else:
            aux = self.getAux(posicion)
            return(self.__arreglo[aux].getValor())
    
    def getAnterior(self,posicion):
        if posicion > self.__arreglo[1].getSiguiente()or posicion <= 1:
            raise IndexError
        elif self.vacia():
            raise IndexError
        else:
            return(self.__arreglo[self.getAux(posicion)].getValor())
    
    def getSiguiente(self,posicion):
        if posicion >= self.__arreglo[1].getSiguiente() or posicion < 1:
            raise IndexError
        else:
            return(self.__arreglo[self.__arreglo[self.getAux(posicion)].getSiguiente()].getValor())
    
    def Primer_Elemento(self):
        return self.__arreglo[self.__arreglo[1].getValor()].getValor()
        
        
    def getAux(self,posicion):
        cont = 1
        aux = self.__arreglo[1].getValor()
        while aux != -1 and cont<posicion-1:
            aux = self.__arreglo[aux].getSiguiente()
            cont+=1
        return aux
    
    def Ultimo_Elemento(self):
        aux = self.__arreglo[1].getValor()
        while self.__arreglo[aux].getSiguiente() != -1 :
            aux = self.__arreglo[aux].getSiguiente()
        return self.__arreglo[aux].getValor()

        


    def Recorrer(self):
        aux = self.__arreglo[1].getValor()
        cadena = ""
        while aux != -1:
            cadena += str((self.__arreglo[aux].getValor()))+ ","
            
            aux = self.__arreglo[aux].getSiguiente()
        print(cadena)
        

            
            
            
    def Mostrar(self):
        cadena = "Registro 0: PosDisponible: {} CantDisponible: {} \nRegistro 1: Cabeza: {} Cantidad: {}\n".format(self.__arreglo[0].getValor(),self.__arreglo[0].getSiguiente(),self.__arreglo[1].getValor(),self.__arreglo[1].getSiguiente())

        for i in range(2,len(self.__arreglo)):
            cadena += "Registro {}: valor: {} siguiente: {}".format(i,self.__arreglo[i].getValor(),self.__arreglo[i].getSiguiente()) + "\n"
        print(cadena)