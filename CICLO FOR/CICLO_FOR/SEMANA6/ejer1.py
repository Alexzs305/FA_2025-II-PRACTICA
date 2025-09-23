num = int(input("Ingrese un numero positivo: "))
print()
i = 1
while num <= 0:
    num = int (input("ERROR. Ingrese un numero positivo: "))

while i <= 12:
    print(f"{i} x {num} = {i * num}")
    i += 1