import numpy as np
import doctest

def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número: "))
            if numero < 0:
                print("El número debe ser positivo")
            else:
                return numero
        except ValueError:
            print("El valor introducido no es un número")

def pedir_numero_0_1():
    while True:
        try:
            numero = float(input("Introduce un número entre 0 y 1: "))
            if numero < 0 or numero > 1:
                print("El número debe estar entre 0 y 1")
            else:
                return numero
        except ValueError:
            print("El valor introducido no es un número")

def area(diametro):
    radio = diametro/2
    return (np.pi * radio ** 2)

def area_protegida(diametro,porcentaje):
    area_prot = area(diametro)*porcentaje
    return area_prot

def longitud_area_protegida():
    p = pedir_numero_0_1()
    d = pedir_numero()
    area_prot= area_protegida(d,p)
    r = np.sqrt(area_prot/np.pi)
    longitud = 2*np.pi*r
    return longitud

def main():
    print(longitud_area_protegida())

if __name__ == '__main__':
    main()
    doctest.testmod()