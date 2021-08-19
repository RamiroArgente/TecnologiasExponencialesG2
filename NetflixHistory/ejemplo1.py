from pprint import pprint

# Incluyo el script pprint de la libreria pprint
# nos permite printear cosas por consola de forma mas ordenada

# Creo una lista de titulos sacados a mano del csv y se la asigno a una variable titulos
titulos = ["Rick y Morty: Temporada 3: Descanso y Ricklajación", "Rick y Morty: Temporada 4: Un tren de antologías", "Community: Temporada 2: Accounting for Lawyers", "Community: Temporada 2: Conspiracy Theories and Interior Design", "Community: Temporada 2: Cooperative Calligraphy", "Community: Temporada 2: Celebrity Pharmacology", "Community: Temporada 3: Biología básica", "Community: Temporada 4: Introducción avanzada a la finalidad", "Community: Temporada 4: Orígenes heroicos", "Rick y Morty: Temporada 4: Aprovechando el mortymento: Vive, muere, Rickpeat","Marvel - Daredevil: Temporada 2: La oscuridad al final del túnel", "Marvel - Daredevil: Temporada 2: .380"]

# La muestro por consola
pprint(titulos)

# Instancio una variable contador en 0
cont = 0

# Itero por cada titulo de mi lista titulos
for titulo in titulos:
	# Divido el titulo en los caracteres ":"
        t_s = titulo.split(":")
        # Obtengo una lista, como vimos en clase, si el titulo contiene 2 o mas ":" podemos decir que es una serie
		if len(t_s) > 2:
			# Si el titulo de la serie ingresado coincide con "Community"
			if t_s[0] == "Community":
				cont += 1
            	# Sumo 1 a mi contador (El operador ++ no existe en python)

# Muestro el resultado

print("Viste " + str(cont) + " capitulos de Community")