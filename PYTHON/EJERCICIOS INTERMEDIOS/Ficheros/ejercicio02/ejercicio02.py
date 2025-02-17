# EJERCICIO 2 
# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 
# con las siguientes columnas: 
    # Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
    # Máximo (precio máximo de la acción durante la jornada), 
    # Mínimo (precio mínimo de la acción durante la jornada), 
    # Volumen (Volumen al cierre de bolsa), 
    # Efectivo (capitalización al cierre en miles de euros).

# Construir una función reciba el fichero de cotizaciones y devuelva un diccionario 
# con los datos del fichero por columnas.
# Construir una función que reciba el diccionario devuelto por la función anterior y 
# cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.

""" EJERCICIO REALIZADO CON MUCHA AYUDA DE PÁGINAS EXTERNAS E IAs GENERATIVAS."""

import csv

def leer_cotizaciones(fichero):
    datos = {}

    # Inicialización de las listas vacías para cada columna
    datos["Nombre"] = []
    datos["Final"] = []
    datos["Máximo"] = []
    datos["Mínimo"] = []
    datos["Volumen"] = []
    datos["Efectivo"] = []

    # Abrir el archivo CSV en modo lectura
    archivo_csv = open(fichero, "r", encoding="utf-8")
    lector = csv.reader(archivo_csv, delimiter=';')

    # Leer la primera fila manualmente (encabezados)
    encabezados = next(lector)
    print("Encabezados del archivo CSV:", encabezados)

    # Recorrer el archivo línea por línea
    for fila in lector:
        print("Fila actual:", fila)

        # Extraer valores de la fila y convertirlos a los tipos adecuados
        nombre = fila[0]
        precio_final = fila[1].replace(',', '.')
        precio_maximo = fila[2].replace(',', '.')
        precio_minimo = fila[3].replace(',', '.')
        volumen = fila[4].replace('.', '')
        efectivo = fila[5].replace(',', '.').replace('.', '')

        # Agregar valores convertidos a las listas del diccionario
        datos["Nombre"].append(nombre)
        datos["Final"].append(float(precio_final))
        datos["Máximo"].append(float(precio_maximo))
        datos["Mínimo"].append(float(precio_minimo))
        datos["Volumen"].append(int(volumen))
        datos["Efectivo"].append(float(efectivo))

    # Cerrar el archivo
    archivo_csv.close()
    
    return datos

def calcular_estadisticas(datos):
    estadisticas = []

    # Recorrer cada columna numérica
    for columna in ["Final", "Máximo", "Mínimo", "Volumen", "Efectivo"]:
        valores = datos[columna]  # Obtener la lista de valores

        # Calcular mínimo, máximo y media con bucles básicos
        min_valor = valores[0]
        max_valor = valores[0]
        suma = 0
        contador = 0

        for valor in valores:
            if valor < min_valor:
                min_valor = valor
            if valor > max_valor:
                max_valor = valor
            suma += valor
            contador += 1

        media_valor = suma / contador  # Calcular media manualmente

        # Crear un diccionario con los resultados
        resultado = {}
        resultado["Columna"] = columna
        resultado["Mínimo"] = min_valor
        resultado["Máximo"] = max_valor
        resultado["Media"] = media_valor

        # Agregar a la lista de estadísticas
        estadisticas.append(resultado)

    return estadisticas

def escribir_estadisticas(estadisticas, fichero_salida):
    # Abrir archivo CSV en modo escritura
    f = open(fichero_salida, mode='w', newline='', encoding='utf-8')
    escritor = csv.writer(f)

    # Escribir encabezados manualmente
    escritor.writerow(["Columna", "Mínimo", "Máximo", "Media"])

    # Escribir cada fila de estadísticas
    for estadistica in estadisticas:
        escritor.writerow([estadistica["Columna"], estadistica["Mínimo"], estadistica["Máximo"], estadistica["Media"]])

    # Cerrar el archivo
    f.close()

def main():
    datos = leer_cotizaciones("Ficheros/ejercicio02/cotizacion.csv")
    estadisticas = calcular_estadisticas(datos)
    escribir_estadisticas(estadisticas, "estadisticas_cotizacion.csv")

if __name__ == "__main__":
    main()
