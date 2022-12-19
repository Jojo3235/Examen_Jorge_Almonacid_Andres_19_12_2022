#importamos las librearias necesarias
import numpy as np
import doctest

#Creamos la función pedir numero
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

#Creamos una función que nos pida un número entre 0 y 1 para calcular el porcentaje de pasto que se quiere guardar 
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

#Creamos la función area que nos calcula el diametro del pasto total
def area(diametro):
    radio = diametro/2
    return (np.pi * radio ** 2)

#Creamos la función area_protegida que nos indica el área que queremos proteger
def area_protegida(diametro,porcentaje):
    area_prot = area(diametro)*porcentaje
    return area_prot

#Creamos la función longitud_area_protegida que nos calcular cuanto tiene que medir la cerca para proteger la zona
def longitud_area_protegida():
    p = pedir_numero_0_1()
    d = pedir_numero()
    area_prot= area_protegida(d,p)
    r = np.sqrt(area_prot/np.pi)
    longitud = 2*np.pi*r
    return longitud

#Creamos la función main
def main():
    print(longitud_area_protegida())

#Llamamos a la función main
if __name__ == '__main__':
    main()
    doctest.testmod()