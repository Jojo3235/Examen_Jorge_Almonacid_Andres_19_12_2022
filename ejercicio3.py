#Creamos una diccionario que nos relacione los numeros con su palabra en ingles
numeros = {0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
            }

#Creamos la funcion que nos pida un numero
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

#Creamos la funcion que nos separe los digitos del numero en una lista
def separar_numero_lista(n):
    lista = []
    pass
def numbersOfLetters(n):
    pass