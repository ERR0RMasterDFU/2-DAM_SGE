# EJERCICIO 2
# Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
    # Equilibrado significa que estos delimitadores se abren y cierran en orden y de forma correcta.
    # Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
    # Expresión balanceada: { [ a * ( c + d ) ] - 5 }
    # Expresión no balanceada: { a * ( c + d ) ] - 5 }

def comprobarBalanceExpresion (listaCaracteres):

    listaDelimitadores = list()
    pilaDelimitadores = list()

    for var in listaCaracteres:
        if(var == "[" or var == "]" 
           or var == "(" or var == ")" 
           or var == "{" or var == "}"):
            
            listaDelimitadores.append(var)

    #print(listaDelimitadores)

    for i, valor in enumerate(listaDelimitadores):
        if(valor == "["):
            pilaDelimitadores.append("]")
        elif (valor == "{"):
            pilaDelimitadores.append("}")
        elif (valor == "("):
            pilaDelimitadores.append(")")
        
        if(valor == "]"):
            if(valor == pilaDelimitadores[len(pilaDelimitadores)-1]):
                pilaDelimitadores.pop(len(pilaDelimitadores)-1)
            else:
                break
        elif(valor == "}"):
            if(valor == pilaDelimitadores[len(pilaDelimitadores)-1]):
                pilaDelimitadores.pop(len(pilaDelimitadores)-1)
            else:
                break
        elif(valor == ")"):
            if(valor == pilaDelimitadores[len(pilaDelimitadores)-1]):
                pilaDelimitadores.pop(len(pilaDelimitadores)-1)
            else:
                break


    if(listaDelimitadores):
        if(not pilaDelimitadores):
            print("\nLa expresión introducida está BALANCEADA.")
        else:
            print("\nLa expresión introducida NO está balanceada.")
    else:
        print("\nLa expresión introducida carece de delimitadores.")

#---------------------------------------------------------------------------------------------------------------------

expresion = input("Introduzca la expresión que desee:\n")

listaCaracteres = list(expresion)

comprobarBalanceExpresion(listaCaracteres)
