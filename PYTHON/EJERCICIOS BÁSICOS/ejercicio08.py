# EJERCICIO 8
# ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron contra otras bondadosas 
# que no quieren que el mal reine sobre sus tierras. Cada raza tiene asociado un "valor" entre 1 y 5:
    # Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),  Númenóreanos (4), Elfos (5)
    # Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),  Huargos (3), Trolls (5)

# Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
    # El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la suma del valor del ejército y el número de integrantes.
    # Cada ejército puede estar compuesto por un número de integrantes variable  de cada raza.
    # Tienes total libertad para modelar los datos del ejercicio.

# Ej: 1 Peloso pierde contra 1 Orco
    # 2 Pelosos empatan contra 1 Orco
    # Pelosos ganan a 1 Orco

import random

def calcularDinero (x):
    for var in range(x):
        numAleatorio = random.randint(1,8)
    
    return numAleatorio*20

def calcularDescuento (d):
    for var in range(d):
        numAleatorio = random.randint(0,5)
    
    return numAleatorio*10

def aplicarDescuento (p, descuento):
    return int(p - (p * (descuento/100)))

#---------------------------------------------------------------------------------------------------------------------------------------------

puntuacionEjercitoBien = 0
puntuacionEjercitoMal = 0

precioUnidad1 = 10
precioUnidad2 = 20
precioUnidad3 = 30
precioUnidad4 = 40
precioUnidad5 = 50

print("¡LA TIERRA MEDIA ESTÁ EN GUERRA! Y sólo un honorable estratega como tú puede salvarnos...")
print("(Cuando vea este símbolo (>) pulse 'Enter' para seguir con el diálogo.)")
input("(>)")

input("\nGANDALF: Me presento, soy Gandalf, uno de los 5 istari a cargo de combatir a esa peste de Sauron que se cierne"+
      " sobre nosotros. (>)")
input("\nSAURON: Mua ja ja, muy inteligente, Gandalf, pero no creas que va ser cosa fácil ¡Yo también tengo un estratega!"+
      "¡MI PODER ACABARÁ CON VOSOTROS! (>)")

input("\nGANDALF: Me da que va llegando la hora de pegarse... ¡MÁS OS VALE CORRER, INSENSATOS! (>)")
input("\nSAURON: Lo mismo te digo, fósil decrépito. (>)")

print("\n--------------------------------------------------------------------------------------------------------------------------")

input("""
*********************************************************
TURNO DEL ESTRATEGA DEL BIEN (JUGADOR 1)
*********************************************************
(>)
""")

try:
    b1 = int(input("GANDALF: Muy bien, es hora de que nos guíes, golpea mi bastón las veces que quieras..."))
    dineroBien = calcularDinero(b1)
    print(f"HAS OBTENIDO: {dineroBien} €.")
except:
    print("Te caes intentando dar el golpe...")
    dineroBien = calcularDinero(1)
    print(f"HAS OBTENIDO: {dineroBien} €.")

try:
    b2 = int(input("\nGANDALF: Y ahora grita ¡POR LAS RAZAS BONDADOSAS! las veces que creas..."))
    descuentoBien = (calcularDescuento(b2))
    print(f"HAS OBTENIDO UN DESCUENTO DEL: {descuentoBien} %.")
except:
    print("Te ahogas intentando gritar y terminas tosiendo...")
    descuentoBien = (calcularDescuento(1))
    print(f"HAS OBTENIDO UN DESCUENTO DEL: {descuentoBien} %.")

input("(>)")

precioUnidad1Final = aplicarDescuento(precioUnidad1, descuentoBien)
precioUnidad2Final = aplicarDescuento(precioUnidad2, descuentoBien)
precioUnidad3Final = aplicarDescuento(precioUnidad3, descuentoBien)
precioUnidad4Final = aplicarDescuento(precioUnidad4, descuentoBien)
precioUnidad5Final = aplicarDescuento(precioUnidad5, descuentoBien)

print(f"""
---------------------------------------------------------
Crea el ejército del BIEN ¡ELIGE TUS TROPAS!
---------------------------------------------------------
DINERO: {dineroBien} €
DESCUENTO: {descuentoBien} %
---------------------------------------------------------
1 ->    {precioUnidad1Final} € - Peloso
2 ->    {precioUnidad2Final} € - Sureño bueno
3 ->    {precioUnidad3Final} € - Enano
4 ->    {precioUnidad4Final} € - Númenoreano
5 ->    {precioUnidad5Final} € - Elfo
---------------------------------------------------------
""")

