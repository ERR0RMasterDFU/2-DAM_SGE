# EJERCICIO 6
# Crea una función que reciba dos array, un booleano y retorne un array.
    # Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
    # Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
    # No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def elegirBoleano(strBoleano):
    esVerdadero = True
    
    if(strBoleano.upper() == "V"):
        return esVerdadero
    else: 
        esVerdadero = False
        return esVerdadero
    

def recogerElementosDeArray(booleano, array1, array2):

    array3 = list()

    if(booleano is True):
        for elemento1 in array1:
            for elemento2 in array2:
                if(elemento1 == elemento2):
                    if(elemento1 not in array3):    
                        array3.append(elemento1)
    else:    
        for elemento1 in array1:
            if elemento1 not in array2:
                array3.append(elemento1)
        for elemento2 in array2:
            if elemento2 not in array1:
                array3.append(elemento2)

    return array3


# ----------------------------------------------------------------------------------------------------------------------------


elementos1 = input("Introduzca los elementos del primer array.\n")
elementos2 = input("\nIntroduzca los elementos del segundo array.\n")

array1 = elementos1.split(" ")
array2 = elementos2.split(" ")

# BUCLE DO WHILE
while True:
    
    strBoleano = input("\nElija una de los 2 opciones:" + 
                   "\nV - Ver elementos comunes de los dos array." +
                   "\nF - Ver elementos NO comunes de los dos array.\n")
    
    if(strBoleano.upper() == "V" or strBoleano.upper() == "F"):
        break
    else:
        print("\n\nPor favor, elija una de los dos opciones disponibles.")

print("")
print(recogerElementosDeArray(elegirBoleano(strBoleano), array1, array2))
