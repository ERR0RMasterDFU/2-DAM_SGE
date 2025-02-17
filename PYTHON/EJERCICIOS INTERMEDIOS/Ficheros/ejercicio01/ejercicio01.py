# EJERCICIO 1
# Utilizando el fichero notas.txt, realiza un programa en python que lea los datos de ese 
# fichero y construya la siguiente estructura:

    # alumnos = [ 
    #              {"nombre":"Daniel", "apellidos":"Fustero López", "curso": "1A","notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBG":6}},
    #              {"nombre":"Rafaela", ... },...
    # ]
    
# Crea un programa que muestre un menú y puedas elegir una de estas opciones:
    # Muestra el listado de los alumnos con la nota media que han sacado. 
    # Utiliza una función para realizar el cálculo de la nota media.
    # Pide un curso y una asignatura y muestre una lista de los alumnos de ese curso con las notas en esa asignatura.
    # Pide un curso y muestre el porcentaje de aprobados por cada asignatura.
    # Pide un curso, y crea un fichero nombredelcurso.txt con los alumnos y la nota media.

# notas_file = open("EJERCICIOS INTERMEDIOS/Ficheros/ejercicio01/notas.txt", "r+", encoding="utf-8")

# contenido_txt = notas_file.read()

# print(contenido_txt)

# notas_file

""" EJERCICIO REALIZADO CON MUCHA AYUDA DE PÁGINAS EXTERNAS E IAs GENERATIVAS."""

import csv

def cargar_datos(nombre_archivo):
    alumnos = []
    try:
        archivo = open("Ficheros/ejercicio01/notas.txt", "r+", encoding="utf-8")
        lector = csv.reader(archivo)
        encabezados = next(lector)
        for fila in lector:
            alumno = {}
            alumno["nombre"] = fila[1].strip()
            alumno["apellidos"] = fila[0].strip()
            alumno["curso"] = fila[2].strip()
            alumno["notas"] = {}
            alumno["notas"]["FH"] = int(fila[3])
            alumno["notas"]["LM"] = int(fila[4])
            alumno["notas"]["ISO"] = int(fila[5])
            alumno["notas"]["FOL"] = int(fila[6])
            alumno["notas"]["PAR"] = int(fila[7])
            alumno["notas"]["SGBD"] = int(fila[8])
            alumnos.append(alumno)
        archivo.close()
    except:
        print("Error al leer el archivo")
    return alumnos

def calcular_media(notas):
    suma = 0
    cantidad = 0
    for materia in notas:
        suma += notas[materia]
        cantidad += 1
    return suma / cantidad

def mostrar_listado(alumnos):
    for i in range(len(alumnos)):
        alumno = alumnos[i]
        media = calcular_media(alumno["notas"])
        print(alumno["nombre"] + " " + alumno["apellidos"] + " - Media: " + str(round(media, 2)))

def filtrar_por_curso_asignatura(alumnos, curso, asignatura):
    for i in range(len(alumnos)):
        alumno = alumnos[i]
        if alumno["curso"] == curso:
            print(alumno["nombre"] + " " + alumno["apellidos"] + ": " + str(alumno["notas"][asignatura]))

def porcentaje_aprobados(alumnos, curso):
    aprobados = {}
    total = {}
    for materia in ["FH", "LM", "ISO", "FOL", "PAR", "SGBD"]:
        aprobados[materia] = 0
        total[materia] = 0
    for i in range(len(alumnos)):
        alumno = alumnos[i]
        if alumno["curso"] == curso:
            for materia in alumno["notas"]:
                total[materia] += 1
                if alumno["notas"][materia] >= 5:
                    aprobados[materia] += 1
    for materia in aprobados:
        if total[materia] > 0:
            porcentaje = (aprobados[materia] / total[materia]) * 100
        else:
            porcentaje = 0
        print(materia + ": " + str(round(porcentaje, 2)) + "% aprobados")

def guardar_notas_curso(alumnos, curso):
    try:
        archivo = open(curso + ".txt", "w", encoding="utf-8")
        for i in range(len(alumnos)):
            alumno = alumnos[i]
            if alumno["curso"] == curso:
                media = calcular_media(alumno["notas"])
                archivo.write(alumno["nombre"] + " " + alumno["apellidos"] + " - Media: " + str(round(media, 2)) + "\n")
        archivo.close()
    except:
        print("Error al guardar el archivo")

def menu():
    alumnos = cargar_datos("notas.txt")
    while True:
        print("\nOPCIONES:")
        print("1. Listado de alumnos con nota media")
        print("2. Mostrar alumnos de un curso con nota en una asignatura")
        print("3. Porcentaje de aprobados por asignatura en un curso")
        print("4. Guardar notas medias de un curso en un fichero")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            mostrar_listado(alumnos)
        elif opcion == "2":
            curso = input("Introduce el curso: ")
            asignatura = input("Introduce la asignatura: ")
            filtrar_por_curso_asignatura(alumnos, curso, asignatura)
        elif opcion == "3":
            curso = input("Introduce el curso: ")
            porcentaje_aprobados(alumnos, curso)
        elif opcion == "4":
            curso = input("Introduce el curso: ")
            guardar_notas_curso(alumnos, curso)
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
