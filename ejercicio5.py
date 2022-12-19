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
    for i in range(altura):
        if i == 1:
            print('_'*(altura-i)+'#'+'_'*(altura-i))
        elif i == altura-1:
            print('#'*(2*altura-1))
        else:
            print('_'*(altura-i)+'#'+'_'*(2*i)+'#'+'_'*(altura-i))

def main():
    hollow_triangle()

if __name__ == '__main__':
    main()
    doctest.testmod()

