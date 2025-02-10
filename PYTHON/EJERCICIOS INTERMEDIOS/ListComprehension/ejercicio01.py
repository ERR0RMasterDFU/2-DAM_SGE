# EJERCICIO 1
# Encuentra todos los números del 1 al 1000 que sean divisibles por 7.

lista_numeros = list(range(1, 1001))
lista_num_div_7 = list(n for n in lista_numeros if n%7 == 0)

print(lista_num_div_7)
