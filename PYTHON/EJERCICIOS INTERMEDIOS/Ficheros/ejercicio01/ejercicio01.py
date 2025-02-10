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

notas_file = open("EJERCICIOS INTERMEDIOS/Ficheros/ejercicio01/notas.txt", "r+", encoding="utf-8")

contenido_txt = notas_file.read()

print(contenido_txt)

notas_file
