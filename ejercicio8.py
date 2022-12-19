#Importamos la librería doctest
import doctest 

#Creamos la función three_fifty para encontrar si es el monstruo del Lago Ness
def three_fifty(oracion):
    oracion = oracion.lower()
    if 'three fifty' in oracion or '3.50' in oracion or 'tree fiddy' in oracion:
        return 'Es el monstruo del Lago Ness'
    else:
        return 'No es el monstruo del Lago Ness'

#Creamos la función main
def main():
    oracion = input('Introduce una oración: ')
    print(three_fifty(oracion))

#Llamamos a la función main
if __name__ == '__main__':
    main()
    doctest.testmod(main())