while dineroBien >= precioUnidad1Final:

    try:
        tropaElegida = int(input())
    except:
        tropaElegida = 1
        print(f"Resultas inentendible... Contratas a un Peloso por error...")

    if tropaElegida == 1 and dineroBien >= precioUnidad1Final:
        puntuacionEjercitoBien += 1
        dineroBien -= precioUnidad1Final
        print(f"Has contratado a un Peloso.")
    elif tropaElegida == 2 and dineroBien >= precioUnidad2Final:
        puntuacionEjercitoBien += 2
        dineroBien -= precioUnidad2Final
        print(f"Has contratado a un Sureño bueno.")
    elif tropaElegida == 3 and dineroBien >= precioUnidad3Final:
            puntuacionEjercitoBien += 3
            dineroBien -= precioUnidad3Final
            print(f"Has contratado a un Enano.")
    elif tropaElegida == 4 and dineroBien >= precioUnidad4Final:
            puntuacionEjercitoBien += 4
            dineroBien -= precioUnidad4Final
            print(f"Has contratado a un Númenoreano.")
    elif tropaElegida == 5 and dineroBien >= precioUnidad5Final:
            puntuacionEjercitoBien += 5
            dineroBien -= precioUnidad5Final
            print(f"Has contratado a un Elfo.")
    elif tropaElegida == 5 and dineroBien >= precioUnidad5Final:
            puntuacionEjercitoBien += 5
            dineroBien -= precioUnidad5Final
            print(f"Has contratado a un Elfo.")
    elif tropaElegida == 0 or tropaElegida > 5:
        puntuacionEjercitoBien += 1
        dineroBien -= precioUnidad1Final
        print(f"No hay ninguna tropa con ese número asignado... A cambio, contratas a un Peloso.")
        print(f"Has contratado a un Peloso.")
    else:
        puntuacionEjercitoBien += 1
        dineroBien -= precioUnidad1Final
        print(f"No tienes suficiente dinero para contratar esa unidad... A cambio, contratas a un Peloso.")
        print(f"Has contratado a un Peloso.")
    
    print(f"Dinero restante: {dineroBien} €.\n")

print(puntuacionEjercitoBien)

print("\n--------------------------------------------------------------------------------------------------------------------------")

input("""
*********************************************************
TURNO DEL ESTRATEGA DEL MAL (JUGADOR 2)
*********************************************************
(>)
""")

try:
    b1 = int(input("SAURON: ¡Mua ja ja! Como prueba de que el mal se alzará victorioso, besa mi anillo único las veces que desees..."))
    dineroMal = calcularDinero(b1)
    print(f"HAS OBTENIDO: {dineroMal} €.")
except:
    print("Le escupes al anillo sin querer... Sauron te mira con asco...")
    dineroMal = calcularDinero(1)
    print(f"HAS OBTENIDO: {dineroMal} €.")

try:
    b2 = int(input("\nSAURON: Bien, ahora grita ¡MELKOR, PRÉSTANOS TU FUERZA! las veces que necesites..."))
    descuentoMal = (calcularDescuento(b2))
    print(f"HAS OBTENIDO UN DESCUENTO DEL: {descuentoMal} %.")
except:
    print("Pegas un chillido que le deja sordo a Sauron...")
    descuentoMal = (calcularDescuento(1))
    print(f"HAS OBTENIDO UN DESCUENTO DEL: {descuentoMal} %.")

input("(>)")

precioUnidad1Final = aplicarDescuento(precioUnidad1, descuentoMal)
precioUnidad2Final = aplicarDescuento(precioUnidad2, descuentoMal)
precioUnidad3Final = aplicarDescuento(precioUnidad3, descuentoMal)
precioUnidad4Final = aplicarDescuento(precioUnidad4, descuentoMal)
precioUnidad5Final = aplicarDescuento(precioUnidad5, descuentoMal)

