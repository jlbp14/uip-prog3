nombre = input ("Nombre del vendedor: ")
mes1 = float(input ("Ingrese venta mes 1: "))
mes2 = float(input("Ingrese venta mes 2: "))
mes3 = float(input ("Ingrese venta mes 3: "))
ventot = mes1 + mes2 + mes3
comi = ventot * 0.125
print ("Informe de comisiones\nVendedor\tVentas\tComision\n--------\t------\t--------\n" + nombre + "\t" + str(ventot) + "\t" + str(comi))
       
