import csv
from datetime import datetime
import sys

# Tomar los argumentos de la línea de comandos y asignarlos a variables.
argumentos = sys.argv
if len(argumentos) > 1:
	dni = argumentos[1]
	salida = argumentos[2].upper()
	tipo_de_cheque = argumentos[3].upper()
	estado = argumentos[4].upper()
	rango_fecha = argumentos[5].upper()
# Imprimiendo el mensaje de error y poniendo las variables en valores por defecto.
else:
	print('debe ingresar un dni válido')
	print('debe ingresar una salida válida')
	print('debe ingresar un tipo de cheque válido')
	dni = ''
	salida = ''
	tipo_de_cheque = ''
	estado = 'NON'
	rango_fecha = 'NON'


# Tomando los 10 primeros caracteres de la cadena rango_fecha y convirtiéndola en un objeto datetime.
# Luego se toman los siguientes 10 caracteres de la cadena rango_fecha y se convierten en un objeto datetime
# objeto.
primera_fecha = datetime.strptime(rango_fecha[0:10], "%d/%m/%Y")
segunda_fecha = datetime.strptime(rango_fecha[11:21], "%d/%m/%Y")
# Convertir los objetos datetime en enteros.
timestamp1 = int(datetime.timestamp(primera_fecha))
timestamp2 = int(datetime.timestamp(segunda_fecha))

# Leer el archivo csv y añadir las líneas que coinciden con las condiciones a la lista info_cheque.
with open('test_itbank.csv', 'r') as file:
	lineas = csv.reader(file)
	info_cheque = []

	# Comprobando si los argumentos son válidos y añadiendo las líneas que cumplen las condiciones a la
	# lista info_cheque.
	if dni and salida and tipo_de_cheque:
		for linea in lineas:
			if dni == linea[-3] and tipo_de_cheque == linea[-2]:
				if estado == 'NON':
					if rango_fecha == 'NON':
						info_cheque.append(linea)
					elif timestamp1 <= int(linea[-4]) <= timestamp2:
						info_cheque.append(linea)
				elif estado == linea[-1]:
					if rango_fecha == 'NON':
						info_cheque.append(linea)
					elif timestamp1 <= int(linea[-4]) <= timestamp2:
						info_cheque.append(linea)

# Imprimir la lista info_cheque en la pantalla.
if salida == 'PANTALLA':
	print(info_cheque)

# Crear un archivo csv con el nombre del dni y el timestamp del momento en que se creó el archivo.
elif salida == 'CSV':
	tiempo = datetime.timestamp(datetime.now())
	with open(f"{dni}-{tiempo}.csv", 'w') as csv_file:
		csv_file.write(str(info_cheque))
	print(tiempo)
