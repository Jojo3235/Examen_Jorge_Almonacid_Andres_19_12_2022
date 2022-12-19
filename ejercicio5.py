import doctest  #importamos el modulo para la prueba

#Creamos una función para pedir un número
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

#Creamos la función que nos haga las capas de del triangulo
def hollow_triangle():
    altura = pedir_numero()
    for i in range(altura+1):
        if i == 0:
            print('_'*(altura-i-1)+'#'+'_'*(altura-i-1))
        elif i != altura:
            print('_'*(altura-i-1)+'#'+'_'*(2*i-1)+'#'+'_'*(altura-i-1))
        else:
            print('#'*(2*altura-1))

#Creamos la función main
def main():
    hollow_triangle()

#Llamamos a la función main
if __name__ == '__main__':
    main()
    doctest.testmod(main())

