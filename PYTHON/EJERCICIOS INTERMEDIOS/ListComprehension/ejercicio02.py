# EJERCICIO 2
# Encuentra todos los números del 1 al 1000 que incluyan entre sus cifras al menos un 3.

lista_numeros = list(range(1, 1000))
lista_numeros_str = list(map(str, lista_numeros))

listaNumerosFiltrados = list(n for n in lista_numeros_str if "3" in n)

print(f"Lista de todos los números del 1 al 1000 que incluyen entre sus cifras al menos un 3:\n{listaNumerosFiltrados}")
