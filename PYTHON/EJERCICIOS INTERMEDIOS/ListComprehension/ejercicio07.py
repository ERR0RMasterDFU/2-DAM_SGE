# EJERCICIO 7
# Obtén solamente los números en una oración como:
    # 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'.

frase = "En 1984 hubo 13 casos de protesta con más de 1000 asistentes"

lista_frase = frase.split(" ")
lista_numeros = [e for e in lista_frase if e.isdigit()]

print(f"Lista con los números de la oración: {lista_numeros}")


# ACLARACIÓN: La función "isdigit()" la he descubierto mirando los métodos de "e." buscando 
#             si había alguna forma de identificar el número de un string, y me topé con
#             "isdigit()" e "isdecimal()". Leí lo que hacía el primero dejando la flechita
#             del ratón encima y decidí usuarlo. 
