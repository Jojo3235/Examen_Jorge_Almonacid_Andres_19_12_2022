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

def hollow_triangle():
    altura = pedir_numero()
    for i in range(altura+1):
        if i == 0:
            print('_'*(altura-i-1)+'#'+'_'*(altura-i-1))
        elif i != altura:
            print('_'*(altura-i-1)+'#'+'_'*(2*i-1)+'#'+'_'*(altura-i-1))
        else:
            print('#'*(2*altura-1))

def main():
    hollow_triangle()

if __name__ == '__main__':
    main()
    doctest.testmod(main())

