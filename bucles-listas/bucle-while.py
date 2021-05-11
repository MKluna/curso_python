import math

numero = 0
while numero < 20:
    print(numero)
    numero += 1

numero = int(input("Escriba un numero: "))
while numero < 0:
    print("Por favor ingrese un numero positivo")
    numero = int(input("Vuelva a ingresar un numero positivo: "))
print(f"La raiz cuadrada es : {math.sqrt(numero):.2f}")
