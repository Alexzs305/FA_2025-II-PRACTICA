def ejer1():
    nombre = input("(P)Ingrese su nombre:")
    carrera = input("(P)Ingrese su carrera:")

    print(f"\n{nombre}, Bienvenido al curso de Fundamentos de Algoritmos de la carrera {carrera}")

def ejer2():
    print("\"\"ALEXIS\"\"")
def ejer3():
    x= int(input("Ingrese el valor de x:"))
    y= int(input("Ingrese el valor de y:"))

    print("suma", (x+y))
    print("resta", (x-y))
    print("Multiplicación", (x*y))
    print("Division", (x/y))

import math #IMPORTANDO LA LIBRERIA MATH

def ejer4():
    num= int(input("Ingrese un numero decimal: "))

    print ("Raiz2: ", math.sqrt(num))
    print ("Redondeado: ", round(num, 0))
    print("Al cubo: ", math.pow(num, 3))
    print("raiz3: ", num**(1/3))

def ejer5():
    num = input("Ingrese un numero: ")

    entero = int(num)
    deci = float(num)

    print("Resto: ", (entero%2))
    print("Division: ", (deci/3))

ejer5()
 