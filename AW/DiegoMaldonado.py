print ("En este ejercicio te voy a decir si el numero es par o impar y tambien si es negativo o positivo")
n = int(input("Introduce tu numero: "))
p = n % 2
if p == 0 and n > 0:
    print ("Tu numero es positivo y par.")
elif p == 1 and n < 0:
    print("Tu numero es negativo e impar.")
elif p == 0 and n < 0:
    print("Tu numero es negativo y par.")
elif p == 1 and n > 0:
    print("Tu numero es positivo e impar.")
else:
    print ("El número es cero.")
