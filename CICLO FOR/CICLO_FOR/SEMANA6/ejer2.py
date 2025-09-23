sumap = sumai = 0
while True:
    num = int(input("Ingrese un numero positivo (0salir): )"))

    if num<0:
        print("Numero invalido. Ingrese nuevamente")
        continue

    if num ==0:
        break

    if num % 2 ==0:
        sumap += num
    else:
        sumai += num 

print("n\Suma pares", sumap)
print("suma impares", sumai)