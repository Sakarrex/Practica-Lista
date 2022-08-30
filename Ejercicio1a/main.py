
from ListaSecuencial import ListaSecuencial
from ListaEncadena import ListaEncadenada

if __name__ == "__main__":
    UnaLista = ListaEncadenada()
    UnaLista.Insertar(2,1)
    UnaLista.Insertar(1,1)
    UnaLista.Insertar(3,3)
    UnaLista.Insertar(4,2)
    UnaLista.Recorrer()
    print("-----------------------")
    print(UnaLista.getSiguiente(4))