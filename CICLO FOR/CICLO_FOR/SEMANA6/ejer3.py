filas = int(input("INGRESE NUMERO DE FILAS: "))
columnas = int(input("INGRESE NUMERO DE COLUMNAS: "))
print()

i = 0

while i < filas:
    j = 0
    while j < columnas:
        print("*", end=" ")
        j +=1
    print("*")
    i += 1