import csv
from datetime import datetime
import sys

argumentos = sys.argv
if len(argumentos) > 1:
	dni = argumentos[1]
	salida = argumentos[2].upper()
	tipo_de_cheque = argumentos[3].upper()
	estado = argumentos[4].upper()
	rango_fecha = argumentos[5].upper()
else:
	print('debe ingresar un dni válido')
	print('debe ingresar una salida válida')
	print('debe ingresar un tipo de cheque válido')
	dni = ''
	salida = ''
	tipo_de_cheque = ''
	estado = 'NON'
	rango_fecha = 'NON'

primera_fecha = datetime.strptime(rango_fecha[0:10], "%d/%m/%Y")
segunda_fecha = datetime.strptime(rango_fecha[11:21], "%d/%m/%Y")
timestamp1 = int(datetime.timestamp(primera_fecha))
timestamp2 = int(datetime.timestamp(segunda_fecha))

with open('test_itbank.csv', 'r') as file:
	lineas = csv.reader(file)
	info_cheque = []

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

if salida == 'PANTALLA':
	print(info_cheque)

elif salida == 'CSV':
	tiempo = datetime.timestamp(datetime.now())
	with open(f"{dni}-{tiempo}.csv", 'w') as csv_file:
		csv_file.write(str(info_cheque))
	print(tiempo)
