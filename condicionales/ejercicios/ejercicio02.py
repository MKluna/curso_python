numeros = []

for i in range(3):
    numero = float(input("Introduce el numero #{}: ".format(i+1)))
    numeros.append(numero)

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("Mayor : ", mayor)
