import csv
from datetime import datetime
import sys

argumentos= sys.argv
if len(argumentos)>1:
    dni=argumentos[1]
    salida=argumentos[2].upper()
    tipoDeCheque=argumentos[3].upper()
    estado=argumentos[4].upper()
    rangoFecha=argumentos[5].upper()
else:
    print('debe ingresar un dni válido')
    print('debe ingresar una salida válida')
    print('debe ingresar un tipo de cheque válido')
    dni=''
    salida=''
    tipoDeCheque=''
    estado='NON'
    rangoFecha='NON'

print(sys.argv)

if rangoFecha != 'NON':
    primeraFecha=datetime.strptime(rangoFecha[0:10],"%d/%m/%Y")
    segundaFecha=datetime.strptime(rangoFecha[11:21],"%d/%m/%Y")
    timestamp1=int(datetime.timestamp(primeraFecha))
    timestamp2=int(datetime.timestamp(segundaFecha))

file=open('test_itbank.csv','r')
lineas=csv.reader(file)
infoCheque=[]

for linea in lineas:
    if dni and salida and tipoDeCheque:
        if dni==linea[-3] and tipoDeCheque==linea[-2]:
            if estado=='NON':
                if rangoFecha == 'NON':
                    infoCheque.append(linea)
                elif timestamp1<=int(linea[-4]) and timestamp2>=int(linea[-4]):
                    infoCheque.append(linea)
            elif estado==linea[-1]:
                if rangoFecha == 'NON':
                    infoCheque.append(linea)
                elif timestamp1<=int(linea[-4]) and timestamp2>=int(linea[-4]):
                    infoCheque.append(linea)

file.close

if salida=='PANTALLA':
    print(infoCheque)

elif salida=='CSV':
    tiempo = datetime.timestamp(datetime.now())
    archivo = open(f"{dni}-{tiempo}.csv", 'w')
    archivo.write(str(infoCheque))
    archivo.close
    print(tiempo)
