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
        print('_'*(altura-i)+'#'*(1+2*i)+'_'*(altura-i))

def main():
    hollow_triangle()

if __name__ == '__main__':
    main()
    doctest.testmod()

