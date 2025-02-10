# EJERCICIO 7
# Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
    # El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    # La función recibe un listado que contiene pares, representando cada jugada.
    # El par puede contener combinaciones de "R" (piedra), "P" (papel)  o "S" (tijera).
    # Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

def comprobarGanador(ronda1, ronda2, ronda3):
    puntos1 = 0
    puntos2 = 0

    # RONDA 1
    if(ronda1[0] == ronda1[1]):
        puntos1 = 0
    elif(ronda1[0] == "R" and ronda1[1] == "S" or 
         ronda1[0] == "P" and ronda1[1] == "R" or
         ronda1[0] == "S" and ronda1[1] == "P"):
        puntos1 = puntos1 + 1
    else:
        puntos2 = puntos2 + 1
    
    # RONDA 2
    if(ronda2[0] == ronda2[1]):
        puntos1 = 0
    elif(ronda2[0] == "R" and ronda2[1] == "S" or 
         ronda2[0] == "P" and ronda2[1] == "R" or
         ronda2[0] == "S" and ronda2[1] == "P"):
        puntos1 = puntos1 + 1
    else:
        puntos2 = puntos2 + 1

    # RONDA 3
    if(ronda3[0] == ronda3[1]):
        puntos1 = 0
    elif(ronda3[0] == "R" and ronda3[1] == "S" or 
         ronda3[0] == "P" and ronda3[1] == "R" or
         ronda3[0] == "S" and ronda3[1] == "P"):
        puntos1 = puntos1 + 1
    else:
        puntos2 = puntos2 + 1

    if(puntos1 == puntos2):
        return "¡EMPATE!"
    elif(puntos1 > puntos2):
        return "GANADOR: ¡JUGADOR 1!"
    else:
        return "GANADOR: ¡JUGADOR 2!"
    

def comprobarJugadas(jug1Rond1, jug2Rond1, jug1Rond2, jug2Rond2, jug1Rond3, jug2Rond3):

    ronda1Correcta = False
    ronda2Correcta = False
    ronda3Correcta = False
    esCorrecta = False

    if((jug1Rond1.upper() == "R" or jug1Rond1.upper() == "P" or 
        jug1Rond1.upper() == "S") and (jug2Rond1.upper() == "R" or 
        jug2Rond1.upper() == "P" or jug2Rond1.upper() == "S")):
        ronda1Correcta = True

    if ((jug1Rond2.upper() == "R" or jug1Rond2.upper() == "P" or 
        jug1Rond2.upper() == "S") and (jug2Rond2.upper() == "R" or 
        jug2Rond2.upper() == "P" or jug2Rond2.upper() == "S")):
        ronda2Correcta = True

    if ((jug1Rond3.upper() == "R" or jug1Rond3.upper() == "P" or 
        jug1Rond3.upper() == "S") and (jug2Rond3.upper() == "R" or 
        jug2Rond3.upper() == "P" or jug2Rond3.upper() == "S")):
        ronda3Correcta = True

    if(ronda1Correcta == True and ronda2Correcta == True and ronda3Correcta == True):
        esCorrecta = True
        return esCorrecta
    else:
        return esCorrecta


# ----------------------------------------------------------------------------------------------------------------------------


# BUCLE DO WHILE
while True:

    print("--- RONDA 1 ---")
    jug1Rond1 = input("JUGADOR 1: ¡PIEDRA (R), PAPEL (P), TIJERAS (S)!\n")
    jug2Rond1 = input("JUGADOR 2: ¡PIEDRA (R), PAPEL (P), TIJERAS (S)!\n")

    print("\n--- RONDA 2 ---")
    jug1Rond2 = input("JUGADOR 1: ¡PIEDRA (R), PAPEL (P), TIJERAS (S)!\n")
    jug2Rond2 = input("JUGADOR 2: ¡PIEDRA (R), PAPEL (P), TIJERAS (S)!\n")

    print("\n--- RONDA 3 ---")
    jug1Rond3 = input("JUGADOR 1: ¡PIEDRA (R), PAPEL (P), TIJERAS (S)!\n")
    jug2Rond3 = input("JUGADOR 2: ¡PIEDRA (R), PAPEL (P), TIJERAS (S)!\n")


    if(comprobarJugadas(jug1Rond1, jug2Rond1, jug1Rond2, jug2Rond2, jug1Rond3, jug2Rond3) == True):
        break
    
    else:
        print("\n\nSÓLO SE PUEDE SEGUIR EL SIGUIENTE PATRÓN:\n" +
              " - Piedra:  R\n" +
              " - Papel:   P\n" +
              " - Tijeras: S\n\n")


ronda1 = list()
ronda2 = list()
ronda3 = list()

ronda1.append(jug1Rond1.upper())
ronda1.append(jug2Rond1.upper())

ronda2.append(jug1Rond2.upper())
ronda2.append(jug2Rond2.upper())

ronda3.append(jug1Rond3.upper()) 
ronda3.append(jug2Rond3.upper())

print("\n" + comprobarGanador(ronda1, ronda2, ronda3))
