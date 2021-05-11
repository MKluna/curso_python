a = float(input("Ingrese el valor de A : "))
b = float(input("Ingrese el valor de B : "))

a, b = b, a
print(f"El nuevo valor de A es : {a}")
print(f"El nuevo valor de B es : {b}")