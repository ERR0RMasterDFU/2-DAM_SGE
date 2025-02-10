# EJERCICIO 1
# Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
    # Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
    # En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
    # El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

listaConversion = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"_....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    " ":"  " 
    }


texto = input("Por favor introduzca el contenido que quiere traducir.\n")

listaConversionALetras= {v: k for k, v in listaConversion.items()}

listaSimbolos = list(texto.upper()) # Texto convertido en lista.
listaTextoConvertido = list()       # Lista vacía en la que se guardará la conversión.
listaConversionValores = listaConversion.values()
delimitador = ""


if texto.startswith("-") or texto.startswith("."):
    palabras = texto.split("  ")  # Divide en palabras si hay 2 veces espacio.
    for palabra in palabras:
        letras = palabra.split(" ")  # Divide palabras en letras usando un espacio.
        for letra in letras:
            if letra in listaConversionALetras:
                listaTextoConvertido.append(listaConversionALetras[letra])  # Letra correspondiente.
        listaTextoConvertido.append(" ")  # Espacio.
                
    print("\nTRADUCCIÓN A NATURAL: " + delimitador.join(listaTextoConvertido))

else:
    for simbolo in listaSimbolos:
        for conversion in listaConversion:            
            if(simbolo == conversion):
                if(simbolo == " "):
                    listaTextoConvertido.append(" ")
                else:
                    listaTextoConvertido.append(listaConversion.get(simbolo))
                    listaTextoConvertido.append(" ")

    print("\nTRADUCCIÓN EN MORSE: " + delimitador.join(listaTextoConvertido))
    