#importamos el módulo doctest
import doctest

#Creamos la función pedir número
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

#Creamos fibonacci de n terminos
def xbonacci(lista, n):
    resultado = []
    for i in range(len(lista)):
        resultado.append(lista[i])
    for i in range(len(lista), n):
        siguiente_elemento = sum(resultado[-len(lista):])
        resultado.append(siguiente_elemento)
    return resultado

#Creamos una función para crear una lista que vaya añadiendo numeros hasta que se pare
def crear_lista():
    lista = []
    while True:
        try:
            numero = int(input("Introduce un número: "))
            if numero < 0:
                print("El número debe ser positivo")
            else:
                lista.append(numero)
        except ValueError:
            print("El valor introducido no es un número")
            break
    return lista

#Creamos la función main
def main():
    lista = crear_lista()
    n = pedir_numero()
    print(xbonacci(lista, n))

#Llamamos a la función main
if __name__ == '__main__':
    main()
    doctest.testmod(main())