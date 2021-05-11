#Obtener el radio y longitud de un circulo
#área = pi*r^2
#longitud = 2*pi*r
import math
r = float(input("Ingrese el radio : "))
area = math.pi*r**2
longitud = 2*math.pi*r
# :.1f para redondear un numero float
print(f"El area es : {area:.1f} y la longitud es : {longitud:.1f}")