# Operadores Logicos
a = 30
b = 40
c = 50

# Ambos deben cumplirse para que devuelva true
r = ((a < b) and (b < c))
print(r)
# Cualquiera de ellos debe ser true para cumplir la condicion y devolver un true
r = ((a < b) or (b < c))
print(r)

# Niega Todo
r = not((a < b) or (b < c))
print(r)
