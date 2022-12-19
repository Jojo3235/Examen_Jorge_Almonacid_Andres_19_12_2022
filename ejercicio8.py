import doctest 

def three_fifty(oracion):
    oracion = oracion.lower()
    if 'three fifty' in oracion or '3.50' in oracion or 'tree fiddy' in oracion:
        return 'Es el monstruo del Lago Ness'
    else:
        return 'No es el monstruo del Lago Ness'

def main():
    oracion = input('Introduce una oración: ')
    print(three_fifty(oracion))

if __name__ == '__main__':
    main()
    doctest.testmod()