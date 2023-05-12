# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año se añaden al final de
# tu balance de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de
# dinero depositada en la cuenta de ahorros introducida por el usuario. Después el programa debe
# calcular y mostrar por pantalla la cantidad ahorros del primer, segundo y tercer año. Redondear
# cada cantidad a 2 decimales


monto_inicial = float(input("\nIngrese el monto inicial de su ahorro: "))

saldo_anno1 = monto_inicial + (monto_inicial * 0.04)
saldo_anno2 = saldo_anno1 + (saldo_anno1 * 0.04)
saldo_anno3 = saldo_anno2 + (saldo_anno2 * 0.04)

print('\n-------------------------------------')
print('Estado de cuenta anual de sus ahorros')
print(f'   primer  año: {round(saldo_anno1, 2)}')
print(f'   segundo año: {round(saldo_anno2, 2)}')
print(f'   tercer  año: {round(saldo_anno3, 2)}')
print('-------------------------------------\n')
