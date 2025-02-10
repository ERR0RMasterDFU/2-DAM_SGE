# EJERCICIO 11
# Utiliza una comprensión de lista anidada para encontrar todos los números 
# del 1 al 1000 que sean divisibles por cualquier dígito excepto 1 (2-9).

lista_numeros = list(range(1, 1000))

lista_numeros_div = list(n for n in lista_numeros if 
                         n%2 == 0 or n%3 == 0 or 
                         n%4 == 0 or n%5 == 0 or 
                         n%6 == 0 or n%7 == 0 or 
                         n%8 == 0 or n%9 == 0)

print(f"Lista de los números que son divisibles por cualquier dígito excepto 1 (2-9):\n{lista_numeros_div}")
