import numpy as np
import sympy as sp
import doctest

#convertir ecuacion a numeros
def convertir_a_numeros(eq):
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    z = sp.Symbol('z')
    return sp.lambdify((x,y,z), eq)

def simplify(eq):
    convertir_a_numeros(eq)
    return sp.expand(eq)

def main():
    eq = input("Introduce una ecuación: ")
    print(simplify(eq))

if __name__ == '__main__':
    main()
