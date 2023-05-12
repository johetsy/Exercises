# Para tributar un derminadado impuesto se debe ser mayor de 16 años y
# tener unos ingresos iguales o superiores a 1000 euros mensuales.
# Escribir un programa que pregunte al usuario su edad
# y sus ingresos mensuales y muestre por pantalla si el
# usuario tiene que tributar o no.


edad_minima = 16
ingresos_tope = 1000

annos = int(input("\n¿Cuál es tu edad? "))
ingreso = float(input("¿Cuales son tus ingresos mensuales?"))

if annos > edad_minima and ingreso >= ingresos_tope:
    print("\nTienes que tributar")
else:
    print("\nNo tienes que tributar")
