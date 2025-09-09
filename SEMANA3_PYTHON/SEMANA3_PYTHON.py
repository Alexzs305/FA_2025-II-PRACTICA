def ejer1():
    nombre = input("(P)Ingrese su nombre:")
    carrera = input("(P)Ingrese su carrera:")

    print(f"\n{nombre}, Bienvenido al curso de Fundamentos de Algoritmos de la carrera {carrera}")

def ejer2():
    x= int(input("Ingrese el valor de x:"))
    y= int(input("Ingrese el valor de y:"))

    print("suma", (x+y))
    print("resta", (x-y))
    print("Multiplicación", (x*y))
    print("Division", (x/y))
    
    ejer2()
