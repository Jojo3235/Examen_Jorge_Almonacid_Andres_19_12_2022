#Importamos las librerias
import numpy as np
import doctest

#Creamos la clase Caballo con la funcion movimiento como metodo
class Caballo:
    def __init__(self, posicion):
        self.fila = posicion[0]
        self.columna = posicion[1]
    
    def movimiento(self):
        distancia =  np.abs(np.subtract.outer(np.arange(8),np.arange(8)))
        return distancia[self.fila][self.columna]

#Creamos la funcion para pedir un numero
def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número: "))
            if numero < 0 and numero > 8:
                print("El número debe ser positivo")
            else:
                return numero
        except ValueError:
            print("El valor introducido no es un número")

#Creamos la funcion para pedir una lista
def lista_posicion():
    lista = []
    posicion1 = pedir_numero()
    posicion2 = pedir_numero()
    lista.append(posicion1)
    lista.append(posicion2)
    return lista

#Creamos la función main
def main():
    tablero = np.full((8,8), ' ')
    posicion = lista_posicion()
    caballo = Caballo(posicion)
    posicion_deseadad = lista_posicion()
    print(caballo.movimiento())

#Llamamos a la función main
if __name__ == '__main__':
    main()
    doctest.testmod(main())