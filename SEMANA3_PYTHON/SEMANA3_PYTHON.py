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

def ejer6():
    s # type: ignore

def ejer7():
    monto  = float(input("Ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")

    opcion = int(print("\nIngrese una opción: "))

    match opcion:
        case 1: print("DOLARES: ", round(monto / 3.75))
        case 2: print(f"EUROS: , {monto/4.85:.2f}")
        case _: print("OPCION INCORRECTA")

import match

def ejer8():
    print("BIENVENIDO AL SISTEMA DE CALCULO DE ÁREAS")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3.Triángulo")
    print("4. Circulo")

    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            lado = int(input("Ingresa el lado: "))
            print("Area: ", lado*lado)
        case 2: 
            bse = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print("Area rectangulo: ", (bse*alt)/2)
        case 3:
            bse2 = int(input("Ingrese la base: "))
            alt2 = int(input("Ingrese la altura: "))
            print("Area triangulo: ", (bse2*alt2)/2)
        case 4: 
            radio = float(input("Ingrese el radio: "))
            print("Area del circulo: ",(round(math.pi * radio **2),2))
        case _:print("Opcion Incorrecta")


ejer8()
