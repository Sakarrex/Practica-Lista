from ListaEncadena import ListaEncadenada

if __name__ == "__main__":
    UnaLista = ListaEncadenada()
    
    UnaLista.Insertar(1,1)
    UnaLista.Insertar(2,2)
    UnaLista.Insertar(3,3)
    UnaLista.Insertar(3,4)
    UnaLista.Insertar(3,5)
    UnaLista.Insertar(2,6)
    UnaLista.Insertar(1,7)
    UnaLista.Recorrer()
    UnaLista.BorrarDuplicados()
    print("------------------------")
    UnaLista.Recorrer()