import os

from ufos import lee_avistamientos
from ufos import duracion_total
from ufos import comentario_mas_largo
from ufos import indexa_formas_por_mes

# Test de la función lee_avistamientos -------------------------------------------------------------------

ruta_csv = os.path.join("..", "data", "ovnis.csv")

avistamientos = lee_avistamientos(ruta_csv)  #avistamientos = lee_avistamientos("Ufos\data\ovnis.csv")
for a in avistamientos:
    print(a)

# --------------------------------------------------------------------------------------------------------


#Test de la función duracion_total -----------------------------------------------------------------------

estados = ['in', 'nm', 'pa', 'wa']

for estado in estados:
    duracion = duracion_total(avistamientos, estado)
    print(f"Duración total de los avistamientos en {estado}: {duracion} segundos.")

# --------------------------------------------------------------------------------------------------------


# Test de la función comentario_mas_largo ----------------------------------------------------------------

anyo = input("Por favor, introduzca un año (4 dígitos): ")
palabra = input("Por favor, introduzca una palabra: ")
comentario_largo = comentario_mas_largo(avistamientos, anyo, palabra)

if isinstance(comentario_largo, str):
    print(comentario_largo)
else:
    print(f"El avistamiento con el comentario más largo de {anyo} incluyendo la palabra '{palabra}' es: {comentario_largo.comentarios}")

# --------------------------------------------------------------------------------------------------------


# Test de la función indexa_formas_por_mes ---------------------------------------------------------------

# Llamada a la función
resultado = indexa_formas_por_mes(avistamientos)

# Imprimir el resultado
for mes, formas in resultado.items():
    print(f"{mes}: {formas}")

# --------------------------------------------------------------------------------------------------------


# Test de la función avistamientos_fechas ----------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------


# Test de la función hora_mas_avistamientos --------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------






