# EJERCICIO 9
# Generar una lista de tuplas que consten únicamente de los números coincidentes en estas listas:
    # list_a = 1, 2, 3, 4, 5, 6, 7, 8, 9
    # list_b = 2, 7, 1, 12. 
    # El resultado se vería así (4,4), (12,12).

def detectar_numeros_repetidos(list_a, list_b):
    for na in list_a:
        for nb in list_b:
            if(na == nb):
                lista_num_rep.append(na)


# ----------------------------------------------------------------------------------------------------------------------------


list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12] 
lista_num_rep = []

detectar_numeros_repetidos(list_a, list_b)

lista_tuplas = list(tuple([n, n]) for n in lista_num_rep)

print(f"Lista de tuplas con los números repetidos:\n{lista_tuplas}")
