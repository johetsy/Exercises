# Escribir un programa que pregunte al usuario su edad y muestre por pantalla
# si es mayor de edad o no.

edad_maxima = 18
edad = int(input("Cuál es tu edad? "))

if edad < edad_maxima:
    print("Eres menor de edad.")

else:
    print("Eres mayor de edad.")
