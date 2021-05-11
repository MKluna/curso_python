saldo = 2000
print("1. Ingreso de dinero")
print("2. Retiro  de dinero")
print("3. Mostrar dinero")
print("4. Salir")

seleccion = int(input("Elija una opcion: "))

if seleccion == 1:
  ingreso = float(input("Dinero a ingresar: "))
  saldo += ingreso
  print(f"Su nuevo saldo es: {saldo}")
elif seleccion == 2:
  salida = float(input("Dinero de salida: "))
  if salida > saldo:
    print("Saldo insuficiente")
  else:
    salida -= salida
    print(f"Nuevo saldo disponible {saldo}")
elif seleccion == 3:
  print(f"Saldo disponible {saldo}")
elif seleccion == 4:
  print("Fin")
else:
  print("Error")
