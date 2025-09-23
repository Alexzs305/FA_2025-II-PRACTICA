def ejer1():
    n = int(input("INGRESE UN NUMERO: "))
    suma = 0

    print()

    for i in range(n+1):
        print(i)

        if i % 2 == 0:
            suma += i

    print("\n Suma de pares", suma)

def ejer2():

    cant = int(input("Ingrese la cantidad de numeros"))
    ceros = pares = impares = 0
    print()

    for i in range(1, cant+1):
        num = int(input(f"ingrese el numero {i}: "))

        if num ==0:
            ceros+=1 #ceros+
        elif num % 2==0:
            par += 1 #par+
        else:
            impares += 1 #impar+

    print("\n#ceros: ", ceros)
    print("#pares: ", pares)
    print("#impares: ", impares)

ejer2()
