# Escribir un programa que pida al usuario dos números y muestre por
# pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numerador = float(input("Ingresa el dividendo: "))
denominador = float(input("Ingresa el divisor: "))

if denominador == 0:
    print("***¡Error! No se puede dividir por 0.***")

else:
    resultado = numerador % denominador
    print('El resultado es:', numerador/denominador)
