# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 1

# Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura:
# El área de un rectángulo se obtiene al multiplicar la base por la altura.

base = input('Por favor, dime la longitud de la base (m).')
altura = input('Por favor, dime la longitud de la altura (m).')

def area_rectangulo(base, altura):
    return float(base)*float(altura)

print('El área del rectángulo es de', round(area_rectangulo(base, altura),2), 'm2.')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 2

# Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio. 
# Calcula el área de un círculo de 5 de radio:

import math


radio = input('Por favor, introduzca la longitud del radio (cm).')

def area_circulo(radio):
    return math.pi*float(radio)**2

print('El área del círculo es de', round(area_circulo(radio),2), 'cm2.')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 3

# Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
    # - Si el primer número es mayor que el segundo, debe devolver 1.
    # - Si el primer número es menor que el segundo, debe devolver -1.
    # - Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

a = input('Por favor, introduzca el primer número (a).')
b = input('Por favor, introduzca el segundo número (b).')

def relacion(a, b):
    if(a>b):
        return 1
    elif(a<b):
        return -1
    else:
        return 0

print(relacion(a,b))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 4

# Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. 
# Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

a = input('Por favor, introduzca el primer número (a).')
b = input('Por favor, introduzca el segundo número (b).')

def intermedio(a,b):
    return (float(a)+float(b))/2

print('El punto intermedio de ambos números es ',intermedio(a,b),'.')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 5

# Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. 
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
    # - Devolver el límite inferior si el número es menor que éste
    # - Devolver el límite superior si el número es mayor que éste.
    # - Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10.

numero = input('Por favor, introduzca un número cualquiera.')
minimo = input('Por favor, introduzca un mínimo.')
maximo = input('Por favor, introduzca un máximo.')

def recortar(numero, minimo, maximo):
    if(numero<minimo):
        return minimo
    elif(numero>maximo):
        return maximo
    else:
        return numero
    
print(recortar(numero, minimo, maximo))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 6

# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
# La primera con los números pares y la segunda con los números impares.
# Para ordenar una lista automáticamente puedes utilizar el método .sort().

# pares, impares = separar([6,5,2,1,7])
# print(pares)
# print(impares)

# [2, 6]
# [1, 5, 7]

lista = [4,6,3,2,7,9,8,1]
pares = []
impares = []

def separar(lista):
    for numero in lista:
        if(numero%2==0):
            pares.append(numero)
        else:
            impares.append(numero)

    pares.sort()
    impares.sort()

    return pares, impares

pares, impares =  separar(lista)

print('NÚMEROS PARES:', pares)
print('NÚMEROS IMPARES:', impares)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------