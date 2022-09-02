from ListaEncadena import ListaEncadenadaContenido
from ListaSecuencial import ListaSecuencialContenido

if __name__ == '__main__':
    UnaLista = ListaSecuencialContenido(3)
    UnaLista.Insertar(2)
    UnaLista.Insertar(7)
    UnaLista.Insertar(5)
    UnaLista.Insertar(10)
    UnaLista.Recorrer()