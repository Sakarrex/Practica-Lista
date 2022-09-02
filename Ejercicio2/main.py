
from ListaEnlazadaPuntero import ListaEnlazadaCursor

if __name__ == '__main__':
    UnaLista = ListaEnlazadaCursor(4)
    UnaLista.Insertar(3,1)
    UnaLista.Insertar(5,1)
    UnaLista.Insertar(7,2)
    UnaLista.Insertar(9,4)
    UnaLista.Recorrer()
    print(UnaLista.Ultimo_Elemento())
    
    
    print("--------------------------")

    
