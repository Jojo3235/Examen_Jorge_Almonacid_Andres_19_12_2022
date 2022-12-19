def pedir_edad():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad < 0:
                print("La edad debe ser positiva")
            else:
                return edad
        except ValueError:
            print("El valor introducido no es un número")

def comprobar_edad():
    edad  = pedir_edad()
    if edad > 22 and edad < 78:
        return True
    else:
        return False


