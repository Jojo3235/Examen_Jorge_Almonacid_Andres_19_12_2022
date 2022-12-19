import datetime

def dia_actual():
    return datetime.datetime.now().day

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

#pedir fecha de cumpleaños
def pedir_dia_cumpleaños():
    while True:
        try:
            dia = int(input("Introduce el día de tu cumpleaños: "))
            if dia < 1 or dia > 31:
                print("El día debe estar entre 1 y 31")
            else:
                return dia
        except ValueError:
            print("El valor introducido no es un número")

def pedir_mes_cumpleaños():
    while True:
        try:
            mes = int(input("Introduce el mes de tu cumpleaños: "))
            if mes < 1 or mes > 12:
                print("El mes debe estar entre 1 y 12")
            else:
                return mes
        except ValueError:
            print("El valor introducido no es un número")

#calcular la proxima vez que cae el cumpleaños en lunes
def calcular_proximo_cumpleaños():
    dia = pedir_dia_cumpleaños()
    mes = pedir_mes_cumpleaños()
    año = datetime.datetime.now().year
    fecha_cumpleaños = datetime.datetime(año,mes,dia)
    while fecha_cumpleaños.weekday() != 0:
        fecha_cumpleaños = fecha_cumpleaños + datetime.timedelta(days=1)
    return fecha_cumpleaños

def main():
    if comprobar_edad():
        print("Tu próximo cumpleaños que cae en lunes y tienes que trabajar es el: {}".format(calcular_proximo_cumpleaños()))
    else:
        print("No estás en edad laboral")

if __name__ == '__main__':
    main()