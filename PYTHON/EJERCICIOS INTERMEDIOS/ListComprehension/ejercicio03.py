# EJERCICIO 3
# Contar el número de espacios en una cadena.

cadena = input("Por favor, introduzca la cadena de texto que quiera.\n")

lista_cadena = list(cadena)
lista_espacios = list(c for c in lista_cadena if c == " ")

print(f"\nEl número de espacios que hay en la cadena es: {len(lista_espacios)}")
