# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
pizza_vegetariana = 'pimiento ó tofu'
pizza_original = 'peperoni ó jamon ó salmon'
base_pizza = 'tomate y mozarella'

tipo_pizza = int(
    input('\nPedido: \n[1] Vegetariana \n[2] No vegetariana \n\nEscoge tu pizza: '))

print('\nTodas las pizzas tienen', base_pizza)

if tipo_pizza == 1:
    tipo_pizza = 'Vegetariana'
    print('Puedes adicionar:', pizza_vegetariana)
    ingrediente = str(input('Elege 1, Cuál deseas? '))
else:
    tipo_pizza = 'No Vegetariana'
    print('Puedes dicionar', pizza_original)
    ingrediente = str(input('Elege 1, Cuál deseas? '))
print('\n------------ORDEN PIZZA------------------')
print('Tipo: ', tipo_pizza, '\nIngredientes:',
      base_pizza, ' \nEl adicional es:', ingrediente, )
print('\n-----------------------------------------')
