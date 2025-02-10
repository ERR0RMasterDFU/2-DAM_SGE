# EJERCICIO 5
# Obtén el índice y el valor como una tupla para los elementos de la lista “hi”, 4, 8.99, 'apple', 
# ('t,b','n'). El resultado se vería así (índice, valor), (índice, valor).

lista = ["hi", 4, 8.99, 'apple', ('t,b','n')]

lista_tuplas = list(tuple([lista.index(e), e]) for e in lista) 

print(f"Lista de tuplas con índice y valor:\n{lista_tuplas}")
