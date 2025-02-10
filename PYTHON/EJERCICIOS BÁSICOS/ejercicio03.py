# EJERCICIO 3
# Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
    # out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
    # out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

def devolverOtraCadena(str1, str2):

    for letra in list1:
        if(letra in str1 and letra not in str2):
            if(letra not in nuevaList1):
                nuevaList1.append(letra)
    
    for letra in list2:
        if(letra in str2 and letra not in str1):
            if(letra not in nuevaList2):
                nuevaList2.append(letra)

    return print("\nOUTPUT 1: " + delimitador.join(nuevaList1) + 
                 "\nOUTPUT 2: " + delimitador.join(nuevaList2))


# ----------------------------------------------------------------------------------------------------------------------------


str1 = input("Introduzca la primera cadena.\n").upper()
str2 = input("\nIntroduzca la segunda cadena.\n").upper()

list1 = list(str1)
list2 = list(str2)
nuevaList1 = list()
nuevaList2 = list()
delimitador = ""

devolverOtraCadena(str1, str2)
