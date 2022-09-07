from ListaEncadena import ListaEncadenadaContenido

if __name__ == "__main__":
    UnaLista = ListaEncadenadaContenido()
    
    UnaLista.Insertar(3)
    UnaLista.Insertar(3)
    UnaLista.Insertar(3)
    UnaLista.Insertar(4)
    UnaLista.Insertar(1)
    UnaLista.Insertar(1)
    
    UnaLista.Recorrer()
    UnaLista.BorrarDuplicados()
    print("------------------------")
    UnaLista.Recorrer()