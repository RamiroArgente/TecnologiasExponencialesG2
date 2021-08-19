import csv
# incluyo la libreria "csv" en mi script

# Tomo el titulo a contabilizar 
serie = input("Ingrese la serie que quiere contar: ")

# Abro el archivo .csv
with open('NetflixViewingHistory.csv') as csv_file:
    # Lo vuelvo legible
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Instancio un contador en 0
    cont = 0

    # Comienzo a iterar por las filas del csv
    for fila in csv_reader:
    	# Cada fila es una lista del tipo Lista[str, str]
        # En la que la primera posicion es el titulo, y la segunda la fecha

        # Asigno el primer elemento de la fila a una variable "titulo".
        titulo = fila[0]

        # Divido el titulo en los caracteres ":"
        t_s = t.split(":")
        # Obtengo una lista, como vimos en clase, si el titulo contiene 2 o mas ":" podemos decir que es una serie
		if len(t_s) > 2:
			# Si el titulo de la serie ingresado coincide con este
			if t_s[0] == serie:
				cont += 1
            	# Sumo 1 a mi contador (El operador ++ no existe en python)

print("Viste " + str(cont) + " capitulos de " + serie)