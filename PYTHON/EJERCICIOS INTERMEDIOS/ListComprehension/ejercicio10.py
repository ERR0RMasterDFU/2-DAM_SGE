# EJERCICIO 10
# Encuentra todas las palabras en una cadena que tengan menos de 4 letras.

cadena = input("Por favor, introduzca la cadena que quiera.\n")
lista_cadena = cadena.split(" ")

lista_palabras_cortas = list(p for p in lista_cadena if len(p) < 4)

print(f"\nLista de todas las palabras que tienen menos de 4 letras:\n{lista_palabras_cortas}")