print(f"""
---------------------------------------------------------
Crea el ejército del MAL ¡ELIGE TUS TROPAS!
---------------------------------------------------------
DINERO: {dineroMal} €
DESCUENTO: {descuentoMal} %
---------------------------------------------------------
1 ->    {precioUnidad1Final} € - Sureño malo
2 ->    {precioUnidad2Final} € - Orco
3 ->    {precioUnidad3Final} € - Goblin
4 ->    {precioUnidad4Final} € - Huargo
5 ->    {precioUnidad5Final} € - Troll
---------------------------------------------------------
""")

while dineroMal >= precioUnidad1Final:

    try:
        tropaElegida = int(input())
    except:
        tropaElegida = 1
        print(f"Te trabas hablando... Contratas a un Sureño malo por error...")

    if tropaElegida == 1 and dineroMal >= precioUnidad1Final:
        puntuacionEjercitoMal += 1
        dineroMal -= precioUnidad1Final
        print(f"Has contratado a un Sureño malo.")
    elif tropaElegida == 2 and dineroMal >= precioUnidad2Final:
        puntuacionEjercitoMal += 2
        dineroMal -= precioUnidad2Final
        print(f"Has contratado a un Orco.")
    elif tropaElegida == 3 and dineroMal >= precioUnidad3Final:
            puntuacionEjercitoMal += 3
            dineroMal -= precioUnidad3Final
            print(f"Has contratado a un Goblin.")
    elif tropaElegida == 4 and dineroMal >= precioUnidad4Final:
            puntuacionEjercitoMal += 4
            dineroMal -= precioUnidad4Final
            print(f"Has contratado a un Huargo.")
    elif tropaElegida == 5 and dineroMal >= precioUnidad5Final:
            puntuacionEjercitoMal += 5
            dineroMal -= precioUnidad5Final
            print(f"Has contratado a un Troll.")
    elif tropaElegida == 0 or tropaElegida > 5:
        puntuacionEjercitoMal += 1
        dineroMal -= precioUnidad1Final
        print(f"Lees mal los números del cartel... Contratas a un Sureño malo... Sauron te mira raro...")
        print(f"Has contratado a un Sureño malo.")
    else:
        puntuacionEjercitoMal += 1
        dineroMal -= precioUnidad1Final
        print(f"No tienes suficiente dinero para contratar esa unidad... Se te acerca un Sureño malo y lo contratas...")
        print(f"Has contratado a un Sureño malo.")
    
    print(f"Dinero restante: {dineroMal} €.\n")

print(puntuacionEjercitoMal)

print("\n--------------------------------------------------------------------------------------------------------------------------")

input("""
-------------------------------------------------------------
LA BATALLA POR EL DESTINO DE LA TIERRA MEDIA HA COMENZADO...
-------------------------------------------------------------
(>)
""")

input("El ejército del BIEN tiene un total de... (>)")
input(f"¡{puntuacionEjercitoBien} PUNTOS DE VALOR!")  

input("\ny el ejército del MAL tiene un total de... (>)")
input(f"¡{puntuacionEjercitoMal} PUNTOS DE MALDAD!") 

if puntuacionEjercitoBien > puntuacionEjercitoMal:
    print("""
******************************************************************
EL BIEN HA PROTEGIDO LA TIERRA MEDIA ¡EL GANADOR ES EL JUGADOR 1!
******************************************************************
""")
    print("GANDALF: ¡Bien hecho! Esperemos que esta sea la última vez que Sauron vuelva, que insensato...")
elif puntuacionEjercitoMal > puntuacionEjercitoBien:
    print("""
***********************************************************************
EL MAL SE HA APODERADO DE LA TIERRA MEDIA ¡EL GANADOR ES EL JUGADOR 2!
***********************************************************************
""")
    print("SAURON: ¡Por fin está de vuelta el amo y señor del mundo! ¡Mua ja ja ja ja!... Ah, y gracias por el trabajo, Ahem...")
else:
    print("""
*******************************************************************
AMBOS EJÉRCITOS SON IGUAL DE PODEROSOS ¡EL RESULTADO ES UN EMPATE!
*******************************************************************
""")
    print("GANDALF: Dejémoso en tablas por una vez Sauron, estoy cansado...")
    print("SAURON: Que asco y que rabia, pero acepto el empate ¡la próxima vez no tendrás tanta suerte! ¡Vejestorio!...")
    print("GANDALF: Anda que no se lo tiene creído...")
