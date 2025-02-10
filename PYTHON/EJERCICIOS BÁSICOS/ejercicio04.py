# EJERCICIO 4
# Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
    # No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def capitalizarTexto(texto):

    palabras = texto.split(" ")

    for palabra in palabras:
        textoCapitalizado.append(palabra[0].upper() + palabra.removeprefix(palabra[0]))
        
    return print("\n" + delimitador.join(textoCapitalizado))


# ----------------------------------------------------------------------------------------------------------------------------


texto = input("Introduzca el texto que desea capitalizar.\n")
textoCapitalizado = list()
delimitador = " "

capitalizarTexto(texto)
