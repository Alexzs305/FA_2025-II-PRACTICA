def ejer1():
    edad = int(input("Ingrese su edad"))

    if edad >= 18:
        print("Puede votar.")

        if edad >= 25:
            print("Puede ser candidato a un cargo politico.")
        else:
            print("No puede ser candidato a un cargo politico.")
    else:
        print("No puede votar.")
        print("No puede ejercer un cargo politico.")

def ejer2():
    lado1 = int(input("Ingrese lado 1:"))
    lado2 = int(input("Ingrese lado 2:"))
    lado3 = int(input("Ingrese lado 3:"))

    if(lado1 == lado2 == lado3):
        print("EQUILATERO")
    else:
        if(lado1 == lado2 or Lado1 == lado3):
            print("ISÓSCELES")
        else:
            print("ESCALENO")
ejer2()