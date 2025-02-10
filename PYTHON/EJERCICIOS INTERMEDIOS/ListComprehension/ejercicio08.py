# EJERCICIO 8
# Dado numbers = range(20), se genera una lista que contiene la palabra "par" si 
# un número en los números es par, y la palabra "impar" si el número es impar. El 
# resultado se vería así: "impar", "impar", "par".

numbers = range(20)

lista_par_impar = list("par" if n%2 == 0 else "impar" for n in numbers)

print(f"Lista de números en pares e impares:\n{lista_par_impar}")
