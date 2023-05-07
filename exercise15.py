# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden
# ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación
# del nivel.
# Nivel    Puntuación
# Inaceptable    0.0
# Aceptable    0.4
# Meritorio    0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
# así como la cantidad de dinero que recibirá el usuario

print('\n[1] para puntuacion = 0.0 \n[2] para puntuacion = 0.4 \n[3] para puntuacion mayor a 0.6')

puntuacion = int(input("\nIngresa la opcion de tu puntuación: "))

print('---------------------------------')

if puntuacion >= 1 and puntuacion <= 3:
    if puntuacion == 1:
        print('Nivel = Inaceptable \ndinero a recibir es 0 Euros')

    elif puntuacion == 2:
        dinero = 2400 * 0.4
        print('Nivel = Aceptable \ndinero a recibir es de ', int(dinero), 'Euros')

    elif puntuacion >= 0.6:
        dinero = 2400 * 0.6
        print('Nivel = Meritorio \ndinero a recibir es de ', int(dinero), 'Euros')

else:
    print("Puntuación no válida")

print('---------------------------------\n')
