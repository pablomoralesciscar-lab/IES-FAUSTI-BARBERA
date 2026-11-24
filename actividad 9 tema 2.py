n = 1
n1 = int(input("¿Cuantos numeros quieres contar?"))
while n1 > 0:
    print(str(n))
    n1 -= 1
    n += 1
    n2 = n // 5
    while n2 == 0:
        print("")