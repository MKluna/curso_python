# Obtener el precio final que se tiene que pagar si se aplica el 36% de descuento del total de la compra

precioInicial = float(input("Ingrese el valor base de la compra: "))
descuento = precioInicial*(36/100)
precioFinal = precioInicial-descuento
print(
    f"El Valor final a pagar aplicando un descuento del 36% es de : ${precioFinal:.2f}")
