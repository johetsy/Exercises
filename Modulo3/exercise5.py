
cantidad = float(input("Ingresa la cantidad a invertir: "))
interes = float(input("Ingresa el interés anual "))
años = int(input("Ingresa el numero de años: "))
capital = str(round(cantidad * (interes / 100 + 1) ** años, 2))

print("Capital Obtenido al final del período es de: ", capital)
