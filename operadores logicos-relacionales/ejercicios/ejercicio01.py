# Formula : (c+5)(b^2 - 3ac)a^2 / 4a
a = float(input("Ingrese el valor de A : "))
b = float(input("Ingrese el valor de B : "))
c = float(input("Ingrese el valor de C : "))

resultado = ((c+5)*(b**2-3*a*c)*(a**2))/(4*a)
print(f"El Resultado es: {resultado}")
