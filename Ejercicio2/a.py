import numpy as np
from NodoLista import NodoLista
arreglo = np.empty(5, dtype=NodoLista)
arreglo[0] = NodoLista()
print(arreglo)
for i in range(2,len(arreglo)):
    print(i)
