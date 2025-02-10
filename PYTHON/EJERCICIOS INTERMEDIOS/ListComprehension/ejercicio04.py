# EJERCICIO 4
# Crea una lista de todas las consonantes de la cadena “A los yaks amarillos les gusta gritar 
# y bostezar y ayer cantaban mientras comían ñames asquerosos”.

cadena = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"
list_cadena = list(cadena.lower())

lista_consonantes = list(c for c in list_cadena if c!="a" and c!="e" and c!="i" and c!="o" and c!="u" and c!=" ")

print(f"Lista de todas las consonantes de la cadena:\n{lista_consonantes}")
